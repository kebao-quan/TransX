import os
import io
import numpy as np
from google.cloud import vision

def detect_text(path,args):
    """Detects text in the file."""
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(args.rootDir, "python","config","windy-nova-364604-7a2df3513239.json")
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    # texts = response.text_annotations
    
    # text = texts[0]
    #print(text)

    # ret = []
    # vertices = ([(vertex.x, vertex.y)
    #                 for vertex in text.bounding_poly.vertices])
    # ret.append(text.description)
    # ret.append(vertices)
    
    # return ret

    # ret = []

    # for text in texts[1:]:
    #     vertices = ([(vertex.x, vertex.y)
    #                     for vertex in text.bounding_poly.vertices])
    #     ret.append((text.description,vertices))

    # if response.error.message:
    #     raise Exception(
    #         '{}\nFor more info on error messages, check: '
    #         'https://cloud.google.com/apis/design/errors'.format(
    #             response.error.message))

    # return ret


    rets = []
    blocks = response.full_text_annotation.pages[0].blocks
    for block in blocks:
        for paragraph in block.paragraphs:
            font_size_list = []
            line_space_list = []
            last_y = 0
            text = ""
            # get test
            for word in paragraph.words:
                for symbol in word.symbols:
                    end = ""
                    type_ = str(symbol.property.detected_break.type_)
                    if type_=="BreakType.SPACE" or type_=="BreakType.EOL_SURE_SPACE" or type_=="BreakType.SURE_SPACE":
                        end = " "

                    if type_=="BreakType.EOL_SURE_SPACE":
                        line_space_list.append(symbol.bounding_box.vertices[0].y-last_y)
                        last_y = symbol.bounding_box.vertices[0].y

                    text += symbol.text + end
                    font_size_list.append(symbol.bounding_box.vertices[1].x - symbol.bounding_box.vertices[0].x)
            # get box
            vertices = ([(vertex.x, vertex.y) for vertex in paragraph.bounding_box.vertices])
            font_size = np.median(np.array(font_size_list))           
            line_space = np.median(np.array(line_space_list)) / font_size * 0.75
            if np.isnan(line_space) or line_space < 1.2 or line_space > 3:
                line_space = 1.35
        
            rets.append([text, vertices, font_size, line_space])

    return rets
        
# image = r"C:\TranX\image_ocr\image4.png"


# text = detect_text(image)


# print(text[0])
# print(text[1])