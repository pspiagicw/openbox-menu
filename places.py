#!/usr/bin/python
import os
import sys
args = sys.argv[1:]
start = False
dir_path = None
file_manager = 'pcmanfm'
if args:
    dir_path = ' '.join(args)
else:
    start = True
    dir_path = '~'

list_of_dir = os.listdir(os.path.expanduser(dir_path))
dirs = list()
for file in list_of_dir:
    if os.path.isdir(os.path.join(os.path.expanduser(dir_path),file)):
        if not file.startswith('.'):
            dirs.append(file)

print('<openbox_pipe_menu>')


print('<item label="Go To {}">'.format(os.path.expanduser(dir_path)))
print('<action name="Execute"><command>')
print('{file_manager} {path}'.format(file_manager=file_manager,path=os.path.expanduser(dir_path)))
print('</command></action>')
print('</item>')
for dir_name in dirs:
    print('<menu id="{menu_id}" label="{dir_name}" execute="{menu_command}"/>'.format(menu_id=dir_name,dir_name=dir_name,menu_command="~/Code/openbox-menu/places.py " + os.path.expanduser(os.path.join(dir_path,dir_name))))

print('</openbox_pipe_menu>')

