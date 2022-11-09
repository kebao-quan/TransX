from image_ocr.ocr import detect_text
from translate_func import deepl_translate as net_translate
import cv2
import matplotlib.pyplot as plt


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


def main():
    image_path = r"/Users/kyoma/project/TransX/image_ocr/image4.png"

    # org text: text[0], position: text[1]
    text = detect_text(image_path)


    # trains text 
    target = "ZH"
    trans_text = net_translate(target, text[0])


    # pic without word
    img = medianBlur(image_path, text[1])
    # plt.imsave("./test.png",img)

    # fount size 



if __name__ == '__main__':
    main()