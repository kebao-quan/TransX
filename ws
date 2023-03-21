warning: in the working copy of '.gitignore', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.vscode/tasks.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'app.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'bin/www', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'config/windy-nova-364604-7a2df3513239.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'package-lock.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'package.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'public/stylesheets/output.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'public/stylesheets/style.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'python/.ipynb_checkpoints/debug-checkpoint.ipynb', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'python/debug.ipynb', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'python/image_ocr.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'python/test_translate_api.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'requirements.txt', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'routes/index.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'routes/upload.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'routes/users.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'tailwind.config.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'util/path.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'views/error.pug', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'views/index.pug', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'views/layout.pug', LF will be replaced by CRLF the next time Git touches it
[1mdiff --git a/python/main.py b/python/main.py[m
[1mindex 1521685..9361155 100644[m
[1m--- a/python/main.py[m
[1m+++ b/python/main.py[m
[36m@@ -119,6 +119,7 @@[m [mdef main(args):[m
     for pos in text_poss:[m
         img_blur = medianBlur(img_blur, pos)[m
 [m
[32m+[m[41m[m
     data = create_dict(tb_list)[m
     jsonStr = json.dumps(data)[m
     cv2.imwrite(args.blurPath,img_blur)[m
