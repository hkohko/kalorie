from html.parser import HTMLParser

from bs4 import BeautifulSoup
from constants import DATADUMP_DIR, PAGES_DIR


class Source1Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            print(tag)
            self.write_file("\n")
        if tag == "td":
            print(tag)
            self.write_file(",")

    def handle_data(self, data):
        if data.strip() == "" or data is None:
            return None
        print(data)
        self.write_file(data)

    def write_file(self, data):
        with open(DATADUMP_DIR.joinpath("data.txt"), "a") as file:
            file.write(data)


def simplify_page_source1():
    with open(PAGES_DIR.joinpath("SOURCE1.html")) as file:
        read = file.read()
    soup = BeautifulSoup(read, "lxml")
    table = soup.find("table")
    print(table)
    with open(PAGES_DIR.joinpath("SOURCE1_TABLE.html"), "w") as file:
        file.write(str(table))


def parse_source1_data():
    parser = Source1Parser()
    with open(PAGES_DIR.joinpath("SOURCE1_TABLE.html")) as file:
        read = file.read()
    result = parser.feed(read)
    print(result)


if __name__ == "__main__":
    parse_source1_data()
