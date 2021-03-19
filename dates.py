#!/usr/bin/python
import calendar
import datetime
def calRow():
        month = datetime.date.today().month
        year = datetime.date.today().year
        days = list(calendar.Calendar().itermonthdays(year,month))
        return days

def add_zeros(iterator):
    return_list = list()
    for i in iterator:
        if len(i) == 1:
            return_list.append('0' + i)
        else:
            return_list.append(i)
    return return_list
print('<openbox_pipe_menu>')
days = calRow()
print('<item label="Date: {}"/>'.format(datetime.date.today()))
print('<seperator/>')
print('<item label="{}"/>'.format('\t'.join(['Days  ','Mon' , 'Tue','Wed','Thu','Fri'])))
for i in range(len(days)//7):
    day_list = add_zeros(map(str,days[i*7:(i+1)*7]))
    print('<item label="Week {} {}"/>'.format(i,'\t'.join(day_list)))
print('</openbox_pipe_menu>')
