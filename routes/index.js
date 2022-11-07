var express = require('express');
var router = express.Router();


const indexController = require('../controller/c_index');
const { route } = require('./users');

/* GET home page. */
router.get('/', indexController.render);





exports.router = router;
