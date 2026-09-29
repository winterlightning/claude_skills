#!/usr/bin/env python3
"""Serve output_png/report.html locally and save Like / No verdicts to output_png/verdicts.json.

Usage: python3 new-pipeline-test/serve_report.py [--port 8766] [--build]
Then open http://localhost:8766/report.html. Each click on Like / No is written to
verdicts.json right away ({run dir: {verdict, subject, icon_key, at, claim...}}).
claim_liked.py reads that file to claim and upload the liked runs on the Worker.
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE / "output_png"
VERDICTS = ROOT / "verdicts.json"


def normalize(data):
    """Accept the report's Export download (a list of rows) as well as the dict this server writes."""
    if isinstance(data, list):
        return {r["run"]: {"verdict": r.get("verdict", ""), "subject": r.get("subject", ""),
                           "icon_key": r.get("icon_key", "")} for r in data if r.get("run")}
    return data if isinstance(data, dict) else {}


def load():
    try:
        return normalize(json.loads(VERDICTS.read_text()))
    except (OSError, ValueError):
        return {}


def save(data):
    tmp = VERDICTS.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    tmp.replace(VERDICTS)


class Handler(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        if "/api/" in (args[0] if args else ""):
            super().log_message(fmt, *args)

    def send_json(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.split("?")[0] == "/api/verdicts":
            return self.send_json(200, {run: v["verdict"] for run, v in load().items() if v.get("verdict")})
        return super().do_GET()

    def do_POST(self):
        if self.path.split("?")[0] != "/api/verdict":
            return self.send_json(404, {"error": "unknown route"})
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
        except ValueError:
            return self.send_json(400, {"error": "bad json"})
        run, verdict = str(body.get("run") or ""), str(body.get("verdict") or "")
        if not run or "/" in run or verdict not in ("", "like", "dislike"):
            return self.send_json(400, {"error": "run and verdict (like, dislike or empty) required"})
        data = load()
        entry = data.get(run, {})
        if verdict:
            entry.update({"verdict": verdict, "subject": body.get("subject") or entry.get("subject", ""),
                          "icon_key": body.get("icon_key") or entry.get("icon_key", ""),
                          "at": datetime.now(timezone.utc).isoformat()})
            data[run] = entry
        elif entry.get("claim"):
            entry["verdict"] = ""  # keep the claim record, just drop the verdict
        else:
            data.pop(run, None)
        save(data)
        self.send_json(200, {"ok": True, "run": run, "verdict": verdict})


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--port", type=int, default=8766)
    ap.add_argument("--build", action="store_true", help="rebuild report.html first")
    args = ap.parse_args()
    if args.build:
        subprocess.run([sys.executable, str(HERE / "build_report.py")], check=True)
    server = ThreadingHTTPServer(("127.0.0.1", args.port), partial(Handler, directory=str(ROOT)))
    print(f"report: http://localhost:{args.port}/report.html\nverdicts: {VERDICTS}\nctrl-c to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
