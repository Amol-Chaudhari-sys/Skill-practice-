import pyshorteners 


def short():
    url = "https://youtu.be/xQbHQE0HZVQ?si=ypvReGte0MpzQ3C8"
    
    print( pyshorteners.Shortener().tinyurl.short(url))
short()