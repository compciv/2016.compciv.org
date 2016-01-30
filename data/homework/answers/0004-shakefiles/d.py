import os
DATA_DIR = 'tempdata'
HAMLET_FILENAME = os.path.join(DATA_DIR, 'tragedies', 'hamlet')
f = open(HAMLET_FILENAME, 'r')
print(f.readline().strip())
print(f.readline().strip())
print(f.readline().strip())
print(f.readline().strip())
print(f.readline().strip())
f.close()


# alternatively
# import os
# fname = os.path.join('tempdata', 'tragedies', 'hamlet')
# hamletfile = open(fname, 'r')
# for x in range(5):
#     print(hamletfile.readline().strip())
# hamletfile.close()
