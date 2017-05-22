#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import sys
import os

try:
    path = sys.argv[1]
except Exception as e:
    print("Input your filename please. eg: python check_protobuf.py test.proto")
    path = raw_input('please input your path:  ')
    # exit("Input your filename please. eg:  python check_protobuf.py test.proto")

if os.path.exists(path) is False:
    exit("The path is not exist.")
message = []
repeat = []
used = []
i = 0
for line in open(path):
    i = i + 1
    list_option = line.lstrip().split(' ')
    if list_option[0] in ['message', 'enum']:
        name_list = line.split('{')[0].split(' ')[1]
        if name_list.strip() in message:
            repeat.append(name_list.strip())
        message.append(name_list.strip())
    elif list_option[0] in ['optional', 'repeated', 'required'] and (list_option[1].lower() not in ['int32', 'string', 'float']):
        used.append(list_option[1])
    else:
        continue
print ("Repeat item:")
print (repeat)
message = sorted(message)
print ("Total:" + len(message).__str__())
print ("Total after remove repeat items:" + len(set(message)).__str__())
print ("Used but not defined:" + list(set(used).difference(set(message))).__str__())
#print [val for val in used if val in message]
