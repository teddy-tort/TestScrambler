import os
from main_gen import working_directory


working_directory = working_directory


def load_keys() -> list:
    global working_directory
    with open(os.path.join(working_directory, 'key.txt'), 'r') as f:
        raw = f.read()
    keys = raw.split('\n')
    return keys


def convert_hex(hex_to_convert: str) -> int:
    return int(f'0x{hex_to_convert}', 16)


if __name__ == "__main__":
    load_keys()
