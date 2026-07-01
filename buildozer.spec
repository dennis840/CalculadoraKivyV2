[app]

title = Calculadora
package.name = calculadora
package.domain = org.dennis

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0


android.api = 33
android.minapi = 24

android.ndk = 25c
android.ndk_api = 24

android.accept_sdk_license = True

android.archs = arm64-v8a

android.allow_backup = True

android.copy_libs = 1

android.debug_artifact = apk

[buildozer]

log_level = 2
warn_on_root = 1
