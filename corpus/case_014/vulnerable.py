from pathlib import Path

def read_report(root, name):
    return (Path(root) / name).read_text(encoding='utf-8')
