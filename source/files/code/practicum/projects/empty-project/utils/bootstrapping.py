def bootstrap():
    """
    What it expects:
    ----------------

    What it does:
    -------------

    What it returns:
    ----------------
    """



def set_things_up():
    """
    What it expects:
    ----------------
    Nothing

    What it does:
    -------------
    Creates the utils.settings.DATA_DIR

    What it returns:
    ----------------
    Nothing
    """
    os.makedirs(DATA_DIR, exist_ok=True)
