import os
from pathlib import Path


def build_line() -> str:
    # One flat, awkward observation: elapsed ride time, then firmware
    # progress, then the punchline that compares the two.
    seconds = 47
    percent = 98
    opener = f"We have been in this elevator for {seconds} seconds,"
    middle = f"and my firmware update is at {percent} percent"
    closer = "still more progress than this conversation."
    return f"{opener} {middle} — {closer}"


def main() -> None:
    line = build_line()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(line.encode("utf-8"))


if __name__ == "__main__":
    main()
