const fs = require('fs');
const path = require('path');
const rootDir = require('../util/path');

const defaultContext = {
    title: "TransX",
    paragraphs: []
}

exports.render = (req, res, next) => {
    var context = req.session.context;
    req.session.destroy();
    if (context === undefined)
    {
        context = defaultContext;
    }
    res.render('index', context);
}

// exports.downloadFile = (req, res, next) => {
//     let downloadPath = path.join(rootDir, 'download');
//     let filename = req.params.filename;
//     let fullPath = path.join(downloadPath, filename);
//     fs.readFile(fullPath, (err, data) => {
//         if (err)
//         {
//             return next(err)
//         }
//         let tmp = filename.split('-')[1].split('.');
//         let downloadFileName = tmp[0]+'-zh.'+tmp[1];
//         res.setHeader('Content-Disposition', 'attachment; filename="' + downloadFileName + '"')
//         res.send(data);
//     })
// }

