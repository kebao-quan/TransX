var express = require('express');
var router = express.Router();

const multer = require('multer');
//const { path } = require('../app');
// 指定上传到服务器的目录

const path = require('path')
const rootDir = require('../util/path')

const upload = multer({dest:'upload'})
/* GET home page. */
router.get('/', function(req, res, next) {
  res.sendFile(path.join(rootDir, 'views', 'index.html'));
  //res.render('index', { title: 'Express!!!' });
});


router.post('/upload',upload.single('xxx'),function(req,res){
    console.log(req.file.originalname);
    res.send('上传成功')
})

module.exports = router;
