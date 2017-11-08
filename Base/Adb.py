import os


# 获取手机设备数量
def attached_devices():
    rt = os.popen('adb devices').readlines()
    n = len(rt) - 2
    print("当前已连接手机数量为：" + str(n))



