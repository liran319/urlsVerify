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


__all__ = "__URLFilter", "copy_urls", "verify2txt", "copy2txt"
