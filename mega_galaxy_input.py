import sys
import shutil
import os

def check_data_format(fn):
    f = open(fn,'r')
    l = f.readline()
    if l[0:5] == '#mega':
        return 'meg'
    if l[0] == '>':
        return 'fasta'
    if l[0] == '(':
        return 'nwk'

data_name = str(sys.argv[1])
data_mod_name = 'mega_data.'+check_data_format(data_name)
os.symlink(data_name,data_mod_name)
if len(sys.argv) == 3:
    tree_name = str(sys.argv[2])
    tree_mod_name = 'mega_tree.nwk'
    os.symlink(tree_name,tree_mod_name)
lf = open('mega_data.txt','w')
lf.write(data_mod_name+'\n')

