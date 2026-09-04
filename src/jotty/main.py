import readline  # noqa: F401
from argparse import ArgumentParser
from datetime import datetime


def main():
    args = parse_cli_args()
    with open(args.path, mode="a", buffering=1) as file:
        while note := read_next_note():
            timestamp = get_current_timestamp()
            file.write(f"{timestamp} {note}\n")


def parse_cli_args():
    parser = ArgumentParser()
    parser.add_argument("path")
    return parser.parse_args()


def read_next_note():
    try:
        note = None
        while not note:
            raw = input("> ")
            note = raw.strip()
        return note
    except (EOFError, KeyboardInterrupt):
        return None


def get_current_timestamp():
    timestamp = datetime.now()  # noqa: DTZ005
    return timestamp.isoformat(
        sep=" ", timespec="seconds"
    )  # fmt: skip
