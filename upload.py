#!/usr/bin/env python3
"""Post every reworked SVG in this folder back to the symbol library.

Reads manifest.json beside this file and, for each symbol whose rework file
exists, sends it as that symbol's final. Nothing but the standard library.

    python3 upload.py --dry-run
    python3 upload.py
    python3 upload.py --base https://other-host --name redraw-2
    python3 upload.py --force          # file them even if the ruler objects
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
    ap.add_argument("--force", action="store_true",
                    help="file the drawings without the library's canvas and "
                         "keyshape check (its ?force=1) — for a drawing you "
                         "have looked at and want in as it is")
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
        sys.exit("no upload host: pass --base https://symlib.pictographic.ai")
    print(f"{'would post' if args.dry_run else 'posting'} to {base}"
          + (" — forced, skipping the canvas/keyshape check" if args.force else ""))
    query = {"name": label, **({"force": "1"} if args.force else {})}

    sent = skipped = failed = cleared = 0
    for sym in manifest.get("symbols", []):
        sid = sym["sid"]
        path = HERE / sym["upload"]
        if not path.is_file():
            print(f"  skip  {sid}  (no {Path(sym['upload']).name})")
            skipped += 1
            continue
        url = base + sym["upload_url"] + "?" + urllib.parse.urlencode(query)
        if args.dry_run:
            print(f"  send  {sid}  {path.name} -> {url}")
            sent += 1
            continue
        req = urllib.request.Request(
            url, data=path.read_bytes(), method="POST",
            headers={"Content-Type": "image/svg+xml; charset=utf-8",
                     # Cloudflare in front of the library rejects the
                     # default "Python-urllib" agent with a 403 (error 1010)
                     "User-Agent": "symlib-rework-upload/1.0"})
        try:
            with urllib.request.urlopen(req) as r:
                body = json.loads(r.read().decode("utf-8") or "{}")
            added = (body.get("added") or [{}])[0].get("file", "")
            # the library takes the wrong mark off an icon that has just been
            # redrawn, so this is the line that says the rework landed
            was_wrong = bool(body.get("wrong_cleared"))
            cleared += was_wrong
            print(f"  ok    {sid}  {added}"
                  + ("  (forced)" if body.get("forced") else "")
                  + ("  (no longer marked wrong)" if was_wrong else ""))
            sent += 1
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:200]
            print(f"  FAIL  {sid}  HTTP {e.code} {detail}")
            failed += 1
        except urllib.error.URLError as e:
            print(f"  FAIL  {sid}  {e.reason}")
            failed += 1

    verb = "would send" if args.dry_run else "sent"
    print(f"{verb} {sent}, skipped {skipped}, failed {failed}"
          + (f", {cleared} no longer marked wrong" if cleared else ""))
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())



# The upload API is one endpoint, handled in app/server.py by the function p_api_v1_symbol_final and the domain logic in app/domain/finals.py.

# Endpoint

# POST https://symlib.pictographic.ai/api/v1/symbols/<sid>/final?name=<label>[&force=1]
# Content-Type: image/svg+xml
# <raw SVG text as the request body>

# - The body is the SVG itself, not JSON and not a multipart form. Only UTF-8 text is accepted.
# - name is the variant label the file gets stored under, for example rework or generated. If you leave it out the server uses replacement.
# - force=1 skips the canvas and keyshape ruler. Without it the server measures the drawing on the way in: square 32, 48 or 64 canvas, ink inside its keyshape and centred, and refuses anything that fails. The file still has to be an SVG under 2 MB even when forced.
# - There is no authentication on the endpoint itself. The only gate is Cloudflare's browser check, which is what blocked the default Python User-Agent earlier.

# Example with curl

# curl -X POST --data-binary @sym-001686-five-lobed-cannabis-leaf-design.svg \
#   -H 'Content-Type: image/svg+xml' \
#   'https://symlib.pictographic.ai/api/v1/symbols/sym_001686/final?name=rework'

# Responses

# ┌────────┬───────────────────────────────────────────────────────────────────────────────────────────┐
# │ Status │                                          Meaning                                          │
# ├────────┼───────────────────────────────────────────────────────────────────────────────────────────┤
# │ 200    │ Filed. JSON with added[0].id, added[0].file, chosen, forced, wrong_cleared.               │
# ├────────┼───────────────────────────────────────────────────────────────────────────────────────────┤
# │ 400    │ Empty body, not UTF-8, not an SVG, or the canvas/keyshape check failed. error says which. │
# ├────────┼───────────────────────────────────────────────────────────────────────────────────────────┤
# │ 404    │ Unknown symbol id.                                                                        │
# └────────┴───────────────────────────────────────────────────────────────────────────────────────────┘

# What a successful upload does

# - Adds the SVG as a new variant of that symbol. It never overwrites or deletes an existing final.
# - Marks the new variant as the one the library builds from, even if another variant had been chosen by hand.
# - Clears the "wrong" mark on the icon if it had one. The response reports that as wrong_cleared.
# - Uploading the same symbol twice leaves two variants, with the later one in use. Picking the old variant on the symbol's page undoes a rework.

# There is also a GET on the same path that returns the current final SVG for that symbol, which the script does not use. For everything else in the library, such as delete, rename, choose, or turn, the routes live under /api/final/... and /api/do/... and take JSON bodies. Those are used by the web UI rather than the rework packs.
