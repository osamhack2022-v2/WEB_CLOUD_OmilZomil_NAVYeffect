import time
import sys
import numpy as np
import re
from .UniformChecker import UniformChecker
from OZEngine.dress_classifier import classification2
from OZEngine.lib.utils import sortContoursByArea, getVertexCnt, getContourCenterPosition, getRectCenterPosition, isPointInBox
from OZEngine.lib.defines import *
from OZEngine.lib.ocr import OCR
from OZEngine.lib.utils import plt_imshow

# (동)정복 검사


class CombatUniformChecker(UniformChecker):
    def __init__(self, train_mode):
        # hyperparameter
        filter = {
            'name_tag': {
                'lower': (0, 30, 0), 
                'upper': (255, 255, 255)
            },
            'flag_tag': {
                'lower': (100, 10, 60), 
                'upper': (255, 255, 255)
            }
        }
        super().__init__(filter, 'combat_uniform', train_mode)
        self.name_cache = None
        self.debug_cnt = 0

        self.W = 0

        self.result_dic = {'component':{}, 'box_position':{}, 'masked_img':{}, 'probability':{}}

    def getPosition(self, contour):
        center_p = getContourCenterPosition(contour)
        position = 'left' if center_p[0] < (self.W//2) else 'right'
        return position
    

    def isNameTag(self, position, kind):
        return position == 'left' and kind == 'name_tag'

    def isInsigniaTag(self, position, kind):
        return position == 'right' and kind == 'insignia_tag'

    def isFlagTag(self, position, kind):
        return position == 'left' and kind == 'flag_tag'

    def isRankTag(self, position, kind):
        return position == 'right' and kind is not None and kind.find('rank_tag') != -1

    def checkUniform(self, org_img):
        img = org_img
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        H, W = img.shape[: 2]
        self.W = W
        self.result_dic = {'component':{}, 'box_position':{}, 'masked_img':{}, 'probability':{}}


        # 이름표, 부대마크, 계급장 체크
        contours, _,  self.result_dic['masked_img']['name_tag'] = self.getMaskedContours(
            img=img, hsv_img=hsv_img, kind='name_tag', sort=True, reverse=True, morph='erode2dilate')

        if contours is not None:
            for contour in contours:
                is_name_tag = self.result_dic['component'].get('name_tag')
                is_rank_tag = self.result_dic['component'].get('rank_tag')
                is_insignia_tag = self.result_dic['component'].get('insignia_tag')
                
                area = cv2.contourArea(contour)
                if area > 10000:
                    continue

                if is_name_tag and is_rank_tag and is_insignia_tag or (area < 500):
                    break

                position = self.getPosition(contour)

                tmp_box_position = cv2.boundingRect(contour)
                x,y,w,h = tmp_box_position
                parts_img = img[y:y+h, x:x+w]

                isCenter = x < W//2 < x+w

                if self.train_mode:
                    probability, kind = 0, 'name_tag2'
                else:
                    probability, kind = self.parts_classifier.predict(parts_img)[:2]

                if not is_name_tag and self.isNameTag(position, kind):
                    # 이름표 OCR
                    if self.name_cache:
                        box_position = tmp_box_position
                        component = self.name_cache
                    else:
                        # pass
                        ocr_list = OCR(img)
                        self.debug_cnt += 1
                        box_position, component = self.getName(contour, ocr_list, is_strict=True)
                        self.name_cache = component

                    self.result_dic['box_position']['name_tag'] = box_position
                    self.result_dic['component']['name_tag'] = component
                    self.result_dic['probability']['name_tag'] = probability
                
                if not is_rank_tag and self.isRankTag(position, kind):
                    self.result_dic['box_position']['rank_tag'] = tmp_box_position
                    rank_n = kind.split('+')[1]
                    self.result_dic['component']['rank_tag'] = Classes.dic.get(int(rank_n))
                    self.result_dic['probability']['rank_tag'] = probability

                if not is_insignia_tag and self.isInsigniaTag(position, kind):
                    self.result_dic['box_position']['insignia_tag'] = tmp_box_position
                    self.result_dic['component']['insignia_tag'] = True
                    self.result_dic['probability']['insignia_tag'] = probability

        contours, _,  self.result_dic['masked_img']['flag_tag'] = self.getMaskedContours(
            img=img, hsv_img=hsv_img, kind='flag_tag', sort=True)

        if contours is not None:
            for contour in contours:
                area = cv2.contourArea(contour)
                if area < 500:
                    break

                position = self.getPosition(contour)

                tmp_box_position = cv2.boundingRect(contour)
                x,y,w,h = tmp_box_position
                parts_img = img[y:y+h, x:x+w]

                isCenter = x < W//2 < x+w

                if self.train_mode:
                    probability, kind = 0, 'name_tag2'
                else:
                    probability, kind = self.parts_classifier.predict(parts_img)[:2]

                if self.isFlagTag(position, kind):
                    self.result_dic['box_position']['flag_tag'] = tmp_box_position
                    self.result_dic['component']['flag_tag'] = True
                    self.result_dic['probability']['flag_tag'] = probability

        return self.result_dic
