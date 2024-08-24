from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model

model = load_model('./Fruit_detection.h5')

class_labels=['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 'cauliflower', 
              'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi', 
              'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple', 'pomegranate',
            'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato', 'turnip', 'watermelon']

def predict_image(img_path):
  img = image.load_img(img_path, target_size=(224, 224))
  plt.imshow(img)
  plt.show()
  img = image.img_to_array(img)
  img = np.expand_dims(img, axis=0)
  img = img/255

  prediction = model.predict(img)
  predicted_class = np.argmax(prediction)
  predicted_label = class_labels[predicted_class]

  print("Predicted Class:", predicted_class)
  print("Predicted Label:", predicted_label)

# Replace 'path/to/your/image.jpg' with the actual path to your image
predict_image('./kiwi.jpg')
