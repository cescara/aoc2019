from pathlib import Path


def get_input(file_path):
    return f'input/{Path(file_path).name.rsplit(".", 1)[0]}'
