from os.path import join
from glob import glob

def single_file_reading_routine(fname):
    txtfile = open(fname, 'r')
    total_line_count = 0
    nonblank_line_count = 0
    for line in txtfile:
        total_line_count += 1
        if line.strip() is not "":
            nonblank_line_count += 1
    txtfile.close()
    print(fname, 'has', nonblank_line_count,
          'non-blank lines out of', total_line_count, 'total lines')
    return [nonblank_line_count, total_line_count]

## Main routine
all_line_count = 0
all_nonblank_line_count = 0
filepattern = join('tempdata', '**', '*')
filenames = glob(filepattern)
for fname in filenames:
    line_counts = single_file_reading_routine(fname)
    all_nonblank_line_count += line_counts[0]
    all_line_count += line_counts[1]

print("All together, Shakespeare's",
      len(filenames), "text files have:")
print(all_nonblank_line_count,
      "non-blank lines out of",
      all_line_count, "total lines")
