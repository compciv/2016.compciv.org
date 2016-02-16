from os.path import join

# directories
DATA_DIR = 'data'
ORIGINAL_DATA_DIR = join(DATA_DIR, 'original')
GEODATA_DIR = join(DATA_DIR, 'geo')

# various data files
ZIPPED_DATA_FILENAME = join(ORIGINAL_DATA_DIR, 'thecounted-data.zip')
COMPILED_FILENAME = join(DATA_DIR, 'compiled-data.csv')
WRANGLED_FILENAME = join(DATA_DIR, 'geocoded-data.csv')

# other useful files
GEOCODER_CREDENTIALS_FILENAME = 'creds_mapzen.txt'
