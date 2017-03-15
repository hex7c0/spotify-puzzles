#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

'''
Task
Your task will be to write a program for reversing numbers in binary. For instance, the binary representation of 13 is 1101, and reversing it gives 1011, which corresponds to number 11.

Input
The input contains a single line with an integer N, 1 ≤ N ≤ 1000000000.

Output
Output one line with one integer, the number we get by reversing the binary representation of N.

Sample input 1
13
Sample output 1
11
Sample input 2
47
Sample output 2
61
'''

str_input = raw_input() # input from stdin
int_input = int(str_input) # convert int from str
str_bin = bin(int_input)[2:] # remove binary rappr
str_bin_reverse = str_bin[::-1] # str reverse
print int(str_bin_reverse, 2) # print to output
