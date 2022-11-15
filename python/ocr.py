import os
import io
from google.cloud import vision




def detect_text(path,args):
    """Detects text in the file."""
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(args.rootDir, "python","config","windy-nova-364604-7a2df3513239.json")
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    ret = []
    text = texts[0]
    #print(text)
    vertices = ([(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
    ret.append(text.description)
    ret.append(vertices)
    
    return ret


    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))
        

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
        
# image = r"C:\TranX\image_ocr\image4.png"


# text = detect_text(image)


# print(text[0])
# print(text[1])