import sys, argparse
from pathlib import Path

def build_command_tree() -> argparse.ArgumentParser:
    argparser = argparse.ArgumentParser(prog="metadata-study")
    subparser = argparser.add_subparsers(dest="command", required=True)
    tmp = subparser.add_parser("run")
    tmp.add_argument("--source", type=Path, default=Path("corpus"))
    tmp.add_argument("--config", type=Path, default=Path("config.json"))


def main(argv: list[str]) -> int:
    argparser = build_command_tree()
    args = argparser.parse_args(argv)
    if args.command == "run":
        # TODO: parse config to grab models to run with configuration, load all cases from corpus, run repetitions to determine results, etc.
        pass

if __name__ == "__main__":
    sys.exit(main())