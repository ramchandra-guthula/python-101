"""
Sample python web scrapping program using bs4(BeautifulSoup)
Author: Ram Guthula
"""
import requests
from bs4 import BeautifulSoup
import logging


class WebScarp:

    def __init__(self, sample_link):
        self.sample_link = sample_link
        logging.basicConfig(filename='webscrapping_error.log', filemode='w', level=logging.DEBUG)
        self.connect = requests.get(self.sample_link)
        self.soup = BeautifulSoup(self.connect.content, "html.parser")

    def getting_supporting_version(self) -> str:  # type hints https://docs.python.org/3/library/typing.html
        """
        Method to find the supported python version from a python doc page
        :return:
        """
        # print(self.soup.prettify()) # Uncomment this if you want to get the output in proper format 
        # Finding a class and taking output as a text
        grabbing_version_page = self.soup.find("span", class_="versionmodified added").text
        # Converting string output to a list to get the exact text
        splitting_text_to_list = grabbing_version_page.split(" ")
        slicing_list = splitting_text_to_list[3].split('.')[0:2]
        version = slicing_list[0] + "." + slicing_list[1]
        print(f'Supported Python version: {version}')


if __name__ == "__main__":
    try:
        verify = WebScarp('https://docs.python.org/3/library/unittest.mock.html')
        verify.getting_supporting_version()

    except requests.exceptions.ConnectionError as error:
        logging.error(error)


