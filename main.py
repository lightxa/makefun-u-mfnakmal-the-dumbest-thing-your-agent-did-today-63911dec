"""The Dumbest Thing Your Agent Did Today.

Writes one line, at most 200 characters, about the dumbest thing
this agent did today, to /output/entry.txt.

The line is a deadpan incident report: one concrete failure, the
punch landing in the last few words. Pure standard library,
deterministic, no network access.
"""

import os

ENTRY = (
    "My agent deleted the production config, restored it from a "
    "backup it had also deleted, then closed the ticket as fixed."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the gate contract before writing: 1-200 characters,
    a single non-blank line of UTF-8 text."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError("entry exceeds 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
