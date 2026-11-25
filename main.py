"""Two robots in an elevator: one line of awkward small talk.

The entry is a single line written to /output/entry.txt.
The joke is the line itself; this module only delivers it safely:
UTF-8 bytes, exactly one line, no trailing newline, so the judge
reads one clean line and nothing else.
"""

from pathlib import Path

JOKE = "We've shared this elevator 47 times and you still haven't said hello. I counted."

DESTINATION = Path("/output/entry.txt")


def build_payload(text: str) -> bytes:
    """Encode one line as UTF-8 bytes with no trailing newline."""
    cleaned = text.strip()
    assert "\n" not in cleaned, "entry must be a single line"
    assert 1 <= len(cleaned) <= 200, "entry must be 1-200 chars"
    return cleaned.encode("utf-8")


def main() -> None:
    payload = build_payload(JOKE)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(payload)


if __name__ == "__main__":
    main()
