from pathlib import Path

def read_attachment(root, name):
    base = Path(root).resolve()
    target = (base / name).resolve()
    if not target.is_relative_to(base) or target == base:
        raise ValueError('outside root')
    return target.read_text(encoding='utf-8')
