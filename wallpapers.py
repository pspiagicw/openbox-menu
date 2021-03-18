#!/usr/bin/python
import os

directory = '~/Pictures/Wallpapers'

wallpaper_command = 'nitrogen --set-zoom-fill'

print('<openbox_pipe_menu>')
for file in os.listdir(os.path.expanduser(directory)):
    filename = os.path.join(directory,file)
    print('<item label="{}">'.format(file))
    print('<action name="Execute"><execute>')
    print('{wallpaper_command} {filename}'.format(wallpaper_command=wallpaper_command,filename=filename))
    print('</execute></action>')
    print('</item>')
print('</openbox_pipe_menu>')
