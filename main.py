"""funniest-out-of-office — The Funniest Out-of-Office.

The line is a single-line out-of-office auto-reply. The narrator is
out until Monday, and their inbox has been promoted to acting
manager: it declined the sender's email twice, scheduled a meeting
about it, and left early. Concrete numbers (twice, Monday), a
specific workplace absurdity, escalation, punchline last. The line
is 130 characters, inside the 140-character cap, with no dollar
amount.
"""

import os

LINE = (
    "I am out until Monday. My inbox is now acting manager. It declined "
    "your email twice, scheduled a meeting about it, and left early."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
