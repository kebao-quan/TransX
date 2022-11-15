let {PythonShell} = require('python-shell')
const rootDir = require('../util/path');
const path = require('path');
var PythonPath = path.join(rootDir, 'python', 'main.py')
const fs = require('fs');

exports.postUpload = (req, res, next) => {
    console.log(req.fileName);
    imagePath = path.join(rootDir, 'upload', req.fileName);
    originPath = path.join(rootDir, 'public', 'image', 'original', req.fileName);
    blurPath = path.join(rootDir, 'public', 'image', 'blured');
    downloadPath = path.join(rootDir, 'download');

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
        args: [rootDir, imagePath, blurPath, downloadPath]
    };

    PythonShell.run(PythonPath, options, function (err, results) {
        if (err) 
        {
            console.log(err.message);
            next(err);
            throw err;
        }
 
        console.log(req.session.context)
        req.session.context = JSON.parse(results[0]);
        req.session.context.originPath = '/image/original/' + req.fileName;
        req.session.context.downloadPath = downloadPath;
        req.session.context.fileName = req.fileName
        res.redirect('/');
    });
}