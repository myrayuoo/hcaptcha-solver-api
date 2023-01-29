import requests, tempfile, random, string, tensorflow as tf, shutil, numpy as np, os, httpx, cv2
from difflib import SequenceMatcher

classes = ['apple', 'banana on a plate', 'lemon on a tree', 'pineapple on a plate', 'rough sea', 'squirrel eating a nut', 'strawberry on a plate', 'strawberry on tree']
model = tf.keras.models.load_model('./model')

def Predict(word_to_find, img_data):
    temp_dir = tempfile.mkdtemp()
    image_name = "".join(random.choice(string.ascii_letters) for x in range(10)) + ".jpg"; image_path = f'{temp_dir}/{image_name}'
    with open(image_path , "wb") as handler:handler.write(img_data)
    img = tf.keras.utils.load_img(image_path, target_size=(140, 140))
    img_array = tf.keras.utils.img_to_array(img)
    shutil.rmtree(temp_dir) 
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    predicted_vechicle = classes[np.argmax(score)]
    print(predicted_vechicle)
    if word_to_find == predicted_vechicle  or (SequenceMatcher(a=word_to_find,b=predicted_vechicle).ratio() > 0.75 and len(predicted_vechicle == len(word_to_find))):
        return 'True'
    else:
        return 'False'
