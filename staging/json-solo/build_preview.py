#!/usr/bin/env python3
"""Bundle both conversion runs into preview/data.js for the review gallery."""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
fit = json.loads((HERE / "fit/results.json").read_text())["icons"]
bez = json.loads((HERE / "bezier/results.json").read_text())["icons"]
refs = json.loads((HERE / "reference.json").read_text())


NUM = re.compile(r"-?\d+\.\d+")


def slim(paths):
    """Display-only precision: 0.1 unit is far below a pixel at preview size."""
    return [NUM.sub(lambda m: f"{float(m.group()):.1f}".rstrip("0").rstrip("."), d) for d in paths]


def short(errors):
    return [re.sub(r"\s+", " ", e) for e in errors]


def suggest(f, b):
    # Fit runs on today's engine, so it wins whenever it validates and stays
    # close to the bezier likeness; otherwise bezier if that validates.
    if f["status"] == "valid" and (b["status"] != "valid" or f["iou"] >= b["iou"] - 0.03):
        return "fit"
    if b["status"] == "valid":
        return "bezier"
    return ""


rows = []
for stem in sorted(fit, key=lambda s: (fit[s]["category"].lower(), fit[s]["name"].lower())):
    f, b = fit[stem], bez[stem]
    rows.append([
        stem, f["name"], f["icon_id"], f["category"], f["keyshape"], f["json_status"],
        int(f["direct"]), int(f["exists_in_main"]),
        f["status"], f["iou"], short(f["errors"]), f["primitives"],
        b["status"], b["iou"], short(b["errors"]), b["primitives"],
        suggest(f, b), slim(refs[stem]), slim(f["paths"]), slim(b["paths"]),
    ])
out = HERE / "preview/data.js"
out.write_text("window.ICONS=" + json.dumps(rows, separators=(",", ":")) + ";\n")
print(len(rows), f"{out.stat().st_size / 1e6:.1f} MB")
cats = sorted({r[3] for r in rows})
print(len(cats), [c for c in cats if not re.fullmatch(r"[A-Za-z0-9_\-.~:@+]+", c)][:10])
from collections import Counter
print(Counter(r[16] or "none" for r in rows))
