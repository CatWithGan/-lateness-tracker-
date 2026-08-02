[app]
# (Раздел 1: Основные настройки приложения)
title = Lateness Tracker
package.name = lateness_tracker
package.domain = org.experiment
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy==2.3.0

# (Раздел 2: Экран)
orientation = portrait
fullscreen = 0

# (Раздел 3: Настройки Android — отдаем управление Buildozer)
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
