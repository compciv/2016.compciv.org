from utils.settings import ORIGINAL_DATA_DIR, GEODATA_DIR
from utils.settings import COMPILED_FILENAME, WRANGLED_FILENAME
from utils.moar_utils.compiling import compile_data_files
from utils.moar_utils.embiggening import embiggen_teh_data
from glob import glob
from os.path import join

def wrangle():
    """
    Whatsup
    """

    filenames = gather_data_files()
    print("Compiling files into:", COMPILED_FILENAME)
    compile_data_files(filenames, COMPILED_FILENAME)

    print("Attempting to embiggen our data with geocoding")
    embiggen_teh_data(src=COMPILED_FILENAME,
                      dest=WRANGLED_FILENAME,
                      geodata_dir=GEODATA_DIR)

    print("Created", WRANGLED_FILENAME)



def gather_data_files():
    fpath = join(ORIGINAL_DATA_DIR, '*.csv')
    return glob(fpath)
