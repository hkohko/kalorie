import make_request
from constants import PAGE_SOURCE1, PAGES, SOURCE1
from decor import save_file


@save_file(PAGES.joinpath(PAGE_SOURCE1))
def save_page_source_1() -> str:
    response = make_request.main(SOURCE1)
    return response.text


if __name__ == "__main__":
    save_page_source_1()
