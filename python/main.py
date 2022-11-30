# -*- coding: UTF-8 -*-
from ocr import detect_text
from translate_func import deepl_translate as net_translate
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import json
import argparse


class Textbox(object):
    def __init__(self, position, text_org=None, text_trans=None):
        x1, x2 = position[0][1], position[2][1]
        y1, y2 = position[0][0], position[1][0]

        self.margin_left = min(x1, x2)
        self.margin_top = min(y1, y2)
        self.width = abs(x1-x2)
        self.height = abs(y1-y2)
        self.text_org = text_org
        self.text_trans = text_trans

def create_dict(tb_list):
    block_dir = {}
    for i in range(len(tb_list)):
        block_dir[f"block_{i}"] = tb_list[i].__dict__

    data_dir = {}
    data_dir["blocks"] = block_dir
    data_dir["path"] = "you_path"

    return data_dir


#TODO
def decided_blur_strength():
    return 53


def medianBlur(img, position):
    x1, x2 = position[0][1], position[2][1]
    y1, y2 = position[0][0], position[1][0]

    red = 3
    if x1 - red >= 0:
        x1 = x1 - red

    if y1 - red >= 0:
        y1 = y1 - red

    if x2 + red < img.shape[0]:
        x2 = x2 + red

    if y2 + red < img.shape[1]:
        y2 = y2 + red

    img_tmp = img[x1:x2,y1:y2,:]
    # plt.imsave("./test_tmp.png",img_tmp)
    img_tmp = cv2.medianBlur(img_tmp, decided_blur_strength())
    img[x1:x2,y1:y2,:] = img_tmp
    return img


def main(args):
    texts = detect_text(args.imagePath,args)
    img_blur = mpimg.imread(args.imagePath)
    img_blur = img_blur.copy()
    tb_list = []

    for text in texts:
        # trains text 
        target = "ZH"
        trans_text = net_translate(target, text[0])

        # pic without word        
        img_blur = medianBlur(img_blur, text[1])

        # fount size TODO

        # pic with word TODO

        tb = Textbox(text[1],text[0],trans_text)
        tb_list.append(tb)

    data = create_dict(tb_list)
    jsonStr = json.dumps(data)
    print(jsonStr)
    plt.imsave(args.blurPath,img_blur)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('rootDir', type=str, help='root dir')
    parser.add_argument('imagePath', type=str, help='orginal image')
    parser.add_argument('blurPath', type=str, help='image without any word')
    parser.add_argument('downloadPath', type=str, help='image with translated word')
    args = parser.parse_args()
    main(args)
