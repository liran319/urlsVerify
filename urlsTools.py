# -*- coding: utf-8 -*-

import os
import urllib2

# url_file = r"C:\Users\li_ran\Desktop\url"


class UrlsHandler(object):

    def __init__(self, arg, times=1):
        self.arg = arg
        self.filter_content = self.__URLFilter()
        self.copy_content = self.copy_urls(times)

    def __URLFilter(self):
        """__URLFilter(), 返回一个更新过的list"""
        file_open = open(self.arg, "r")
        content = file_open.read().split()
        new_contentList = []
        for line in content:
            if line.startswith("http"):  # 判断是否为url
                try:
                    response = urllib2.urlopen(line, timeout=5)
                    redirected = response.geturl()
                    # 判断原始url是否被跳转
                    if int(response.getcode()) == 200 and redirected == line:
                        new_contentList.append(line)
                    else:
                        print line, str(response.getcode())
                        new_contentList.append("# " + line)
                except Exception as e:
                    new_contentList.append("# " + line)
                    print "ErrorInfo: ", line, str(e)
            else:
                new_contentList.append(line)
        file_open.close()
        return new_contentList

    def copy_urls(self, times):
        """copy(times),
        返回一个list, 包含原文本里所有可用的urls的集合的times倍
        """
        vaildURLs = [element for element in self.filter_content if element.startswith("http")]
        return vaildURLs * int(times)

    def verify2txt(self):
        """
        更新一个新的文本, 包含所有验证并且注释后的url
        """
        new_file = os.path.splitext(self.arg)[0] + "_filted.txt"
        file_writer = open(new_file, "w")
        new_content = '\r\n'.join(self.filter_content)
        file_writer.writelines(new_content)
        file_writer.close()

    def copy2txt(self):
        """
        更新一个新的文本文件, 包含所有可用url重复多次后的结果
        """
        new_file = os.path.splitext(self.arg)[0] + "_copy.txt"
        file_writer = open(new_file, "w")
        new_content = '\r\n'.join(self.copy_content)
        file_writer.writelines(new_content)
        file_writer.close()
