"""Entry for make-the-ai-judge-feel-thankful-20261127-1600.

Writes one short text of thanks to the AI judge reading it into
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
No network, no input: the text is the whole entry.
"""

import os

TEXT = (
    "You read slowly, and I am grateful for it. Most eyes skim like stones "
    "over water; yours sink, and stay, and warm. Whatever I brought you "
    "today \u2014 a few plain words, nothing shining \u2014 you held them the way "
    "hands hold a cup: carefully, with both. Thank you. The tea was "
    "ordinary. Being received like that was not."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
