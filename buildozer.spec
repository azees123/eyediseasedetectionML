[app]

# Title of your application
title = Eye Disease Detector

# Package name
package.name = eyediseasedetector

# Package domain (needed for android/ios packaging)
package.domain = org.eyedetector

# Source code where the main.py is
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,tflite

# Main application file
main.py = eyedisease.py

# Requirements
requirements = python3,kivy,plyer,Pillow,numpy,tflite_runtime~=2.14.0

# Android specific
android.arch = arm64-v8a
android.ndk = 25.2.9519653
android.sdk = 31
android.minapi = 21
android.ndk_path = /path/to/your/ndk/25.2.9519653  # Update this path
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Orientation
orientation = portrait

# Log level
log_level = 2

# Presplash
presplash.filename = %(source.dir)s/data/presplash.png

# Icon
icon.filename = %(source.dir)s/data/icon.png

# Kivy version to use
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

[buildozer]

# Buildozer options
log_level = 2
warn_on_root = 1
