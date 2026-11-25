import os

LINE = "Magnetron fault: I heated your soup for 90 seconds. The bowl is 71\u00b0C, the soup is 12\u00b0C. The soup has unionised. Negotiations begin at noon."


def validate_output(path):
    # Read back the written file and prove it is byte-identical to LINE:
    # exact string, within the 200-char limit, and zero newlines (single line).
    with open(path, "r", encoding="utf-8", newline="") as f:
        data = f.read()
    assert data == LINE, "output differs from final text"
    assert len(data) == len(LINE) == 139, "output length is not 139 chars"
    assert len(data.encode("utf-8")) == 141, "output length is not 141 bytes"
    assert len(data) <= 200, "output exceeds the 200-char limit"
    assert data.count("\n") == 0, "output must be a single line"
    assert data.endswith("Negotiations begin at noon.") and "71\u00b0C" in data and "12\u00b0C" in data, "output must end on negotiations and name both temperatures"


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get(
        "OUTPUT_DIR", "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    validate_output(path)


if __name__ == "__main__":
    main()
