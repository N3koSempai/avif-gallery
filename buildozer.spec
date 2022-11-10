[app]

title = Test App
package.name = testapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,avif

version = 0.1
requirements = python3,Kivy==2.1.0,Kivy-Garden==0.1.5,kivymd==1.1.1,Pillow==9.2.0,pillow-avif-plugin==1.3.1,avif==0.5.0

orientation = portrait
fullscreen = 0
android.archs = armeabi-v7a

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

[buildozer]
log_level = 1
