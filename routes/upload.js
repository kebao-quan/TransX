var express = require('express');
var router = express.Router();
const multer = require('multer');


const path = require('path');

const rootDir = require('../util/path');
const uploadController = require('../controller/c_upload')


const fileStorage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'public/image/original');
    },
    filename: (req, file, cb) => {
        req.fileName = new Date().toISOString().replace(/[-:.]/g,"") + '-' + file.originalname;
        cb(null, req.fileName);
    }
})

const fileFilter = (req, file, cb) => {
    if (file.mimetype === 'image/png')
    {
        cb(null, true);
    } else {
        cb(null, false);
    }
}

const upload = multer({
    storage:fileStorage,
    fileFilter: fileFilter
})

router.post('/', upload.single('image'), uploadController.postUpload)



exports.router = router;
