var express = require('express');
var router = express.Router();
const multer = require('multer');


const path = require('path');

const rootDir = require('../util/path');
const uploadController = require('../controller/c_upload');
const { nextTick } = require('process');


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
    if (file.mimetype === 'image/png' || file.mimetype === 'image/jpg' || file.mimetype === "image/jpeg")
    {
        cb(null, true);
    } else {
        cb(null, false);
        return cb(new Error("Only .png, .jpg, and .jpeg format allowed!"))
    }
}

const maxSize = 2 * 1024 * 1024
const upload = multer({
    storage:fileStorage,
    fileFilter: fileFilter,
    limits: {fileSize: maxSize}
})

router.post('/', upload.single('image'), uploadController.postUpload)


exports.router = router;
