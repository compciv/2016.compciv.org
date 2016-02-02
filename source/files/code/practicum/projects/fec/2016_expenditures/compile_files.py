from os.path import join
DATA_DIR = 'tempdata'
YEAR_NAME = '16'
YEAR_DATA_DIR = join(DATA_DIR, YEAR_NAME)


DATA_STUBNAMES = ['cm', 'cn', 'ccl', 'oppexp']
for _n in DATA_STUBNAMES:
    header_fname = join(YEAR_DATA_DIR, _n + '_header_file.csv')
    data_fname = join(YEAR_DATA_DIR, _n + '.txt' )
    compiled_fname = join(YEAR_DATA_DIR, "compiled_" + _n + '.txt')

    hf = open(header_fname, 'r', encoding='latin-1')
    df = open(data_fname, 'r', encoding='latin-1')

    with open(compiled_fname, 'w') as f:
        # read the contents of the header file (i.e. the single line)
        # and replace all commas with pipes
        pipeheadertxt = hf.read().replace(',', '|')
        #
        f.write(pipeheadertxt)
        f.write(df.read())
    hf.close()
    df.close()




