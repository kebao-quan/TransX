var express = require('express');
var router = express.Router();
const indexController = require('../controller/c_index');





router.get('/:filename', indexController.downloadFile)




exports.router = router;
