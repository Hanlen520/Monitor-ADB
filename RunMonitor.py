# -*- coding: utf-8 -*-
import time
import xlsxwriter
from Base import Adb
from Base import Report
from Base import Monitor


# 输出报告
def report(dev, datas):
    run_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    book = xlsxwriter.Workbook('report_' + dev + "_" + run_time + '.xlsx')
    st = book.add_worksheet("详细信息")  # 创建sheet页面
    bs = Report.ManageReport(book, st)
    bs.gen_chart(datas)
    bs.close()
    print("------------报告已生成-----------")


def start_monitor(dev, package_name, second):
    print("-------------开始监控-------------")
    cpu = []
    men = []
    while True:
        Monitor.get_cpu(package_name, dev, cpu)
        Monitor.get_men(package_name, dev, men)
        tmp = 2
        time.sleep(tmp)
        print("倒计时：%d秒" % second)
        second -= tmp
        if second < tmp:
            print("设备" + dev + "监控完成")
            all_data = {'cpu': cpu, 'men': men}
            report(dev, all_data)
            break


if __name__ == '__main__':
    Adb.attached_devices()  # 获取手机设备数量
    devID = '4d986a30'  # 输入设备ID
    setTime = 500  # 输入监控时间（秒）
    pacName = 'com.rongzi.creditmanager'  # 输入监控app名字
    start_monitor(devID, pacName, setTime)
