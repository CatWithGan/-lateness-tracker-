[app]
# (Раздел 1: Основное)
title = Lateness Tracker
package.name = lateness_tracker
package.domain = org.experiment
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy==2.3.0

# (Раздел 2: Настройки экрана)
orientation = portrait
fullscreen = 0

# (Раздел 3: Настройки Android - КРИТИЧЕСКИ ВАЖНО)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25.2.9519653
android.archs = arm64-v8a
android.accept_sdk_license = True
android.bootstrap = sdl2
p4a.branch = master # Используем самую свежую версию python-for-android

[buildozer]
log_level = 2
warn_on_root = 1
