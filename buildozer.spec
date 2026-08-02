[app]
# (Раздел 1: Основные настройки приложения)
title = Lateness Tracker
package.name = lateness_tracker
package.domain = org.experiment
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1

# Требования для Kivy и SDL2 (автоматически подтягивает шрифты)
requirements = python3,kivy==2.3.0,sdl2_ttf

# (Раздел 2: Экран)
orientation = portrait
fullscreen = 0

# (Раздел 3: Настройки Android - КРИТИЧЕСКИ ВАЖНО)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b # Фиксируем стабильную версию NDK
android.archs = arm64-v8a
android.accept_sdk_license = True
android.enable_androidx = True # Важно для совместимости с новыми Android
android.bootstrap = sdl2 # Явно указываем загрузчик
android.entrypoint = main.py # Явно указываем точку входа
p4a.branch = master # Используем самую свежую версию python-for-android

[buildozer]
log_level = 2
warn_on_root = 1
