import re
from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen
import requests


# How to create a class in python
class Extractor:
    # A class can have one more more methods
    # A method is a function inside a class
    # Fuction is a block of related code
    def find(self, *, url, section, value):
        """Find takes three arguments (url, section,value)
        and returns a list of elements found
        """
        page = requests.get(url)
        bs = Soup(page.content, "html.parser")
        l = bs.find_all(
            section,
            attrs={
                "class": value,
            },
        )
        return l
