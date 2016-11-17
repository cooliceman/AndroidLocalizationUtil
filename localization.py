#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, getopt
import openpyxl

from lxml import etree


def load_xml(path):
    # 创建清除空字符的Parser,否则pretty_print不起作用.
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(path, parser)
    return tree


def exist(tree, key):
    return tree.find("string[@name='%s']" % key) is not None


def main(argv):
    input_file = ''
    dest_folder = ''
    force_update = False
    try:
        opts, args = getopt.getopt(argv, "hvfi:d:", ["file=", "dir=", "version", "force"])
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
        elif opt in ("-d", "--dir"):
            dest_folder = arg
        elif opt in ("-f", "--force"):
            force_update = True
    print 'Input file:', input_file
    print 'Destination directory:', dest_folder
    localize(input_file, dest_folder, force_update)


def usage():
    print 'localization.py -i <excel file> -d <destination directory>'


def version():
    print "version:1.0.0"


def localize(input_file, dest_dir, force_update):
    # 打开多语言翻译excel文件
    wb = openpyxl.load_workbook(input_file)
    # 获取默认Sheet
    ws = wb.active
    # 获取字符串资源文件列表
    file_list = find_string_resource_files(dest_dir)
    # 遍历Excel每个语言数据行
    for col in range(3, ws.max_column + 1):
        # 提取语言码
        lang_code = ws.cell(row=1, column=col).value
        print "\n%s" % lang_code
        # 获取对应语言的资源文件
        lang_string_file = find_string_resource_file_of(file_list, lang_code)
        if not lang_string_file:
            continue
        string_map = load_xml(lang_string_file)
        for r in range(4, ws.max_row):
            key = ws.cell(row=r, column=1).value
            value = ws.cell(row=r, column=col).value
            print key, lang_code, value
            if not key:
                print "no key exist at:%d,%d" % (r, col)
                break
            if not value:
                print "no value found, skip"
                continue
            if exist(string_map, key):
                if force_update:
                    print "Key already exist, update"
                    string_map.find("string[@name='%s']" % key).text = value
                    continue
                else:
                    print "Warning:%s already exist, skip" % key
                    continue
            # 新建字符结点
            localize_element = etree.Element('string', name=key)
            localize_element.text = value
            # 追加结点
            string_map.getroot().append(localize_element)
        string_map.write(lang_string_file, xml_declaration=True, encoding='UTF-8', pretty_print=True)


def find_string_resource_files(folder):
    """

    遍历目录获取所有语言的string.xml文件
    """
    file_list = []
    for root, dirs, files in os.walk(os.path.abspath(folder)):
        for d in dirs:

            find_string_resource_files(d)
            if "res" == d:
                break

        for f in files:
            if f == "strings.xml":
                file_list.append(os.path.join(root, f))
    return file_list


def find_string_resource_file_of(file_list, language_code):
    """find_string_resource_file_of(file_list, language_code)

    通过语言码来找到对应的string.xml文件路径
    """
    for f in file_list:
        if language_code in f:
            return f


if __name__ == "__main__":
    main(sys.argv[1:])
