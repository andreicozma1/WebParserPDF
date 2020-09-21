from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import os
import sys


class WebParserPDF:
    def __init__(self, url, savePath):
        self.url = url
        self.savePath = savePath
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}

        print("WebParserPDF - init")
        print(" - URL:", self.url)
        print(" - Save Path:", self.savePath)
        if not os.path.exists(self.savePath): os.mkdir(self.savePath)

        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")
        for i in soup.select("a[href$='.pdf']"):
            fname = os.path.join(self.savePath, i['href'].split('/')[-1])
            print("Downloading", fname)
            with open(fname, 'wb') as f:
                f.write(requests.get(urljoin(self.url, i['href'])).content)

        print("Done")


if len(sys.argv) == 2:
    URL = sys.argv[1]
    savePath = "downloads"
    WebParserPDF(URL, savePath)
elif len(sys.argv) == 3:
    URL = sys.argv[1]
    savePath = sys.argv[2]
    WebParserPDF(URL, savePath)
else:
    print("Usage: python3 main.py <url> <optional:foldername>")
