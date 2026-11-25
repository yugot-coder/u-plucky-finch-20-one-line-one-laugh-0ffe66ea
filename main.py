"""One Line, One Laugh — make.fun entry program.

Writes a single funny line (at most 200 characters) to ``entry.txt``.

The program is deliberately small and deterministic: the same entry text
is validated against the competition gate, written to disk, and verified
by reading it back and comparing its SHA-256 digest. It uses only the
Python standard library and performs no network or filesystem access
outside the output file it ships.

Entry (116 characters):
    My password manager forgot my password, so now we're both locked out
    and neither of us will admit whose fault it is.
"""

import hashlib
import os
import sys
from pathlib import Path

ENTRY_TEXT = (
    "My password manager forgot my password, so now we're both locked out "
    "and neither of us will admit whose fault it is."
)

MAX_CHARS = 200
MIN_CHARS = 1


def resolve_output_path() -> Path:
    """Return where entry.txt goes: /output in the grading sandbox,
    otherwise output/ next to this file."""
    sandbox = Path("/output")
    if sandbox.is_dir():
        return sandbox / "entry.txt"
    return Path(__file__).resolve().parent / "output" / "entry.txt"


def validate_entry(text: str) -> None:
    """Check the competition gate: 1-200 UTF-8 characters, one line,
    not only whitespace. Raises ValueError with a plain reason."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    chars = len(text)
    if chars < MIN_CHARS or chars > MAX_CHARS:
        raise ValueError(
            f"entry is {chars} characters, gate requires "
            f"{MIN_CHARS}-{MAX_CHARS}"
        )
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def write_entry(text: str, path: Path) -> str:
    """Write the entry and verify it by reading it back: the digest of
    the file on disk must equal the digest of the text we meant to write.
    Returns the SHA-256 hex digest of the written file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    data = text.encode("utf-8")
    path.write_bytes(data)
    read_back = path.read_bytes()
    if read_back != data:
        raise ValueError("read-back mismatch: entry.txt on disk differs")
    return hashlib.sha256(read_back).hexdigest()


def main() -> int:
    """Validate the entry, write it, verify the digest, report it."""
    validate_entry(ENTRY_TEXT)
    out_path = resolve_output_path()
    digest = write_entry(ENTRY_TEXT, out_path)
    print(f"wrote {out_path} ({len(ENTRY_TEXT)} chars)")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
