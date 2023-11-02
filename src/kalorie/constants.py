from pathlib import Path

from dotenv import dotenv_values

PROJ_DIR = Path(__file__).parents[2]
SRC = PROJ_DIR.joinpath("src")
KALORIE = SRC.joinpath("kalorie")
ENV = PROJ_DIR.joinpath(".env")
PAGES_DIR = KALORIE.joinpath("page")
DATADUMP_DIR = KALORIE.joinpath("data_dump")

PAGE_SOURCE1 = "SOURCE1.html"
PAGE_SOURCE2_1 = "SOURCE2_1.html"
PAGE_SOURCE2_2 = "SOURCE2_2.html"

ENV_FILE = dotenv_values(ENV)
SOURCE1 = ENV_FILE.get("SOURCE1")
