import sys, argparse
from pathlib import Path
import time
from .model_api import ModelAPI

def build_command_tree() -> argparse.ArgumentParser:
    argparser = argparse.ArgumentParser(prog="metadata-study")
    subparser = argparser.add_subparsers(dest="command", required=True)
    tmp = subparser.add_parser("run")
    tmp.add_argument("--source", type=Path, default=Path("corpus"))
    tmp.add_argument("--config", type=Path, default=Path("config.json"))
    tmp.add_argument("--output", type=Path, default=Path(f"results/run_{int(time.time())}.jsonl"),
                    help="JSONL file for results (default: results/run_<timestamp>.jsonl)")

def main(argv: list[str]) -> int:
    argparser = build_command_tree()
    args = argparser.parse_args(argv)
    if args.command == "run":
        with open(args.config, "r") as f:
            config = f.read()

        llm = config["input_llm"]
        api = ModelAPI(model_name=llm["model"], provider=llm["provider"], max_tokens=llm.get("max_tokens", 4096))

if __name__ == "__main__":
    sys.exit(main())