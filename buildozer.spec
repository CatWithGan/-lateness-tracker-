[app]
# (Раздел 1: Основное)
title = Lateness Tracker
package.name = lateness_tracker
package.domain = org.experiment
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1

# Оставляем только самое необходимое
requirements = python3,kivy==2.3.0

# (Раздел 2: Экран)
orientation = portrait
fullscreen = 0

# (Раздел 3: Android)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.enable_androidx = True

# Явное указание точки входа и движка
android.bootstrap = sdl2
android.entrypoint = main.py

# Используем ветку master для python-for-android
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
