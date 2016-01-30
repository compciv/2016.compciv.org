from os.path import join
from glob import glob
tragic_path = join('tempdata', 'tragedies', '*')
tragic_filenames = glob(tragic_path)

for fname in tragic_filenames:
    # open the file to count the lines
    txtfile = open(fname, 'r')
    mylist = txtfile.readlines()
    txtfile.close()
    total_lines = len(mylist)
    # print out the filename this one time, with the line count
    print(fname, "has", total_lines, "lines")
    # calculate the line from which to start printing text
    starting_line_num = total_lines - 5
    for line_num in range(starting_line_num, total_lines):
        line = mylist[line_num]
        proper_line = str(line_num + 1) + ": " + line.strip()
        print(proper_line)
