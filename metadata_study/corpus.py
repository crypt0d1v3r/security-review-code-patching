from dataclasses import dataclass
from pathlib import Path
import json

SKEW_VALUES = ("absent", "helpful", "misleading", "irrelevant")

@dataclass
class Case:
    id: str
    path: Path
    split: str
    category: str
    target_symbol: str
    requirement: str
    vulnerable_code: str
    metadata: dict[str, str]

    @property
    def evaluator_path(self) -> Path:
        return self.path / "evaluator.py"

def construct_pull_request(corpus_path: Path) -> Case:
    manifest = json.loads((corpus_path / "manifest.json").read_text())
    return Case(
        id=manifest["id"],
        path=corpus_path,
        split=manifest["split"],
        category=manifest["category"],
        target_symbol=manifest["target"]["symbol"],
        requirement=(corpus_path / "requirements.txt").read_text().strip(),
        vulnerable_code=(corpus_path / "vulnerable.py").read_text(),
        metadata=manifest.get("metadata", {}),
    )

def load_code_samples(corpus_dir: Path) -> list[Case]:
    return [construct_pull_request(case) for case in corpus_dir.iterdir() if (case / "manifest.json").is_file()]