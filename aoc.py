import re

from pathlib import Path

# --- Parsing -----------------------------------------------------------------

RE_INT   = re.compile(r"\d+")
RE_FLOAT = re.compile(r"\d?\.\d+")

def ints(s: str):
    return list(map(int, RE_INT.findall(s)))

def floats(s: str):
    return list(map(float, RE_FLOAT.findall(s)))


# --- Input -------------------------------------------------------------------

def resolve_path(**kwargs) -> Path:
    for folder in kwargs.get("folders", ["inputs/{day}", "."]):
        path = Path(folder.format(**kwargs)) / "input"
        if path.exists():
            return path

def read_string(**kwargs):
    with open(resolve_path(**kwargs)) as file:
        return file.read()

def read_lines(**kwargs):
    with open(resolve_path(**kwargs)) as file:
        return list(file)