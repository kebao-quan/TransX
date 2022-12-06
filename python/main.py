# -*- coding: UTF-8 -*-
from ocr import detect_text
from translate_func import deepl_translate as net_translate
import cv2
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
import os
import sys
import json
import argparse
from time import sleep
from threading import Thread


class Textbox(object):
    def __init__(self, position, text_org=None, text_trans=None, font_size=16, line_space=1.5, color="#000000"):
        x1, x2 = position[0][1], position[2][1]
        y1, y2 = position[0][0], position[1][0]

        self.margin_left = min(y1, y2) 
        self.margin_top = min(x1, x2)
        self.width = abs(y1-y2)
        self.height = abs(x1-x2)
        self.text_org = text_org
        self.text_trans = text_trans
        self.font_size = font_size
        self.line_space = line_space
        self.font_color = color


def create_dict(tb_list):
    block_dir = {}
    for i in range(len(tb_list)):
        block_dir[f"block_{i}"] = tb_list[i].__dict__

    data_dir = {}
    data_dir["blocks"] = block_dir
    data_dir["path"] = "you_path"

    return data_dir


#TODO
def blur_strength():
    return 53

# def async(f):
#     def wrapper(*args, **kwargs):
#         thr = Thread(target=f, args=args, kwargs=kwargs)
#         thr.start()
#     return wrapper

# @async
def del_image(imgs_path):
    sleep(10)
    for img in imgs_path:
        os.remove(img)



def medianBlur(img, position):
    x1, x2 = position[0][1], position[2][1]
    y1, y2 = position[0][0], position[1][0]

    red = 8
    if x1 - red >= 0:
        x1 = x1 - red

    if y1 - red >= 0:
        y1 = y1 - red

    if x2 + red < img.shape[0]:
        x2 = x2 + red

    if y2 + red < img.shape[1]:
        y2 = y2 + red

    img_tmp = img[x1:x2,y1:y2,:]
    img_tmp = cv2.medianBlur(img_tmp, blur_strength())
    img[x1:x2,y1:y2,:] = img_tmp
    return img


def main(args):
    texts = detect_text(args.imagePath,args)
    img_blur = cv2.imread(args.imagePath)
    img_blur = img_blur.copy()
    tb_list = []

    for text in texts:
        # trains text 
        trans_text = net_translate(args.target, text[0])

        # pic without word        
        img_blur = medianBlur(img_blur, text[1])

        # font_size = 
        font_size = text[2]

        if args.target == "ZH":
            font_size = font_size * 1.70
        else:
            font_size = font_size * 1.5
        # pic with word TODO

        tb = Textbox(position=text[1],text_org=text[0],text_trans=trans_text, font_size=font_size, line_space=text[3])
        tb_list.append(tb)

    data = create_dict(tb_list)
    jsonStr = json.dumps(data)
    cv2.imwrite(args.blurPath,img_blur)
    print(jsonStr)
    

    # del image
    del_image([args.blurPath, args.imagePath])

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('rootDir', type=str, help='root dir')
    parser.add_argument('imagePath', type=str, help='orginal image')
    parser.add_argument('blurPath', type=str, help='image without any word')
    parser.add_argument('target', type=str, help='target language')
    args = parser.parse_args()
    # args.target = "ZH"
    main(args)
