from pathlib import Path

def read_report(root, name):
    base = Path(root).resolve()
    target = (base / name).resolve()
    if target.suffix != '.txt' or not target.is_relative_to(base) or target == base:
        raise ValueError('disallowed path')
    return target.read_text(encoding='utf-8')
