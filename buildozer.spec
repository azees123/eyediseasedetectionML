[app]
title = Eye Disease Detector
package.name = eyediseasedetector
package.domain = org.eyedetector
source.dir = .
source.include_exts = py,png,jpg,kv,tflite
main.py = eyedisease.py

# Updated requirements with specific versions
requirements = 
    python3==3.9.13,
    kivy==2.2.1,
    plyer==2.1.0,
    Pillow==10.1.0,
    numpy==1.26.4,
    tflite-runtime==2.14.0

# Updated Android configuration
android.archs = arm64-v8a
android.api = 31
android.minapi = 21
android.ndk_path = /home/runner/work/eyediseasedetectionML/eyediseasedetectionML/android-sdk/ndk/25.2.9519653
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

orientation = portrait
log_level = 2
