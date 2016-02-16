def compile_data_files(source_filenames, compiled_filename):
    """
    What it expects:
    ----------------
    `source_filenames` is a list of strings that represent separate
       data text files to be compiled, e.g.

            data/the-counted-2015.csv
            data/the-counted-2016.csv

    `compiled_filename` is a string representing the filename of the
       file to be created.


    What it does:
    -------------
    Creates a new file at the path specified by: `compiled_filename`

    This new file consists of the files in `source_filenames` smushed
    together.

    Even though the data files in this case are CSV-formatted files...
    we don't actually need to use the csv module. We just need to
    combine all the lines of the files into one...and also, not repeat
    the headers.

    What it returns:
    ----------------
    Returns the `compiled_filename` argument, just for the heck of it
    """
    outfile = open(compiled_filename, 'w')
    data_filenames = glob(join(DATA_DIR, "the-counted-*.csv"))
    for file_num, fname in enumerate(data_filenames):
        infile = open(fname, 'r')
        # The first line of each separate data file is
        # the column headers
        print(file_num)
        headers = infile.readline()

        # if we're on the FIRST file to be combined
        # we want to write the headers to the outfile
        if file_num == 0:
            outfile.write(headers)
        else:  # we do nothing, i.e. just pass
            pass
        # at this point, we loop through each line in the file
        # and write it to outfile
        for line in infile:
            outfile.write(line)

        # after we're done reading infile, close it
        infile.close()

    # After we've read each file, we're done with outfile
    # so close it:
    outfile.close()

    return compiled_filename
