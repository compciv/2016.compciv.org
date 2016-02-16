import requests
from os import makedirs
from shutil import unpack_archive
from utils.settings import ZIPPED_DATA_FILENAME
from utils.settings import ORIGINAL_DATA_DIR, GEODATA_DIR
SRC_URL = "https://interactive.guim.co.uk/2015/the-counted/thecounted-data.zip"


def bootstrap():
    """
    Set up the file folders and fetch the data

    What it expects:
    ----------------
    Nothing

    What it does:
    -------------
    Calls setup_directories() to create ORIGINAL_DATA_DIR and GEO_DATA_DIR
    Calls fetch_data() to get the data and unpack it

    What it returns:
    ----------------
    Nothing
    """
    setup_directories()
    fetch_data()


def fetch_data():
    """
    What it expects:
    ----------------
    That the DATA_DIR has been created

    What it does:
    -------------
    Downloads the zip file from the Guardian
    Saves it to DATA_DIR
    Unzips it into DATA_DIR

    What it returns:
    ----------------
    Nothing
    """

    resp = requests.get(SRC_URL)
    print("Downloading", SRC_URL)
    # save the zip file to disk
    with open(ZIPPED_DATA_FILENAME, 'wb') as f:
        f.write(resp.content)
    # unzip the zip file
    print("Unzipping", ZIPPED_DATA_FILENAME)
    unpack_archive(ZIPPED_DATA_FILENAME, extract_dir=DATA_DIR)

2

def setup_directories():
    print("Creating directory:", ORIGINAL_DATA_DIR)
    os.makedirs(ORIGINAL_DATA_DIR, exist_ok=True)
    print("Creating directory:", GEO_DATA_DIR)
    os.makedirs(GEO_DATA_DIR, exist_ok=True)
