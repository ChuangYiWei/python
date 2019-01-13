# coding=UTF-8

__author__ = 'Chuang Yi, Wei'
import os
import sys

import datetime
import subprocess


cmd_7z="7z a "
space = " "
PATH_7Z = "C:\\Program Files\\7-Zip"

def check_7z_path(path):
    if(False == os.path.isdir(path)):
        print("%s not exist" % path)
        print("please install 7z !")
    else:
        print("%s exist" % path)

def Get_time():
    now = datetime.datetime.now()
    return now.strftime("%Y_%m_%d_%H_%M")

def compress_file(path):
    file_name = path.split('\\')
    file_full_name = Get_time() + "_" + file_name[-1]
    cmd = cmd_7z + file_full_name + space + path + "\\*"
    print("exe cmd: %s" % cmd)
    subprocess.call(cmd)

def pause():
    programPause = input("Press the <ENTER> key to continue...")


def main():
    check_7z_path(PATH_7Z)
    compress_path=input("please input comperss path:")
    # compress_path=os.getcwd()
    print("compess path is : %s" % compress_path)
    compress_file(compress_path)

main()
pause()