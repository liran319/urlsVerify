#/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
from urlsTools import *

urlsPath = sys.argv[1]


def main():
    file_list = os.listdir(urlsPath)
    filespath = [os.path.join(urlsPath, i).replace("\\", "/") for i in file_list]
    for each_file in filespath:
        if each_file.find("_filted.txt") >= 0 or each_file.find("_copy.txt") >= 0:
            pass
        else:
            print "正在处理: " + each_file
            handler = UrlsHandler(each_file)
            """下面一行调用函数来生成验证过的文件，可注释来取消"""
            handler.verify2txt()
            """下面一行调用函数来生成重复多次有效url的文件，可注释来取消"""
            # handler.copy2txt()
            print "该文件处理完毕！"
    print "太棒啦！所有文件都处理好啦:)"


if __name__ == '__main__':
    main()
