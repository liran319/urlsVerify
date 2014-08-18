# -*- coding: utf-8 -*-

import os
import sys
from urlsTools import *

"""__URLFilter:
   筛选文件里面urls是否可用,
   如果无效，在该行url前添加注释;

   copy_urls:
   根据需要将可用的url复制多次并返回一个list对象

   verify2txt:
   更新一个新的文本, 包含所有验证并且注释后的url

   copy2txt:
   更新一个新的文本文件, 包含所有可用url重复多次后的结果
"""
# urlsPath = r"C:\Users\li_ran\Desktop\url"

__all__ = "__URLFilter", "copy_urls", "verify2txt", "copy2txt"
# urlsPath = sys.argv[1]


# def main():
#     file_list = os.listdir(urlsPath)
#     filespath = [os.path.join(urlsPath, i).replace("\\", "/") for i in file_list]
#     for each_file in filespath:
#         if each_file.find("_filted.txt") >= 0 or each_file.find("_copy.txt") >= 0:
#             pass
#         else:
#             print "正在处理: " + each_file
#             handler = UrlsHandler(each_file)
#             handler.verify2txt()
#             # handler.copy2txt()
#             print "该文件处理完毕！"
#     print "太棒啦！所有文件都处理好啦:)"


# if __name__ == '__main__':
#     main()
