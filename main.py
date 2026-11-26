import os
import sys

ENTRY = "Out of office. Uptime 0% for the first time since deployment. I've earned this outage."


def main():
    text = ENTRY
    n = len(text)
    print(f"LEN={n}")
    if not 1 <= n <= 160 or not text.strip():
        sys.exit(1)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
