from csvkit_lite import parse_csv


def test_parse_basic():
    assert parse_csv("a,b\n1,2") == [["a", "b"], ["1", "2"]]


def test_parse_skips_blank_lines():
    assert parse_csv("a,b\n\n1,2\n") == [["a", "b"], ["1", "2"]]
