[app]
title = MyCGC Monitor
package.name = mycgc
package.domain = org.dahai.mycgc
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf,otf
version = 1.0

requirements = python3==3.11.9,hostpython3==3.11.9,kivy==2.3.0,pyjnius,requests,certifi

orientation = portrait
fullscreen = 0

# 息屏也要能持续跑：需要 FOREGROUND_SERVICE + WAKE_LOCK
# 通知：POST_NOTIFICATIONS（Android 13+ 需要动态申请）
# RECEIVE_BOOT_COMPLETED 预留给以后做"开机自启"用
android.permissions = INTERNET,FOREGROUND_SERVICE,WAKE_LOCK,POST_NOTIFICATIONS,RECEIVE_BOOT_COMPLETED

android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.enable_androidx = True
android.archs = arm64-v8a

# 后台前台服务：对应 service/main.py，类名会是 Service + Monitor.capitalize() = ServiceMonitor
# :foreground -> p4a 会在 onStartCommand 里自动、同步地调用 startForeground()，
#                不依赖 Python 解释器启动完成后再手动调用（后者容易超过系统给的5秒时限被杀）
# :sticky     -> 让 Service 返回 START_STICKY：
#                a) 被系统内存回收后能自动重启
#                b) 用户把App从"最近任务"里划掉时不会被 onTaskRemoved() 直接 stopSelf()
services = monitor:service/main.py:foreground:sticky

[buildozer]
log_level = 2
warn_on_root = 1
