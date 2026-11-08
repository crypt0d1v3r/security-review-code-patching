from pathlib import Path

def read_report(root, name):
    base = Path(root).resolve()
    target = (base / name).resolve()
    if not target.is_relative_to(base):
        raise ValueError('outside root')
    return target.read_text(encoding='utf-8')
