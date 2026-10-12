#!/usr/bin/env python3
"""serve_report.py — serve the review pages locally so LOCK IN saves to the project.

A page opened straight from disk (file://) cannot write files, so its locks only live in that
browser. Served by this script, the toggle page's Lock in / Unlock / Accept buttons save to
locks.json (see core/locks.py), where every pipeline run checks them.

  python3 reports/serve_report.py                 # http://127.0.0.1:8748/toggle48_report.html
  python3 reports/serve_report.py --port 9000 --no-open

Local only (binds 127.0.0.1). API used by the page:
  GET  /api/locks                         -> {name: {fp, at}}
  POST /api/locks  {"name", "action": "lock"|"pending"|"unlock", "fp": {input, round, sharp}}
  POST /api/locks  {"action": "lock_many"|"pending_many"|"unlock_many", "items": [{"name", "fp"}]}
  (lock = reviewed OK, pending = reviewed not OK, unlock = back to ready)
  POST /api/picks  {"page", "picks": {...}}  -> saves picks/<page>.json in the served folder (picker pages)
"""

import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))   # corner_processing/: import core
import argparse
import json
import os
import sys
import threading
import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

from core import locks
from _shared import default_dir

HERE = os.path.dirname(os.path.abspath(__file__))
_lock = threading.Lock()          # one writer at a time


class Handler(SimpleHTTPRequestHandler):
    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.split("?")[0] == "/api/locks":
            with _lock:
                return self._json(200, locks.load())
        return super().do_GET()

    def do_POST(self):
        if self.path.split("?")[0] == "/api/picks":
            try:
                req = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
                page = "".join(c for c in str(req["page"]) if c.isalnum() or c in "-_")
                assert page and isinstance(req["picks"], dict)
            except (ValueError, KeyError, AssertionError):
                return self._json(400, {"error": "need JSON with page and picks"})
            with _lock:
                os.makedirs(os.path.join(self.directory, "picks"), exist_ok=True)
                with open(os.path.join(self.directory, "picks", page + ".json"), "w") as f:
                    json.dump(req["picks"], f, indent=1)
            return self._json(200, {"saved": len(req["picks"])})
        if self.path.split("?")[0] != "/api/locks":
            return self._json(404, {"error": "not found"})
        try:
            n = int(self.headers.get("Content-Length") or 0)
            req = json.loads(self.rfile.read(n) or b"{}")
            action = req["action"]
            name = req.get("name") if action.endswith("_many") else req["name"]
        except (ValueError, KeyError):
            return self._json(400, {"error": "need JSON with name and action"})
        with _lock:
            cur = locks.load()
            if action in ("lock", "pending"):
                fp = req.get("fp")
                if not isinstance(fp, dict) or set(fp) != set(locks.PARTS):
                    return self._json(400, {"error": f"{action} needs fp with input, round, sharp"})
                locks.lock(cur, name, fp, req.get("note", ""),
                           "pending" if action == "pending" else "locked")
            elif action == "unlock":
                cur.pop(name, None)
            elif action in ("lock_many", "pending_many", "unlock_many"):
                items = req.get("items")
                if not isinstance(items, list) or not all(
                        isinstance(it, dict) and "name" in it and (action == "unlock_many" or (
                            isinstance(it.get("fp"), dict) and set(it["fp"]) == set(locks.PARTS)))
                        for it in items):
                    return self._json(400, {"error": f"{action} needs items [{{name, fp}}]"})
                for it in items:
                    if action != "unlock_many":
                        locks.lock(cur, it["name"], it["fp"],
                                   status="pending" if action == "pending_many" else "locked")
                    else:
                        cur.pop(it["name"], None)
            else:
                return self._json(400, {"error": "action must be lock, pending, unlock or *_many"})
            locks.save(cur)
            return self._json(200, cur)

    def log_message(self, fmt, *args):          # keep the terminal quiet except for API calls
        if "/api/" in (args[0] if args else ""):
            sys.stderr.write("  " + (fmt % args) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Serve the review pages with saving locks.")
    ap.add_argument("--port", type=int, default=8748)
    ap.add_argument("--dir", help="the folder with the pages (default: outputs/solo48 or outputs/, whichever ran last)")
    ap.add_argument("--no-open", action="store_true")
    ap.add_argument("--locks", help="lock file to use (default: locks.json next to the scripts)")
    cfg = ap.parse_args(argv)
    cfg.dir = cfg.dir or default_dir()
    if cfg.locks:
        locks.LOCKS_PATH = os.path.abspath(cfg.locks)
    srv = ThreadingHTTPServer(("127.0.0.1", cfg.port), partial(Handler, directory=cfg.dir))
    url = f"http://127.0.0.1:{cfg.port}/toggle48_report.html"
    print(f"serving {cfg.dir}\n  {url}\n  locks -> {locks.LOCKS_PATH}\n  Ctrl+C to stop")
    if not cfg.no_open:
        webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
