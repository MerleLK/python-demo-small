"""
@description: you can load the text file content to the excel file.
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-7-20
"""
import json


# read the text file to json
def read_text_to_json(filename):
    with open(filename, 'r') as text_file:
        l = []
        # l = [text_file.readlines()]
        _sad = text_file.readline()
        for line in text_file.readlines():
            print(line, end='')
            # print('{' in line)
            print(line.split(':'))
            s1 = line.split(':')
            print(s1[0])
            # print(s1[1])
            if len(''.join(line.split('\n'))) > 2:
                pass
        print(l)


# 将json字符串拆分写入excel
def write_to_excel(json_data):
    pass

if __name__ == '__main__':
    file_name = 'student.txt'
    read_text_to_json(file_name)
    pass
