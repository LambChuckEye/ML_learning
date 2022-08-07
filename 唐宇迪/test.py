#!/usr/bin/env python3
import sys
words = []
# 获取输入并切词
for i in sys.stdin:
    i = i.strip()
    words.append(i)
# 输出
for i in words:
    print(i, ",", 1)
