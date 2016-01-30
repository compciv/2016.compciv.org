# import os
# import glob
# DATA_DIR = 'tempdata'
# fpath = os.path.join(DATA_DIR, '**', '*')
# filenames = glob.glob(fpath)
# total_linecount = 0
# for fname in filenames:
#     linecount = 0
#     ffile = open(fname, 'r')
#     for line in ffile:
#         if len(line.strip()) > 0:
#             linecount += 1
#             total_linecount += 1
#     ffile.close()
#     print(fname, 'has', linecount, 'non-blank lines')


# print("All together, Shakespeare's", len(filenames), "works have a total of", total_linecount, "non-blank lines")
