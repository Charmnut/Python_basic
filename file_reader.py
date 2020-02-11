#!/usr/bin/env python 
# -*- coding:utf-8 -*-

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('pi_digits.txt', 'a') as file_object:
    file_object.write("I love programing")