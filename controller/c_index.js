const fs = require('fs');
const path = require('path');
const rootDir = require('../util/path');

const defaultContext = {
    title: "TranX1",
    paragraphs: [{text: "aaaaaaaaaa", left: 20, top: 30}    ,
                 {text: "bbbbbbbbbb", left: 30, top: 40},
                 {text: "cccccccccc", left: 100, top: 100}]
}

exports.render = (req, res, next) => {
    var context = req.session.context;
    req.session.destroy();
    if (context === undefined)
    {
        console.log("Rendering default context");
        context = defaultContext;
    }
    res.render('index', context);
}

exports.downloadFile = (req, res, next) => {
    let downloadPath = path.join(rootDir, 'download');
    let filename = req.params.filename;
    let fullPath = path.join(downloadPath, filename);
    fs.readFile(fullPath, (err, data) => {
        if (err)
        {
            return next(err)
        }
        let tmp = filename.split('-')[1].split('.');
        let downloadFileName = tmp[0]+'-zh.'+tmp[1];
        res.setHeader('Content-Disposition', 'attachment; filename="' + downloadFileName + '"')
        res.send(data);
    })
}

