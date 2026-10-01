#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-

import os, cProfile

def win_tree_test(a='i:/new/database/'):
    b = os.walk(a)
    c = open(a + '1.txt','w')
    for d,e,f in b:
        c.write(str(d))
        c.write('\n')
        c.write(str(e))
        c.write('\n')
        c.write(str(f))
        c.write('\n')
        #print(c,d,e)
            
    c.close()
    
def tree_test():
    p = "/media/karim/2"
    b = os.walk(p)
    a = open("/media/karim/2/New/tree/1.txt",'w')
    for c,d,e in b:
        a.write(str(c))
        a.write('\n')
        a.write(str(d))
        a.write('\n')
        a.write(str(e))
        a.write('\n')
        #print(c,d,e)
            
    a.close()

def tree_test_1(dir="/media/karim/2", print_files=False):
    a = open("/media/karim/2/New/tree/1.txt",'w')   
    cmd = "find '%s'" % dir
    files = os.popen(cmd).read().strip().split('\n')
    padding = '|  '
    for file in files:
        level = file.count(os.sep)
        pieces = file.split(os.sep)
        symbol = {0:'', 1:'/'}[os.path.isdir(file)]
        if not print_files and symbol != '/':
            continue
        print(padding*level + pieces[-1] + symbol)
        a.write(padding*level + pieces[-1] + symbol)
        a.write("\n")
    a.close()

def extract(file):
    l = ['├──','└──']
    b = open("/media/karim/2/New/tree/archives.txt",'a')
    if file.find(l[0]) != -1:        
        path = file[file.find(l[0])+4:]
        cmd = "patool list %s" %path
        files = os.popen(cmd).read().strip().split('\n')
        for d in files:
            b.write(d)
            b.write('\n')
        b.close()
    elif file.find(l[1]) != -1:
        path = file[file.find(l[1])+4:]
        cmd = "patool list %s" %path
        files = os.popen(cmd).read().strip().split('\n')
        for d in files:
            b.write(d)
            b.write('\n')
        b.close()
    
def tree_test_2(print_files=False):
    a = open("/media/karim/2/New/tree/hard_tree.txt",'w')
    cmd = "tree -f /media/karim"
    files = os.popen(cmd).read().strip().split('\n')
    l = ['zip','rar']
    for file in files:
        c = len(file)-1-file[::-1].find('.')
        if file[::-1].find('.') != -1 and file[c+1:]in l:
            extract(file)
##        print(file)
        a.write(file)
        a.write("\n")
    a.close()

##cProfile.run("tree_test_2()")

##def tree(dir, padding, print_files=False):
##    cmd = "find '%s'" % dir
##    files = os.popen(cmd).read().strip().split('\n')
##    padding = '|  '
##    for file in files:
##        level = file.count(os.sep)
##        pieces = file.split(os.sep)
##        symbol = {0:'', 1:'/'}[os.path.isdir(file)]
##        if not print_files and symbol != '/':
##            continue
##        print(padding*level + pieces[-1] + symbol)


## {{{ http://code.activestate.com/recipes/217212/ (r1)
#! /usr/bin/env python

# tree.py
#
# Written by Doug Dahms
#
# Prints the tree structure for the path specified on the command line
##
##from os import listdir, sep
##from os.path import abspath, basename, isdir
##from sys import argv
##
##def tree(dir, padding, print_files=False):
##    print padding[:-1] + '+-' + basename(abspath(dir)) + '/'
##    padding = padding + ' '
##    files = []
##    if print_files:
##        files = listdir(dir)
##    else:
##        files = [x for x in listdir(dir) if isdir(dir + sep + x)]
##    count = 0
##    for file in files:
##        count += 1
##        print padding + '|'
##        path = dir + sep + file
##        if isdir(path):
##            if count == len(files):
##                tree(path, padding + ' ', print_files)
##            else:
##                tree(path, padding + '|', print_files)
##        else:
##            print padding + '+-' + file
##
##def usage():
##    return '''Usage: %s [-f] <PATH>
##Print tree structure of path specified.
##Options:
##-f      Print files as well as directories
##PATH    Path to process''' % basename(argv[0])
##
##def main():
##    if len(argv) == 1:
##        print usage()
##    elif len(argv) == 2:
##        # print just directories
##        path = argv[1]
##        if isdir(path):
##            tree(path, ' ')
##        else:
##            print 'ERROR: \'' + path + '\' is not a directory'
##    elif len(argv) == 3 and argv[1] == '-f':
##        # print directories and files
##        path = argv[2]
##        if isdir(path):
##            tree(path, ' ', True)
##        else:
##            print 'ERROR: \'' + path + '\' is not a directory'
##    else:
##        print usage()
##
##if __name__ == '__main__':
##    main()
#### end of http://code.activestate.com/recipes/217212/ }}}
##
