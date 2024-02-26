def validurl(url):

    if url.startswith("http://") or url.startswith("https://"):
        if "." in url:
            return True
    return False