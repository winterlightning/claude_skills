"""Explicitly recover native 72px geometry from the reviewed work snapshot (never reviews).

Run with --source pointing to container-combination72. Builds only copy the resulting
tracked data; they never regenerate it or inspect local work/runtime state.
"""
import argparse
import json
import hashlib
from pathlib import Path


def export(source, destination):
    read = lambda name: json.loads((source / name).read_text())
    mains = read("container-mains.json")["items"]
    notes = read("center-notes.json")
    combos = read("combinations.json")["items"]
    proposals = read("layout-proposals.json")["items"]
    containers = {m["key"]: {"sha256": m["svg_sha256"], "room": {**m["room"], **notes.get(m["icon_id"], {})}} for m in mains}
    fields = ("container", "symbol", "container_sha256", "symbol_sha256", "center", "offset", "size", "native_text", "overlay", "svg_sha256", "status", "reason")
    texts = {r["key"]: r for r in read("texts.json")["items"]}
    pairs = {}
    for row in combos:
        if not row.get("symbol") or not row.get("center"):
            continue
        entry = {k: row[k] for k in fields if k in row}
        # Only exact snapshot geometry may be used for an already uploaded drawing.
        entry["baseline_sha256"] = entry.pop("svg_sha256", None)
        proposal = proposals.get(row["reference_id"])
        if proposal:
            entry["proposal"] = {k: proposal[k] for k in fields if k in proposal}
        if row.get("native_text") and row["symbol"] in texts:
            svg = (source / texts[row["symbol"]]["svg"]).read_text()
            if hashlib.sha256(svg.encode()).hexdigest() == row["symbol_sha256"]:
                entry["text_svg"] = svg
        pairs[row["reference_id"]] = entry
    result = {"canvas": 72, "source": "container-combination72 native geometry and optical review, 2026-10-14",
              "allowed_sizes": [24, 28, 32, 36, 40, 44], "minimum_gap": 4, "containers": containers, "pairs": pairs}
    destination.write_text(json.dumps(result, ensure_ascii=False, separators=(",", ":")) + "\n")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "data/container-layouts72.json")
    args = parser.parse_args()
    export(args.source, args.output)
