#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

mdirname,  filename = os.path.split(os.path.abspath(__file__))

class data:
    data_list = {}
    def __init__(self):
        with open(os.path.join(mdirname, '.environmental'),  'r') as f:
            for line in f.readlines():
                line = line.split('=')
                if (len(line) == 2):
                    self.data_list[line[0]] = str(line[1]).replace('\n', '')
                elif line:
                    continue
                else:
                    print(str(line) + " is Error")

    def add_path(self, key, path):
        self.data_list[key] = path
        self.end_to_data()

    def modify_go_cmd(self, key, path):
        cmdDir={}
        cmdDir[key] = path
        self.end_to_cmd(cmdDir)

    def clear_path(self):
        self.data_list.clear()
        self.end_to_data()

    def has_path(self, key):
        if key in self.data_list:
            return True
        else:
            return False
    def get_path(self, key):
        if key in self.data_list:
            return self.data_list[key]
        else:
            return None

    def delete_path(self, key):
        result = False
        if self.data_list.has_key(key):
            del self.data_list[key]
            self.end_to_data()
            result = True
        return result

    def list_path(self):
        pathList = []
        with open(os.path.join(mdirname,  '.environmental'),  'r') as f:
            for path in f.readlines():
                pathList.append(path.replace('\n',''))
        return pathList

    def end_to_data(self):
        with open(os.path.join(mdirname,  '.environmental'),  'w+') as f:
            f.truncate()
            for k, v in self.data_list.viewitems():
                f.writelines(k + '=' + v + '\n')

    def end_to_cmd(self, cmdDir):
        with open(os.path.join(mdirname,  '.cmd'),  'w+') as f:
            f.truncate()
            for k, v in cmdDir.viewitems():
                f.writelines(k + '=' + v + '\n')

if __name__ == "__main__":
    data = data()
    data.add_path("imwcc", "aa");
    data.add_path("kk", "aa");
    data.add_path("gg", "aa");
    data.add_path("ww", "aa");
    data.list_path();
    print("======= clear =======")
    data.clear_path()
    data.list_path()