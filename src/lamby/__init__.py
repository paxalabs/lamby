import random
import sys
import textwrap

__version__ = "0.0.2"

LINES = [
    "baa.",
    "coming soon.",
    "i am the one who baas.",
    "tread lightly.",
    "99.1% wool.",
    "the kitchen is closed. come back later.",
    "no half measures. only whole sheep.",
    "say my name. (it's lamby)",
    "i'm not saying what i do. i have a lawyer.",
]

LAMB = r"""
  \
   \      .@@@@@.
    \   .@@@@@@@@@.
     [o-o]@@@@@@@@@@
      \_/ @@@@@@@@@
           ||    ||
"""


def bubble(text, width=40):
    lines = textwrap.wrap(text, width) or [""]
    w = max(len(line) for line in lines)
    top, bottom = " " + "_" * (w + 2), " " + "-" * (w + 2)
    if len(lines) == 1:
        return "\n".join([top, f"< {lines[0]} >", bottom])
    body = []
    for i, line in enumerate(lines):
        left, right = ("/", "\\") if i == 0 else ("\\", "/") if i == len(lines) - 1 else ("|", "|")
        body.append(f"{left} {line.ljust(w)} {right}")
    return "\n".join([top, *body, bottom])


def main():
    args = sys.argv[1:]
    if args in (["--version"], ["-V"]):
        print(f"lamby {__version__}")
        return
    print(bubble(" ".join(args) or random.choice(LINES)) + LAMB.rstrip())
