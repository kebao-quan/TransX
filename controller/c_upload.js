let {PythonShell} = require('python-shell')
const rootDir = require('../util/path');
const path = require('path');
var PythonPath = path.join(rootDir, 'python', 'main.py')
const fs = require('fs');


function extractParagraph(context)
{
  let paragraphs = [];
  for (const [key_, value_] of Object.entries(context["blocks"])) {
    let style = "";
    let text_org = "";
    let text_trans = "";
    for (const [key, value] of Object.entries(value_)) {
        //console.log(key, value);
        switch (key) {
            case "margin_left":
                style = style.concat("margin-left: ", value, "px; ");
                break;
            case "margin_top":
                style = style.concat("margin-top: ", value, "px; ");
                break;
            case "width":
                style = style.concat("width: ", value, "px; ");
                break;
            case "height":
                style = style.concat("height: ", value, "px; ");
                break;
            case "text_org":
                text_org = value;
                break;
            case "text_trans":
                text_trans = value;
                break;
            case "font_size":
                style = style.concat("font-size: ", value, "px; ");
                break;
            case "line_space":
                style = style.concat("line-height: ", value, "; ");
                break;
            default:
                break;
        }
    }
    let tmp = {
        style: style,
        text_org: text_org,
        text_trans: text_trans
    }
    paragraphs.push(tmp)
  }
  return paragraphs
}

exports.postUpload = (req, res, next) => {
    console.log(req.fileName);
    imagePath = path.join(rootDir, 'upload', req.fileName);
    originPath = path.join(rootDir, 'public', 'image', 'original', req.fileName);
    blurPath = path.join(rootDir, 'public', 'image', 'blured');
    blurPathFull = path.join(rootDir, 'public', 'image', 'blured', req.fileName);
    downloadPath = path.join(rootDir, 'download');
    downloadPathFull = path.join(rootDir, 'download', req.fileName);
    fs.copyFile(imagePath, originPath, (err) => {
        if (err) 
        {
            console.log(err.message)
            throw err;
        }
    });

    //redundent
    fs.copyFile(imagePath, path.join(downloadPath, req.fileName), (err) => {
        if (err) 
        {
            console.log(err.message)
            throw err;
        }
    });
    
    var options = {
        mode: 'text',
        args: [rootDir, imagePath, blurPathFull, downloadPathFull]
    };

    PythonShell.run(PythonPath, options, function (err, results) {
        if (err) 
        {
            console.log(err.message);
            next(err);
            throw err;
        }
 
        console.log(req.session.context);
        req.session.context = JSON.parse(results[0]);
        req.session.context.originPath = '/image/original/' + req.fileName;
        req.session.context.blurPath = '/image/blured/' + req.fileName;
        req.session.context.downloadPath = downloadPath;
        req.session.context.fileName = req.fileName;

        //extract paragraph
        req.session.context.paragraphs = extractParagraph(req.session.context);

        console.log(req.session.context);
        res.redirect('/');
    });
}