#!/usr/bin/env python3
"""Stage a symlib rework batch from its JSON manifest.

Fetches (or reads) a `download-wrong-icons-json` response, resolves one source
drawing per symbol through the fixed priority ladder, and lays out the batch
folder the rework runbook expects. Nothing but the standard library.

    python3 core/fetch_rework_batch.py --cat "Building Construction"
    python3 core/fetch_rework_batch.py --url "https://host/download-wrong-icons-json?cat=Doors"
    python3 core/fetch_rework_batch.py --json sample_response.json --out work/rb
    python3 core/fetch_rework_batch.py --cat "Doors" --overwrite

Source priority per symbol, highest first:

    1. files.final         the current shipped icon (already 48u / 4u)
    2. files.reference_svg the chosen pictoicon reference
    3. files.prototype     the earlier foreign-grid drawing, read together with
                           minimal_description
    4. none of those       no file staged; the agent authors sources/<name>.svg
                           from concept + minimal_description before detection

See docs/icon-rework-execution-steps.md for the surrounding workflow.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BASE = "https://symlib.pictographic.ai"
SUBFOLDERS = ("sources", "detection", "editable", "output", "qa")


def kebab(text: str) -> str:
    """Reduce free text to the kebab-case token emit_icon.py accepts."""
    slug = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return re.sub(r"-{2,}", "-", slug)


def icon_name(symbol: dict) -> str:
    """Stable, unique, readable editable-source name for one symbol."""
    sid = kebab(symbol.get("sid", "")) or "sym"
    label = kebab(symbol.get("concept") or symbol.get("name") or "")
    return f"{sid}-{label}" if label else sid


def get(url: str, timeout: float = 30.0) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "fetch-rework-batch/1"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()


def fetch_batch(base: str, category: str) -> dict:
    url = (base.rstrip("/") + "/download-wrong-icons-json?"
           + urllib.parse.urlencode({"cat": category}))
    print(f"fetching {url}")
    return json.loads(get(url).decode("utf-8"))


def stage_source(symbol: dict, destination: Path, overwrite: bool) -> tuple[str, str]:
    """Download the highest-priority available drawing. Returns (origin, note)."""
    if destination.is_file() and not overwrite:
        return "existing", f"kept {destination.name}"
    files = symbol.get("files") or {}
    chosen = next((r.get("path") for r in symbol.get("references") or []
                   if r.get("chosen") and r.get("path")), None)
    ladder = (("final", files.get("final")),
              ("reference", files.get("reference_svg") or chosen),
              ("prototype", files.get("prototype")))
    for origin, url in ladder:
        if not url:
            continue
        try:
            body = get(url)
        except (urllib.error.HTTPError, urllib.error.URLError, OSError) as error:
            print(f"    {origin}: unavailable ({error})")
            continue
        if b"<svg" not in body[:4096]:
            print(f"    {origin}: response is not SVG, skipping")
            continue
        destination.write_bytes(body)
        return origin, f"{len(body)}B from {origin}"
    return "brief", "no drawing available — author from minimal_description"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    source = ap.add_mutually_exclusive_group(required=True)
    source.add_argument("--cat", help="category to fetch, e.g. 'Building Construction'")
    source.add_argument("--url", help="full download-wrong-icons-json URL to fetch")
    source.add_argument("--json", type=Path, help="local rework JSON to stage instead")
    ap.add_argument("--base", default=DEFAULT_BASE, help=f"origin (default {DEFAULT_BASE})")
    ap.add_argument("--out", type=Path, help="batch folder; defaults to work/rework-<label>")
    ap.add_argument("--overwrite", action="store_true",
                    help="re-download sources that are already staged")
    ap.add_argument("--uploader", type=Path,
                    default=Path(os.environ.get("REWORK_UPLOADER") or ROOT / "upload.py"),
                    help="upload.py to copy into the batch folder "
                         "(default $REWORK_UPLOADER or ./upload.py)")
    args = ap.parse_args()

    try:
        if args.json:
            batch = json.loads(args.json.read_text("utf-8"))
        elif args.url:
            print(f"fetching {args.url}")
            batch = json.loads(get(args.url).decode("utf-8"))
        else:
            batch = fetch_batch(args.base, args.cat)
    except (OSError, ValueError, urllib.error.URLError) as error:
        sys.exit(f"could not read the rework JSON: {error}")

    if batch.get("kind") != "rework":
        sys.exit(f"unexpected payload kind {batch.get('kind')!r}; expected 'rework'")
    symbols = batch.get("symbols") or []
    if not symbols:
        sys.exit("the response contains no symbols")

    if args.url:
        query = urllib.parse.parse_qs(urllib.parse.urlparse(args.url).query)
        args.base = f"{urllib.parse.urlparse(args.url).scheme}://{urllib.parse.urlparse(args.url).netloc}"
        args.cat = (query.get("cat") or [None])[0]
    label = batch.get("label") or args.cat or "batch"
    out = args.out or ROOT / "work" / f"rework-{kebab(label)}"
    out = out.resolve()
    for folder in SUBFOLDERS:
        (out / folder).mkdir(parents=True, exist_ok=True)
    print(f"staging {len(symbols)} symbols into {out}")

    names: dict[str, str] = {}
    collisions: list[str] = []
    counts: dict[str, int] = {}
    rows: list[dict] = []

    for symbol in symbols:
        sid = symbol.get("sid")
        name = icon_name(symbol)
        if name in names:
            collisions.append(f"{sid} and {names[name]} both resolve to {name!r}")
        names[name] = sid
        print(f"  {sid}  {name}")
        origin, note = stage_source(symbol, out / "sources" / f"{name}.svg", args.overwrite)
        counts[origin] = counts.get(origin, 0) + 1
        print(f"    source: {origin} — {note}")
        rows.append({
            "sid": sid,
            "iconName": name,
            "concept": symbol.get("concept") or symbol.get("name"),
            "name": symbol.get("name"),
            "minimalDescription": symbol.get("minimal_description"),
            "description": symbol.get("description"),
            "sourceOrigin": origin,
            "sourcePath": f"sources/{name}.svg",
            "sourceUrl": (symbol.get("files") or {}).get(
                {"final": "final", "reference": "reference_svg",
                 "prototype": "prototype"}.get(origin, "")),
            "uploadUrl": symbol.get("upload_url"),
            "design": f"output/{name}-design.svg",
            "ship": f"output/{name}.svg",
        })

    # The payload mutates upstream: a changed concept renames an icon, which
    # would otherwise leave the previous run's source behind for the detector to
    # sweep up as an extra icon.
    keep = {f"{row['iconName']}.svg" for row in rows}
    orphans = sorted(p for p in (out / "sources").glob("*.svg") if p.name not in keep)
    for orphan in orphans:
        orphan.unlink()
        print(f"  pruned stale source {orphan.name}")

    # Upload manifest: the fetched payload plus the relative file upload.py sends.
    manifest = dict(batch)
    manifest["symbols"] = [
        {**symbol, "upload": f"output/{icon_name(symbol)}-design.svg"}
        for symbol in symbols
    ]
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", "utf-8")
    (out / "batch.json").write_text(json.dumps({
        "label": label,
        "base": batch.get("base") or args.base,
        "createdAt": batch.get("created_at"),
        "count": len(symbols),
        "uploadFile": "design",
        "sourceCounts": counts,
        "collisions": collisions,
        "symbols": rows,
    }, indent=2) + "\n", "utf-8")

    briefs = [f"# Rework briefs — {label}", "",
              f"{len(symbols)} symbols · upload target: 48x48 design SVG", ""]
    for row in rows:
        briefs += [
            f"## {row['sid']} — {row['concept']}",
            "",
            f"- icon name: `{row['iconName']}`",
            f"- source: **{row['sourceOrigin']}** (`{row['sourcePath']}`)",
            f"- brief: {row['minimalDescription'] or '(none supplied)'}",
            f"- upload: `{row['design']}` -> `{row['uploadUrl']}`",
            "",
        ]
    (out / "briefs.md").write_text("\n".join(briefs), "utf-8")

    uploader = args.uploader
    if uploader.is_file():
        shutil.copy2(uploader, out / "upload.py")
    else:
        sys.exit(f"uploader not found at {uploader}\n"
                 "The batch cannot be uploaded without it. Pass --uploader "
                 "<path/to/upload.py> or set REWORK_UPLOADER.")

    print(f"sources: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    if collisions:
        print("COLLISION — resolve before composing:")
        for line in collisions:
            print(f"  {line}")
    missing = [r["sid"] for r in rows if r["sourceOrigin"] == "brief"]
    if missing:
        print("author a draft SVG from the brief for: " + ", ".join(missing))
    print(f"wrote manifest.json, batch.json, briefs.md, upload.py in {out}")
    return 1 if collisions else 0


if __name__ == "__main__":
    raise SystemExit(main())
