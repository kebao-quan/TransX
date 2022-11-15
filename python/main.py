from ocr import detect_text
from translate_func import deepl_translate as net_translate
import cv2
import matplotlib.pyplot as plt
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


#TODO
def decided_blur_strength():
    return 51


def medianBlur(path, position):

    x1, x2 = position[0][1], position[2][1]
    y1, y2 = position[0][0], position[1][0]

    img = cv2.imread(path)
    img_tmp = img[x1:x2,y1:y2,:]
    # plt.imsave("./test_tmp.png",img_tmp)

    img_tmp = cv2.medianBlur(img_tmp, decided_blur_strength())

    img[x1:x2,y1:y2,:] = img_tmp

    return img


def main(args):
    # image_path = r"/Users/kyoma/project/TransX/image_ocr/image4.png"

    # org text: text[0], position: text[1]
    text = detect_text(args.imagePath)


    # trains text 
    target = "ZH"
    trans_text = net_translate(target, text[0])


    # pic without word
    img_blur = medianBlur(args.imagePath, text[1])
    plt.imsave(args.blurPath,img_blur)

    tb = Textbox(text[1],text[0],trans_text)

    # fount size TODO

    # pic with word TODO

    jsonStr = json.dumps(tb.__dict__)
    print(jsonStr)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('rootDir', type=str, help='root dir')
    parser.add_argument('imagePath', type=str, help='orginal image')
    parser.add_argument('blurPath', type=str, help='image without any word')
    parser.add_argument('downloadPath', type=str, help='image with translated word')
    args = parser.parse_args()
    # args.filePath = sys.argv[0]
    # args.rootDir = sys.argv[1]
    # args.imagePath = sys.argv[2]
    # args.blurPath = sys.argv[3]
    # args.downloadPath = sys.argv[4]
    # print(args)
    main(args)
