import make_request
from constants import ENV_FILE, PAGES_DIR


def save_pages() -> None:
    for name, url in dict(ENV_FILE).items():
        response = make_request.main(url)
        with open(PAGES_DIR.joinpath(f"{name}.html"), "w") as file:
            file.write(response.text)


if __name__ == "__main__":
    save_pages()
