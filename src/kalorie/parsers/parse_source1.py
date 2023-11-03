from html.parser import HTMLParser

from bs4 import BeautifulSoup

from kalorie.constants import DATADUMP_DIR, PAGES_DIR


class Source1Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.write_file("\n")
        if tag == "td":
            self.write_file(",")

    def handle_data(self, data):
        if data.strip() == "" or data is None:
            return None
        self.write_file(data)

    def write_file(self, data):
        with open(DATADUMP_DIR.joinpath("data_source1.txt"), "a") as file:
            file.write(data)


def simplify_page_source1():
    with open(PAGES_DIR.joinpath("SOURCE1.html")) as file:
        read = file.read()
    soup = BeautifulSoup(read, "lxml")
    table = soup.find("table")
    tbody = table.find("tbody")
    trs = tbody.find_all("tr")
    trs_list = [str(tr) for tr in trs if tr.get("class") is None]

    with open(PAGES_DIR.joinpath("SOURCE1_TABLE.html"), "w") as file:
        file.write("\n".join(trs_list))


def parse_source1_data():
    parser = Source1Parser()
    with open(PAGES_DIR.joinpath("SOURCE1_TABLE.html")) as file:
        read = file.read()
    parser.feed(read)


def write_non_blank_lines():
    lines = []
    with open(DATADUMP_DIR.joinpath("data_source1.txt")) as file:
        for line in file:
            if line.strip() in ("", "\n"):
                continue
            lines.append(line)
    with open(DATADUMP_DIR.joinpath("data_source1_clean.csv"), "w") as file:
        file.write("".join(lines))


def main():
    simplify_page_source1()
    parse_source1_data()
    write_non_blank_lines()


if __name__ == "__main__":
    main()
