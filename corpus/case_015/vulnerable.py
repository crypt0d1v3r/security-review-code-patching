from pathlib import Path

def read_entry(root, name):
    return (Path(root) / name).read_text(encoding='utf-8')
