#!/usr/bin/env python

import sys
wordList = dict()
file_object = open('test-algo.txt')
for line in file_object:
    line = line.strip()
    words = line.split(',')


    print(words[1],words[4],1)