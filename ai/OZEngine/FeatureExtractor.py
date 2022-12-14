import os
import numpy as np
import pickle
import cv2
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model


class FeatureExtractor:
    def __init__(self, base_path):
        base_model = VGG16(weights='imagenet')
        # Customize the model to return features from fully-connected layer
        self.model = Model(inputs=base_model.input,
                           outputs=base_model.get_layer('fc1').output)

        self.base_path = base_path
        self.train_set_path = os.path.join(base_path, 'dataset', 'train_set')
        self.validation_set_path = os.path.join(base_path, 'dataset', 'validation_set')
        self.model_set_path = os.path.join(base_path, 'model')
        try:
            self.getFeatures()
        except Exception as e:
            print('Feature Load 실패!', e)


    def getFeatures(self):
        # Load feature maps
        self.features = np.load(os.path.join(self.model_set_path, 'feature_vector.npy'))

        # Load img paths
        path = os.path.join(self.model_set_path, 'img_paths')
        with open(path, "rb") as fr:
            self.img_paths = pickle.load(fr)

        # Load classes
        path = os.path.join(self.model_set_path, 'classes')
        with open(path, "rb") as fr:
            self.classes = pickle.load(fr)

    def get_train_paths(self, train_set_path):
        train_paths = []
        for (root, dirs, files) in os.walk(train_set_path):
            if len(dirs) == 0:
                for file_name in files:
                    train_paths.append(os.path.join(root, file_name))
        return train_paths

    def train(self):
        features = []
        img_paths = []
        classes = []

        train_paths = self.get_train_paths(self.train_set_path)

        for img_path in train_paths:
            class_name = img_path.split('/')[-2]
            img = cv2.imread(img_path)
            feature = self.extract(img=img)
            features.append(feature)
            img_paths.append(img_path)
            classes.append(class_name)

        
        feature_path = os.path.join(self.model_set_path, 'features')
        img_path = os.path.join(self.model_set_path, 'img_paths')
        class_path = os.path.join(self.model_set_path, 'classes')

        np.save(feature_path, features)

        with open(img_path, 'wb') as f:
            pickle.dump(img_paths, f)

        with open(class_path, 'wb') as f:
            pickle.dump(classes, f)

    def evaluate(self):
        all_cnt = 0
        cnt = 0
        for (root, dirs, files) in os.walk(self.validation_set_path):
            if len(dirs) == 0:
                for file_name in files:
                    path = os.path.join(root, file_name)
                    kind = path.split('/')[-2]
                    img = cv2.imread(path)
                    res = self.predict(img)

                    res_kind = res[1]
                    print('res vs kind ', res_kind, kind)
                    if res_kind == kind:
                        cnt += 1
                    all_cnt += 1
        return cnt / all_cnt * 100

    def predict(self, img):
        query = self.extract(img)
        dists = np.linalg.norm(features - query, axis=1)
        id = np.argsort(dists)[0]
        
        return (dists[id], self.classes[id], self.img_paths[id], id)
        

    def extract(self, img):
        img = cv2.resize(img, (224, 224))
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        x = np.array(rgb)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        feature = self.model.predict(x, verbose=0)[0]
        return feature / np.linalg.norm(feature)
