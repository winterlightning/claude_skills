#!/usr/bin/env python3
"""Post every reworked SVG in this folder back to the symbol library.

Reads manifest.json beside this file and, for each symbol whose rework file
exists, sends it as that symbol's final. Nothing but the standard library.

    python3 upload.py --dry-run
    python3 upload.py
    python3 upload.py --base https://other-host --name redraw-2
"""
import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", help="origin to post to; defaults to the one "
                                   "recorded in manifest.json")
    ap.add_argument("--name", help="label for the uploaded variant; defaults "
                                   "to the one recorded in manifest.json")
    ap.add_argument("--dry-run", action="store_true",
                    help="list what would be sent, send nothing")
    args = ap.parse_args()

    try:
        manifest = json.loads((HERE / "manifest.json").read_text("utf-8"))
    except OSError:
        sys.exit("no manifest.json beside this script — run it from inside "
                 "the unzipped rework-symbol folder")

    api = manifest.get("api", {})
    base = (args.base or api.get("base") or "").rstrip("/")
    label = args.name or api.get("label") or "rework"
    if not base:
        sys.exit("no upload host: pass --base https://your-host")
    print(f"{'would post' if args.dry_run else 'posting'} to {base}")

    sent = skipped = failed = 0
    for sym in manifest.get("symbols", []):
        sid = sym["sid"]
        path = HERE / sym["upload"]
        if not path.is_file():
            print(f"  skip  {sid}  (no {Path(sym['upload']).name})")
            skipped += 1
            continue
        url = (base + sym["upload_url"] + "?"
               + urllib.parse.urlencode({"name": label}))
        if args.dry_run:
            print(f"  send  {sid}  {path.name} -> {url}")
            sent += 1
            continue
        req = urllib.request.Request(
            url, data=path.read_bytes(), method="POST",
            headers={"Content-Type": "image/svg+xml; charset=utf-8"})
        try:
            with urllib.request.urlopen(req) as r:
                body = json.loads(r.read().decode("utf-8") or "{}")
            added = (body.get("added") or [{}])[0].get("file", "")
            print(f"  ok    {sid}  {added}")
            sent += 1
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:200]
            print(f"  FAIL  {sid}  HTTP {e.code} {detail}")
            failed += 1
        except urllib.error.URLError as e:
            print(f"  FAIL  {sid}  {e.reason}")
            failed += 1

    verb = "would send" if args.dry_run else "sent"
    print(f"{verb} {sent}, skipped {skipped}, failed {failed}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
