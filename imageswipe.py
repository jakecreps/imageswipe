import urllib.request
import csv

def download():
    f = open("imagelinks.csv")
    csv_f = csv.reader(f)
    for links in csv_f:
        links = "".join(links)
        remove = links.replace("http://www.", "")
        filename = remove.replace("/", "_")
        urllib.request.urlretrieve(links, filename)
download()
