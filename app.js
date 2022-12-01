var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
const session = require('express-session');

const rootDir = require('./util/path')


var indexRouter = require('./routes/index').router;
var usersRouter = require('./routes/users');
var upload = require('./routes/upload.js');
var download = require('./routes/download.js');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');



app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(
  session({
    secret: 'mySecret',
    resave: false,
    saveUninitialized: false,
    cookie: {
      expires: 60000
    }
  })
);

// Get function in which send session as routes.
app.get('/session', function (req, res, next) {
  if (req.session.views) {
// Increment the number of views.
    req.session.views++
// Session will expires after 1 min
// of in activity
    res.write('<p> Session expires after 1 min of in activity: ' + (req.session.cookie.expires) + '</p>')
    res.end()
  } else {
    req.session.views = 1
    res.end(' New session is started')
  }
})

app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/upload', upload.router);
//app.use('/download', download.router);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  //res.send('404');
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
