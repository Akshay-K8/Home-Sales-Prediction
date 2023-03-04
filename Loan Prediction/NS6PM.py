def replacer(df):
    for i in df.columns:
        if(df[i].dtype=='object'):
            x=df[i].mode()[0]
            df[i]=df[i].fillna(x)
        else:
            x=df[i].mean()
            df[i]=df[i].fillna(x)



def seprate(df):
    cat=[]
    con=[]
    for i in df.columns:
        if(df[i].dtype=='object'):
            cat.append(i)
        else:
            con.append(i)
    return cat,con


def standardize(df):
    cat,con=seprate(df)
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    ss=StandardScaler()
    x1=pd.DataFrame(ss.fit_transform(df[con]),columns=con)
    return x1

def preprocess(df):
    cat,con=seprate(df)
    import pandas as pd
    x1=standardize(df)
    x2=pd.get_dummies(df[cat])
    Xnew=x1.join(x2)
    return Xnew

def outlier(df):
    x1=standardize(df)
    ol=[]
    for i in x1.columns:
        ol.extend(list(x1[(x1[i]>3)|(x1[i]<-3)].index))
    import numpy as np
    OL=np.unique(ol)
    df=df.drop(index=OL,axis=1)
    return df
    
def ANOVA(df,cat,con):
    from statsmodels.formula.api import ols
    eqn = str(con) + " ~ " + str(cat)
    model = ols(eqn,df).fit()
    from statsmodels.stats.anova import anova_lm
    Q = anova_lm(model)
    return round(Q.iloc[0:1,4:5].values[0][0],5)

def chisq(df,cat1,cat2):
    import pandas as pd
    from scipy.stats import chi2_contingency
    ct = pd.crosstab(df[cat1],df[cat2])
    a,b,c,d = chi2_contingency(ct)
    return round(b,5)