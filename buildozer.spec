[app]
# (Раздел 1: Основные настройки приложения)
title = Lateness Tracker
package.name = lateness_tracker
package.domain = org.experiment
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1

# Добавлены hostpython3, libffi и openssl для исправления ошибки линковщика
requirements = python3,kivy==2.3.0,hostpython3,libffi,openssl

# (Раздел 2: Настройки экрана)
orientation = portrait
fullscreen = 0

# (Раздел 3: Настройки Android — пуленепробиваемый конфиг)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.bootstrap = sdl2
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
