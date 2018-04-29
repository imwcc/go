#!/usr/bin/python
# -*- coding: UTF-8 -*-
import getopt
import sys
import os
import logging
from data import data

# 程序返回说明：
# 0  程序执行成功，直接跳转到go 参数路径
# 1  程序直接讲参数传递给 cd 命令
# 2  程序执行成功，但是不传递任何参数给 cd 命令
# -1 程序执行失败

dirname, filename = os.path.split(os.path.abspath(__file__))

def usage():
    print("usage")

def is_cd_defalut_arg(arg):
    if arg == '-':
        return True
    else:
        return False


def is_dir(path):
    if os.path.isdir(path):
        return True
    else:
        return False

def main():
    mdata = data()

    if(len(sys.argv) == 1):#不带参数，直接去home目录
        # print("dircrt return due to only one argv: "+ str(sys.argv))
        exit(1)
    if is_cd_defalut_arg(sys.argv[1]):#key是默认参数，直接跳转
        exit(1)
    elif is_dir(sys.argv[1]): #key是一个目录，直接跳转
        exit(1)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:ld:", ["add=", "list", "delete="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(-1)
    if (len(opts) == 0):#没有option，后面只能添加key or 跳转到指定目录
        if len(args) == 1: #一个参数就尝试跳转
            if mdata.has_path(args[0]):
                print('cd ' + mdata.get_path(args[0]))
                exit(0) #有该路径，直接跳转
            else:
                print("This key %s is invaild" %(args))
                os._exit(-1)
        elif len(args) == 2:
            if(os.path.isdir(args[1]) or os.path.isfile(args[1]) or args[1] == '.'):
                if args[1] == '.':
                    args[1] = os.getcwd()
                print(args[0], args[1])
                mdata.add_path(args[0], args[1])
            else:
                print("This is not a vaild path: %s" %(args[1]))
                exit(-1)

    for option, value in opts:
        if option == "-a":
            print(opts,args)
            #-a 表示添加路径， go -a gordon /home/arvin/source_code/gordon_peak
            if len(opts) == 1 and len(args) == 1:
                if (os.path.isdir(args[0]) or os.path.isfile(args[0]) or args[0] == '.'):
                    if args[0] == '.':
                        args[0] = os.getcwd()
                    mdata.add_path(value, args[0])
                    break
                else:
                    print("Path %s is not a vaild path:" % (args))
                    exit(-1)
                    break

        elif option in ("-l", "--list"):
            mdata.list_path()
            break
        elif option in ("-d", "--delete"):
            if value == "all":
                sys.stdout.write("Dlete all of the mdata ? [Y OR N]: ")
                result = sys.stdin.readline().split()[0]
                if result in ('yes','y','YES','Y'):
                    print("begin delete the below mdata" + '\n' +'\n')
                    mdata.clear_path()
                    break
                else:
                    print('cancel delte')
                    break
            if mdata.has_path(value):
                mdata.delete_path(value)
                print('success')
                exit(2)
            else:
                print("value is not exist: " + value)
                exit(-1)
        else:
            assert False, "unhandled option"

if __name__ == "__main__":
    main()
    exit(2)
