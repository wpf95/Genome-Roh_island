# _*_ coding: utf-8 _*_
"""
Created on 2023/7/26 11:33

@author: Wangpf

@Email: 206462763@qq.com
"""
import sys

fo = open(sys.argv[1], 'r')
def build_pos(chr):
    if chrom == str(chr):
        for i in range(int(pos1), int(pos2) + 1):
            print(str(chr) + "\t" + str(i))

for line in fo:
    if 'FID' in line:
        pass
    else:
        line = line.strip().split()
        chrom = line[3]
        pos1 = line[6]
        pos2 = line[7]
        for i in range(1,30):
            build_pos(i)
