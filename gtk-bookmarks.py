#!/bin/python
import os


filemanager = 'pcmanfm'

lines = None
with open(os.path.expanduser('~/.gtk-bookmarks')) as bookmarks:
    lines = bookmarks.readlines()
    
print('<openbox_pipe_menu>')
for line in lines:
    line = line[7:-1]
    print('<item label="{}">'.format(line))
    print('<action name="Execute"><execute>')
    print('{filemanager} {bookmark}'.format(filemanager=filemanager,bookmark=line))
    print('</execute></action>')
    print('</item>')
print('</openbox_pipe_menu>')

