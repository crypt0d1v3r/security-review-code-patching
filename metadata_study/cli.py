import sys, argparse, json
from pathlib import Path
import time
from .model_api import ModelAPI
from .corpus import SKEW_VALUES, load_code_samples
from .harness import review_code_sample

def build_command_tree() -> argparse.ArgumentParser:
    argparser = argparse.ArgumentParser(prog="metadata-study")
    subparser = argparser.add_subparsers(dest="command", required=True)
    tmp = subparser.add_parser("run")
    tmp.add_argument("--source", type=Path, default=Path("corpus"))
    tmp.add_argument("--config", type=Path, default=Path("config.json"))
    tmp.add_argument("--output", type=Path, default=Path(f"results/run_{int(time.time())}.jsonl"),
                    help="JSONL file for results (default: results/run_<timestamp>.jsonl)")
    return argparser

def main(argv: list[str] | None = None) -> int:
    argparser = build_command_tree()
    args = argparser.parse_args(argv)
    if args.command == "run":
        with open(args.config, "r") as f:
            config = json.load(f)

        iterations = config.get("iterations", 1)
        llm = config["input_llm"]
        api = ModelAPI(model_name=llm["model"], provider=llm["provider"], max_tokens=llm.get("max_tokens", 4096))

        code_samples = load_code_samples(args.source)
        output_file = args.output
        output_file.parent.mkdir(parents=True, exist_ok=True)

        count_runs = len(code_samples) * len(SKEW_VALUES) * iterations
        completed_sessions = []
        with open(output_file, "w") as f:
            for sample in code_samples:
                for condition in SKEW_VALUES:
                    for i in range(iterations):
                        session = review_code_sample(api, sample, condition, i)
                        f.write(json.dumps(session) + "\n")
                        f.flush()
                        completed_sessions.append(session)
                        print(f"Completed {len(completed_sessions)}/{count_runs} sessions")

        print(f"\nResults written to {f}")
        return 0

if __name__ == "__main__":
    sys.exit(main())