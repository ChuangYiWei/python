# coding=UTF-8

__author__ = 'Chuang Yi, Wei'
import os
import sys

import datetime
import subprocess
print("current encoding : %s " % sys.stdout.encoding)
print ("current dir: %s" % (os.getcwd()))

cmd_7z="7z a "
space = " "
def Get_time():
    now = datetime.datetime.now()
    return now.strftime("%Y_%m_%d_%H_%M")
print ("Current date and time using strftime: %s" % Get_time())

def compress_file(path):
    file_name = path.split('\\')
    file_full_name = Get_time() + "_" + file_name[-1]
    cmd = cmd_7z + file_full_name + space + path + "\\*"
    print("exe cmd: %s" % cmd)
    subprocess.call(cmd)

def pause():
    programPause = input("Press the <ENTER> key to continue...")


def main():
    compress_path=input("please input comperss path:")
    # compress_path=os.getcwd()
    print(compress_path)
    compress_file(compress_path)



main()
pause()