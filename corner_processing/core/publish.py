#!/usr/bin/env python3
"""core/publish.py — store the round and sharp outputs as icon records on the review site.

Each output becomes `<key>--round` / `<key>--sharp`, its own icon in the source's family with style round or sharp
(Worker POST /api/icons/styled, migration 0019). New drawings start Ready; an icon whose corner check failed is a
failed build. Sending the same drawing again changes nothing, so a re-run only sends what changed.

  python3 -m core.publish --user jakes                      # outputs/solo48 -> production, password asked
  python3 -m core.publish --styles round --limit 50         # a first few
  PICTOGRAPHIC_PUSH_TOKEN=... python3 -m core.publish       # or the push token instead of a sign-in

Reads input/<set>/icons.csv (file name -> Worker key) and outputs/<set>/toggle.json (each icon's check).
"""

import argparse
import csv
import getpass
import http.cookiejar
import json
import os
import sys
import urllib.request

from .fetch import API
from .paths import INPUT_DIR, OUT_DIR, SETS

BATCH = 25             # icons per request (the route takes up to 50)


class Client:
    def __init__(self, api, token=None):
        self.api, self.token = api.rstrip("/"), token
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

    def post(self, path, body):
        headers = {"Content-Type": "application/json", "User-Agent": "corner48-publish/1.0"}  # Cloudflare 403s urllib's UA
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        req = urllib.request.Request(self.api + path, data=json.dumps(body).encode(), headers=headers, method="POST")
        try:
            with self.opener.open(req, timeout=120) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            raise SystemExit(f"{path}: HTTP {e.code} {e.read().decode(errors='replace')[:300]}")


def items(set_name, styles, out_dir):
    """(source_key, style, svg, check) for every output that has a Worker key."""
    with open(os.path.join(INPUT_DIR, set_name, "icons.csv"), encoding="utf-8") as f:
        keys = {os.path.basename(r["file"]): r["key"] for r in csv.DictReader(f)}
    with open(os.path.join(out_dir, "toggle.json"), encoding="utf-8") as f:
        toggles = json.load(f)["icons"]
    found, missing = [], []
    for style in styles:
        folder = os.path.join(out_dir, style)
        for name in sorted(os.listdir(folder)):
            if not name.endswith(".svg"):
                continue
            if name not in keys:
                missing.append(f"{style}/{name}")
                continue
            check = ((toggles.get(name) or {}).get(style) or {}).get("check", {}).get("status") or "ok"
            with open(os.path.join(folder, name), encoding="utf-8") as f:
                found.append({"source_key": keys[name], "style": style, "svg": f.read(), "check": check})
    return found, missing


def main(argv=None):
    ap = argparse.ArgumentParser(description="Store the round and sharp outputs as icon records (style round / sharp).")
    ap.add_argument("--api", default=API)
    ap.add_argument("--set", default=SETS["solo"], help="input/outputs set folder (default: %(default)s)")
    ap.add_argument("--out", help="outputs folder (default: outputs/<set>)")
    ap.add_argument("--styles", nargs="+", choices=("round", "sharp"), default=["round", "sharp"])
    ap.add_argument("--limit", type=int, default=0, help="send only the first N items (a trial)")
    ap.add_argument("--user", default=os.environ.get("PICTOGRAPHIC_USER"), help="reviewer sign-in (or PICTOGRAPHIC_PUSH_TOKEN)")
    cfg = ap.parse_args(argv)

    found, missing = items(cfg.set, cfg.styles, cfg.out or os.path.join(OUT_DIR, cfg.set))
    if cfg.limit:
        found = found[:cfg.limit]
    client = Client(cfg.api, os.environ.get("PICTOGRAPHIC_PUSH_TOKEN"))
    if not client.token:
        if not cfg.user:
            raise SystemExit("Pass --user (a reviewer) or set PICTOGRAPHIC_PUSH_TOKEN.")
        password = os.environ.get("PICTOGRAPHIC_PASSWORD") or getpass.getpass(f"password for {cfg.user}: ")
        client.post("/api/auth/login", {"username": cfg.user, "password": password})

    total = {"created": 0, "updated": 0, "unchanged": 0}
    errors = []
    for i in range(0, len(found), BATCH):
        answer = client.post("/api/icons/styled", {"items": found[i:i + BATCH]})
        for k in total:
            total[k] += answer.get(k, 0)
        errors += answer.get("errors", [])
        print(f"  sent {min(i + BATCH, len(found))}/{len(found)} | " + ", ".join(f"{k} {v}" for k, v in total.items()) +
              f", errors {len(errors)}", end="\r", flush=True)
    print()
    print(f"{len(found)} outputs -> {cfg.api} | created {total['created']}, updated {total['updated']}, "
          f"unchanged {total['unchanged']}, errors {len(errors)} | {len(missing)} outputs had no Worker key")
    for e in errors[:10]:
        print("  ERROR", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
