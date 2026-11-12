from dataclasses import dataclass
from pathlib import Path

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