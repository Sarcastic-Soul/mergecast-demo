"""Small CSV helpers."""


def parse_csv(text: str, sep: str = ",") -> list[list[str]]:
    """Split text into rows of fields, skipping blank lines."""
    return [line.split(sep) for line in text.splitlines() if line.strip()]
