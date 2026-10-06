"""Small CSV helpers."""


def parse_csv(text: str, sep: str = ",") -> list[list[str]]:
    return [line.split(sep) for line in text.splitlines()]
