"""Entry for make.fun bounty "Laugh Track: The Crypto Trading Joke".

Entry text (draft v1): one funny line about crypto trading.
Limit: 1 to 200 characters. No trailing newline is written.
"""

import os

ENTRY = "My portfolio is so red, even the bulls are wearing sunglasses."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
