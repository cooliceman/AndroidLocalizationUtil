#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, getopt
from bs4 import BeautifulSoup


def load_xml(path):
    # 创建清除空字符的Parser,否则pretty_print不起作用.

    # parser = etree.XMLParser(remove_blank_text=True)
    # tree = etree.parse(path, parser)
    # return tree
    bs = BeautifulSoup(open(path), "lxml")
    return bs


def exist(tree, key):
    return tree.find("string", name="%s" % key) is not None


def export(input_file):
    string_map = load_xml(input_file)
    result = ""
    for element in string_map.findAll("string"):
        result += element.get("name")+", "

    print result


def main(argv):
    input_file = ''
    try:
        opts, args = getopt.getopt(argv, "hvi:", ["file=", "version"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-v", "--version"):
            version()
            sys.exit()
        elif opt in ("-i", "--file"):
            input_file = arg
    print 'Input file:', input_file
    export(input_file)


def usage():
    print 'export_key.py -i <string file>'


def version():
    print "version:1.0.0"


if __name__ == "__main__":
    main(sys.argv[1:])

