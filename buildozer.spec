[app]
title = Dokeh Dar
package.name = dokehdar
package.domain = org.dokehdar

source.dir = .
source.include_exts = py,png,jpg,jpeg,otf,ttf,mp3,wav,ogg,json,kv,atlas
source.exclude_dirs = .git,.github,bin,.buildozer,__pycache__
# فایل‌های ذخیره دسکتاپ داخل APK نرود
source.exclude_patterns = progress.json,layout_save.json,customer_layout.json,students.json

version = 0.1

requirements = python3,kivy==2.3.0,arabic-reshaper==3.0.0,python-bidi==0.4.2,six

orientation = landscape
fullscreen = 1

# بازی به اینترنت یا دسترسی خاصی نیاز ندارد
android.permissions =

android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
