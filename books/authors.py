# coding: utf-8

import re

rfile = 'leveledbooks_refguide.csv'


def file_to_obj(readfile, obj):
    r = open(rfile, "r")
    pat = re.compile(ur'(\s{2,})', re.DOTALL)
    # keys = re.sub(pat, r.readline()).split(';')
    kwargs_list = []
    kwargs = {}
    keys = ['Title', 'Genre', 'Comprehension Skill', 'Description']
    for line in r.read().split('\r'):
        args = re.sub(pat, ' ', line).split(';')
        if len(args) == 4:
            for key, arg in zip(keys, args):
                kwargs[key] = arg
            kwargs_list.append(obj(**kwargs))
    print kwargs_list
    r.close()

print file_to_obj(rfile, Book())

# for line in r.readlines():
# help(str.find)