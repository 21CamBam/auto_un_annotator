import subprocess
import urllib.request
import wget

def get_directory_listing(path, url):
    p = subprocess.Popen(['lftp', '{0}{1}'.format(url,path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    out, _ = p.communicate(b'ls')
    return out.decode('utf-8').split('\n')

def get_file(path, url):
    return urllib.request.urlopen(url + path).read().decode('utf-8')

def download_file(path, url, filename):
    if filename:
        filename = wget.download(url=url + path, out=filename)
    else:
        filename = wget.download(url=url + path)
    return filename

def get_test_urls(comments):
    return []