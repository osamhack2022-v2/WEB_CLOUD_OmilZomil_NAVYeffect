# Import the libraries
from random import uniform
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from pathlib import Path
from PIL import Image
import numpy as np
import os

def get_train_paths(train_set_path):
    train_paths = []
    model_paths = []
    for (root, dirs, files) in os.walk(train_set_path):
        d_split = root.strip('./').split('/')
        if len(d_split) == 3:
            train_dir_name, uniform_kind, parts_kind = d_split
            
            for file in files:
                train_paths.append(os.path.join(root, file))
                model_name = file.split('.')[0] + '.npy'
                model_paths.append(os.path.join('./model', uniform_kind, parts_kind, model_name))
    return train_paths, model_paths

class FeatureExtractor:
    def __init__(self):
        base_model = VGG16(weights='imagenet')
        # Customize the model to return features from fully-connected layer
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)
        
    def extract(self, img):
        img = img.resize((224, 224))
        img = img.convert('RGB')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        feature = self.model.predict(x)[0]
        return feature / np.linalg.norm(feature)

train_set_path = './trainset'
train_paths, model_paths = get_train_paths(train_set_path)
print(train_paths, model_paths)

fe = FeatureExtractor()
for img_path, feature_path in zip(train_paths, model_paths):
    print(img_path, feature_path)
    feature = fe.extract(img=Image.open(img_path))
    np.save(feature_path, feature)