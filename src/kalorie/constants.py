from pathlib import Path

from dotenv import dotenv_values

PROJ_DIR = Path(__file__).parents[2]
SRC = PROJ_DIR.joinpath("src")
KALORIE = SRC.joinpath("kalorie")
ENV = PROJ_DIR.joinpath(".env")
PAGES = KALORIE.joinpath("page")

PAGE_SOURCE1 = "SOURCE1.html"
ENV_FILE = dotenv_values(ENV)
SOURCE1 = ENV_FILE.get("SOURCE1")
