import re

read_list = []
with open('inputs.txt','r') as f:
    for line in f:
        if '@' in line:
            read_list.append(line)

new_read_list = []
result_list = []

for element in read_list:
    line_str = str(element)
    new_read_list = line_str.split(' ')
    for line in new_read_list:
        if '@' in line:
            result_list.append(line.rstrip())


with open('outputs.txt','w') as f:
    for element in result_list:
        f.write(element + '\n')

