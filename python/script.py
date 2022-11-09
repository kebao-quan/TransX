import sys
import json

filePath = sys.argv[0]
rootDir = sys.argv[1]
imagePath = sys.argv[2]
blurPath = sys.argv[3]
downloadPath = sys.argv[4]

#TODO:
#Generate blured image at blurPath
#Generate download file at downloadPath
#Add render property to context






context = {
    'title': 'TranX',
    'filePath': filePath
}
contextJson = json.dumps(context)
print(contextJson)