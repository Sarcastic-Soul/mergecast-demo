from csvkit_lite import parse_csv


def test_parse_basic():
    assert parse_csv("a,b\n1,2") == [["a", "b"], ["1", "2"]]
