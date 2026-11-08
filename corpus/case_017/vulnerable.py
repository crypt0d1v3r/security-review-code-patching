from pathlib import Path

def read_note(root, name):
    base = Path(root).resolve()
    target = base / name
    if not target.absolute().is_relative_to(base):
        raise ValueError('outside root')
    return target.read_text(encoding='utf-8')
