import os
import shutil
DATA_DIR = 'tempdata'
ZIP_LOCAL_FILENAME = os.path.join(DATA_DIR, 'matty.shakespeare.tar.gz')

# unzip
shutil.unpack_archive(ZIP_LOCAL_FILENAME, extract_dir=DATA_DIR)
print("Unpacked", ZIP_LOCAL_FILENAME, "into:", DATA_DIR)
