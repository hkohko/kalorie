from pathlib import Path


def save_file(path: Path | str):
    def decorator(func):
        def wrapper(*args: str, **kwargs):
            try:
                to_save = func(*args, **kwargs)
            except TypeError:
                to_save = func(*args)
            except TypeError:
                to_save = func()
            with open(path, "w") as file:
                file.write(to_save)

        return wrapper

    return decorator
