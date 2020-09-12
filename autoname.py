#!/usr/bin/python
# -*- coding: utf-8 -*-
# 解压icon包,自动转到.2x 3x文件夹中

import os
import zipfile
import shutil
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def move(path, filename, index):
    file_extension = os.path.splitext(filename)[-1][1:]
    #移动icon到目标路径
    newpath = "2020年8月8日+沙二·食安+流动宣传("+ str(index) +")." + file_extension
    print(newpath)
    shutil.move(path + filename, path + newpath)
    
while(1):
    outpath = raw_input('请拖入数据目录:')
    outpath = outpath.rstrip()
    sender = 1
    if os.path.isdir(outpath):
        for parent,dirnames,filenames in os.walk(outpath):
            for val in filenames:
                print(val)
                move(parent+"/", val, sender)
                sender += 1