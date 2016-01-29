import webbrowser
def extract_image_urls(the_dict):
    urls = []
    for item in mydict['data']:
        url = item['images']['standard_resolution']['url']
        webbrowser.open(url)



