[app]

# (str) Title of your application
title = MIT OpenCourseWare

# (str) Package name
package.name = mit-ocw

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Icon of the application
icon.filename = %(source.dir)s/30664.png

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Note: kivy 2.3.0 or higher is required for modern Android API targets
requirements = python3,kivy,kivymd

# (str) Supported orientations (landscape, sensorLandscape, portrait, or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions required by the app
android.permissions = INTERNET

# (int) Target Android API for Android 16
android.api = 36

# (int) Minimum API supported (API 24 = Android 7.0+)
android.minapi = 24

# (str) Android NDK version (NDK r28c is required for 16 KB page size support on Android 16)
android.ndk = 28c

# (int) Android NDK API (usually matches minapi)
android.ndk_api = 24

# (str) Use the develop branch of python-for-android for API 36 toolchain support
p4a.branch = develop

# (list) Architectures to build for (64-bit arm64-v8a is required for modern Android)
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Accept Android SDK licenses automatically
android.accept_sdk_license = True

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug including commands output)
log_level = 0

# (int) Display warning if buildozer is run as root (0 = ignore, 1 = warn)
warn_on_root = 0

