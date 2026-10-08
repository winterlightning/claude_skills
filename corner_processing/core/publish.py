#!/usr/bin/env python3
"""core/publish.py — store the round and sharp outputs as icon records on the review site.

Each output becomes `<key>--round` / `<key>--sharp`, its own icon in the source's family with style round or sharp
(Worker POST /api/icons/styled, migration 0019). New drawings start Ready; an icon whose corner check failed is a
failed build. Sending the same drawing again changes nothing, and outputs/<set>/published.json remembers what
was stored, so a re-run sends only the outputs whose drawing or check changed (--all sends every one). A record
someone picked, edited, reviewed or commented on is kept (reported) unless --replace.

  python3 -m core.publish --user jakes                      # outputs/solo48 -> production, password asked
  python3 -m core.publish --styles round --limit 50         # a first few
  python3 -m core.publish --user jakes --files abdominal-torso a-line-skirt   # only these icons
  python3 -m core.publish --user jakes --replace            # also overwrite records people worked on
  PICTOGRAPHIC_PUSH_TOKEN=... python3 -m core.publish       # or the push token instead of a sign-in

Reads input/<set>/icons.csv (file name -> Worker key) and outputs/<set>/toggle.json (each icon's check).
"""

import argparse
import csv
import getpass
import hashlib
import http.cookiejar
import json
import os
import sys
import time
import urllib.request

from .fetch import API
from .paths import INPUT_DIR, OUT_DIR, SETS

BATCH = 25             # icons per request (the route takes up to 50)


class Client:
    def __init__(self, api, token=None):
        self.api, self.token = api.rstrip("/"), token
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

    def post(self, path, body, tries=4):
        """POST with retries: a timed-out batch may still have been stored, and sending it again is safe (an
        unchanged drawing is skipped)."""
        for k in range(tries):
            try:
                return self._post(path, body)
            except (TimeoutError, urllib.error.URLError) as e:
                if k == tries - 1:
                    raise SystemExit(f"{path}: {type(e).__name__}: {e} (after {tries} tries)")
                time.sleep(5 * (k + 1))

    def _post(self, path, body):
        headers = {"Content-Type": "application/json", "User-Agent": "corner48-publish/1.0"}  # Cloudflare 403s urllib's UA
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        req = urllib.request.Request(self.api + path, data=json.dumps(body).encode(), headers=headers, method="POST")
        try:
            with self.opener.open(req, timeout=120) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code >= 500:
                raise urllib.error.URLError(f"HTTP {e.code}")
            raise SystemExit(f"{path}: HTTP {e.code} {e.read().decode(errors='replace')[:300]}")


MANIFEST = "published.json"   # in the outputs folder: what this machine last stored, per styled key


def items(set_name, styles, out_dir, files=None):
    """(source_key, style, svg, check) for every output that has a Worker key and a corner check result; the
    outputs without a key and those without a check (never sent: a missing check is not an ok)."""
    with open(os.path.join(INPUT_DIR, set_name, "icons.csv"), encoding="utf-8") as f:
        keys = {os.path.basename(r["file"]): r["key"] for r in csv.DictReader(f)}
    with open(os.path.join(out_dir, "toggle.json"), encoding="utf-8") as f:
        toggles = json.load(f)["icons"]
    found, missing, unchecked = [], [], []
    for style in styles:
        folder = os.path.join(out_dir, style)
        for name in sorted(os.listdir(folder)):
            if not name.endswith(".svg") or (files and name not in files):
                continue
            if name not in keys:
                missing.append(f"{style}/{name}")
                continue
            check = ((toggles.get(name) or {}).get(style) or {}).get("check", {}).get("status")
            if check not in CHECKS:
                unchecked.append(f"{style}/{name}")
                continue
            with open(os.path.join(folder, name), encoding="utf-8") as f:
                found.append({"source_key": keys[name], "style": style, "svg": f.read(), "check": check})
    return found, missing, unchecked


CHECKS = ("ok", "contact", "fail")


def styled_key(item):
    return f"{item['source_key']}--{item['style']}"


def fingerprint(item):
    return {"file_sha": hashlib.sha256(item["svg"].encode("utf-8")).hexdigest(), "check": item["check"]}


def load_manifest(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def save_manifest(path, manifest):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(manifest, f, separators=(",", ":"), sort_keys=True)
    os.replace(tmp, path)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Store the round and sharp outputs as icon records (style round / sharp).")
    ap.add_argument("--api", default=API)
    ap.add_argument("--set", default=SETS["solo"], help="input/outputs set folder (default: %(default)s)")
    ap.add_argument("--out", help="outputs folder (default: outputs/<set>)")
    ap.add_argument("--styles", nargs="+", choices=("round", "sharp"), default=["round", "sharp"])
    ap.add_argument("--limit", type=int, default=0, help="send only the first N items (a trial)")
    ap.add_argument("--files", nargs="+", help="send only these icons (file names, .svg optional)")
    ap.add_argument("--all", action="store_true", help="send every output, even those unchanged since this machine last stored them")
    ap.add_argument("--replace", action="store_true",
                    help="also replace records people have picked, edited, reviewed or commented on (kept by default)")
    ap.add_argument("--user", default=os.environ.get("PICTOGRAPHIC_USER"), help="reviewer sign-in (or PICTOGRAPHIC_PUSH_TOKEN)")
    cfg = ap.parse_args(argv)

    out_dir = cfg.out or os.path.join(OUT_DIR, cfg.set)
    files = {f if f.endswith(".svg") else f + ".svg" for f in cfg.files or []}
    found, missing, unchecked = items(cfg.set, cfg.styles, out_dir, files)
    if files and len(found) != len(files) * len(cfg.styles):
        print(f"note: {len(found)} outputs found for {len(files)} files x {len(cfg.styles)} styles")
    # Only what changed since the last run stored it (drawing or check), each with the drawing it replaces
    # (expected_sha256), so a record someone changed meanwhile is reported, not overwritten.
    manifest_path = os.path.join(out_dir, MANIFEST)
    manifest = load_manifest(manifest_path)
    if not cfg.all:
        found = [item for item in found if {k: (manifest.get(styled_key(item)) or {}).get(k) for k in ("file_sha", "check")}
                 != fingerprint(item)]
    for item in found:
        stored = manifest.get(styled_key(item))
        if stored and stored.get("svg_sha256"):
            item["expected_sha256"] = stored["svg_sha256"]
    if cfg.limit:
        found = found[:cfg.limit]
    by_key = {styled_key(item): item for item in found}
    client = Client(cfg.api, os.environ.get("PICTOGRAPHIC_PUSH_TOKEN"))
    if found and not client.token:
        if not cfg.user:
            raise SystemExit("Pass --user (a reviewer) or set PICTOGRAPHIC_PUSH_TOKEN.")
        password = os.environ.get("PICTOGRAPHIC_PASSWORD") or getpass.getpass(f"password for {cfg.user}: ")
        client.post("/api/auth/login", {"username": cfg.user, "password": password})

    total = {"created": 0, "updated": 0, "check_changed": 0, "unchanged": 0}
    errors, kept = [], []
    for i in range(0, len(found), BATCH):
        body = {"items": found[i:i + BATCH]}
        if cfg.replace:
            body["replace"] = True
        answer = client.post("/api/icons/styled", body)
        for k in total:
            total[k] += answer.get(k, 0)
        errors += answer.get("errors", [])
        kept += answer.get("kept_manual", [])
        for result in answer.get("results", []):
            item = by_key.get(result["key"])
            if item:
                manifest[result["key"]] = {**fingerprint(item), "svg_sha256": result["svg_sha256"]}
        save_manifest(manifest_path, manifest)
        print(f"  sent {min(i + BATCH, len(found))}/{len(found)} | " + ", ".join(f"{k} {v}" for k, v in total.items()) +
              f", kept {len(kept)}, errors {len(errors)}", end="\r", flush=True)
    print()
    print(f"{len(found)} outputs sent -> {cfg.api} | created {total['created']}, updated {total['updated']}, "
          f"check changed {total['check_changed']}, unchanged {total['unchanged']}, kept (people's work) {len(kept)}, "
          f"errors {len(errors)} | {len(missing)} outputs had no Worker key, {len(unchecked)} no corner check")
    for k in kept[:10]:
        print("  KEPT", k["key"], "(picked, edited, reviewed or commented on; --replace to overwrite)")
    for e in errors[:10]:
        print("  ERROR", e)
    for name in unchecked[:10]:
        print("  NO CHECK", name)
    return 1 if errors or unchecked else 0


if __name__ == "__main__":
    sys.exit(main())
