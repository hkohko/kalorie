import httpx


def main(url: str):
    response = httpx.get(url)
    return response
