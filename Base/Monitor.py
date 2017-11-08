import subprocess
import re


def get_cpu(pkg_name, dev, cpu):
    cmd = "adb -s " + dev + " shell dumpsys cpuinfo | findstr " + pkg_name
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    for info in output:
        if info.split()[1].decode().split("/")[1][:-1] == pkg_name:
            cpu.append(float(info.split()[2].decode().split("%")[0]))
    return cpu


def get_men(pkg_name, dev, men):
    cmd = "adb -s " + dev + " shell dumpsys meminfo " + pkg_name
    output = subprocess.check_output(cmd).split()
    tmp_men = ".".join([x.decode() for x in output])  # 转换为string
    men.append(int(re.findall("TOTAL.(\d+)*", tmp_men, re.S)[0]))
    return men
