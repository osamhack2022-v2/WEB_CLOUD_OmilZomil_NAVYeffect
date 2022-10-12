import numpy as np
import os
import pickle
from PIL import Image
from OZEngine.parts_classifier import FeatureExtractor


class PartsClassifier():
    def __init__(self, dress_kind):
        if dress_kind == 'navy_service_uniform':
            super.__init__(dress_kind)

        self.feature_extractor = FeatureExtractor()

        model_set_path = './model'
        # Load feature maps
        path = os.path.join(model_set_path, 'features')
        self.features = np.load(os.path.join(feature_path, 'features.npy'))

        # Load img paths
        path = os.path.join(model_set_path, 'img_paths')
        with open(path, "rb") as fr:
            self.img_paths = pickle.load(fr)

        # Load classes
        path = os.path.join(model_set_path, 'classes')
        with open(path, "rb") as fr:
            self.classes = pickle.load(fr)

    

    def predict(self, img):
        query = self.feature_extractor.extract(img)
        dists = np.linalg.norm(self.features - query, axis=1)
        id = np.argsort(dists)[0]
        dist = dists[id]
        kind = self.classes[id]
        if dist < 1:
            return (dist, kind, id)
        else:
            return (None, None, None)

if __name__ == '__main__':
    pc = PartsClassifier('navy_service_uniform')
    pc.predict(img)