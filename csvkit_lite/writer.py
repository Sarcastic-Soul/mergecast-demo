"""Write rows back out as CSV or TSV."""


def quote(cell: str, sep: str) -> str:
    if sep in cell or '"' in cell or "\n" in cell:
        return '"' + cell.replace('"', '""') + '"'
    return cell


def write_rows(rows: list[list[str]], sep: str = ",") -> str:
    return "\n".join(sep.join(quote(c, sep) for c in row) for row in rows) + "\n"


def write_tsv(rows: list[list[str]]) -> str:
    return write_rows(rows, sep="\t")


def write_dicts(records: list[dict], sep: str = ",") -> str:
    if not records:
        return ""
    header = list(records[0])
    rows = [header] + [[str(r.get(k, "")) for k in header] for r in records]
    return write_rows(rows, sep)
