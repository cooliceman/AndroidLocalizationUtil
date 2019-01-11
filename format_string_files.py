#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, getopt, shutil


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
    format_file(input_file)


def format_file(input_file):
    """
    将文件整理成符合Android工程语言目录结构样式

    :param input_file:待处理数据所在目录
    :return:
    """
    for root, folder_names, file_names in os.walk(input_file):
        for file_name in file_names:
            if file_name.endswith("_strings.xml"):
                # 获取语言前缀
                prefix = file_name.split("_s")[0]
                prefix = correct_language_code(prefix)
                print root, file_name, prefix
                new_dir = root + "/values-" + prefix
                # 创建values目录
                if not os.path.exists(new_dir):
                    os.mkdir(new_dir)
                new_file_path = new_dir + "/" + file_name
                # 移动字符文件
                shutil.move(root + "/" + file_name, new_file_path)
                # 切换目录
                os.chdir(new_dir)
                # 重命名文件
                os.rename(file_name, "strings.xml")
                # 切回上一级目录
                os.chdir("../")


def usage():
        print 'format_string_files.py -i <string file>'


def version():
    print "version:1.0.0"


def correct_language_code(code):
    """
    校正不规范语言码格式
    :param code: 从文件名中获取到的语言码
    :return: 符合Android规范的语言码
    """
    parts = code.split("_")
    if len(parts) < 2:
        return code

    parts[1] = parts[1].upper()
    return parts[0] + "-r" + parts[1]


if __name__ == "__main__":
    main(sys.argv[1:])
