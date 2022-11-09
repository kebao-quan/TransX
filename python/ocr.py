def detect_text(path):
    """Detects text in the file."""
    
    import os
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/Users/kyoma/project/TransX/config/windy-nova-364604-7a2df3513239.json"

    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    ret = []
    text = texts[0]
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