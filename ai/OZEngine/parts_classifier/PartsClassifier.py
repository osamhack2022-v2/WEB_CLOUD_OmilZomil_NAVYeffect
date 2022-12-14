import numpy as np
import os
import pickle
from PIL import Image
from OZEngine.FeatureExtractor import FeatureExtractor

def distFunc(x):
    return -0.6*x + 1
class PartsClassifier(FeatureExtractor):
    def __init__(self, dress_kind):
        project_path = os.path.join(os.environ['AI_PATH'], 'OZEngine', 'parts_classifier')
        if dress_kind == 'navy_service_uniform':
            base_url = os.path.join(project_path, 'NavyServiceUniform')
        elif dress_kind == 'full_dress_uniform':
            base_url = os.path.join(project_path, 'FullDressUniform')
        elif dress_kind == 'combat_uniform':
            base_url = os.path.join(project_path, 'CombatUniform')
        super().__init__(base_url)

    def predict(self, img):
        query = super().extract(img)
        dists = np.linalg.norm(self.features - query, axis=1)
        id = np.argsort(dists)[0]
        dist = dists[id]
        kind = self.classes[id]
        if dist < 1:
            return (distFunc(dist), kind, id)
        else:
            return (None, None, None)

if __name__ == '__main__':
    pc = PartsClassifier('navy_service_uniform')
    res = pc.evaluate()
    print(res)