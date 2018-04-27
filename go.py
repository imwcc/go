#!/usr/bin/python
# -*- coding: UTF-8 -*-
import getopt
import sys
import shelve

data = shelve.open("path.db")

def showDataBase():
    for k, v in data.iteritems():
        print k, v

def usage():
    print("usage")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:ld:", ["add=", "list", "delete="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for option, value in opts:
        if option == "-a":
            #-a 表示添加路径， go -a gordon /home/arvin/source_code/gordon_peak
            if len(args) == 1:
                print value, args[0]
                data[value] = args[0] #-a 后面的值为key
            else:
                break

        elif option in ("-l", "--list"):
            showDataBase()
            break
        elif option in ("-d", "--delete"):
            if value == "all":
                sys.stdout.write("Dlete all of the data ? [Y OR N]: ")
                result = sys.stdin.readline().split()[0]
                if result in ('yes','y','YES','Y'):
                    print("begin delete the below data" + '\n' +'\n')
                    showDataBase()
                    data.clear()
                    break
                else:
                    print('cancel delte')
                    break
            if data.has_key(value):
                del data[value]
            else:
                print("value is not exist: " + value)
        else:
            assert False, "unhandled option"
    data.close()

if __name__ == "__main__":
    main()
