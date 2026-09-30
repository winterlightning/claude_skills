#!/usr/bin/env python3
"""Turn `claude -p --output-format stream-json --verbose` into a live, readable log.

Reads the JSON event stream on stdin and prints one line per tool call, the
assistant's text as it arrives, and the final result, flushing every line so
`tail -f <run>/claude.log` shows progress while the redraw is running.
"""
import json
import sys
import time


def short(value, limit=160):
    text = " ".join(str(value).split())
    return text if len(text) <= limit else text[: limit - 3] + "..."


for raw in sys.stdin:
    try:
        event = json.loads(raw)
    except ValueError:
        print(raw.rstrip(), flush=True)
        continue
    stamp = time.strftime("%H:%M:%S")
    kind = event.get("type")
    if kind == "assistant":
        for block in event.get("message", {}).get("content", []):
            if block.get("type") == "text" and block.get("text", "").strip():
                print(f"[{stamp}] {block['text'].strip()}", flush=True)
            elif block.get("type") == "tool_use":
                args = block.get("input", {})
                detail = (args.get("description") or args.get("command")
                          or args.get("file_path") or args.get("skill") or args)
                print(f"[{stamp}] > {block.get('name')}: {short(detail)}", flush=True)
    elif kind == "result":
        cost = event.get("total_cost_usd")
        secs = (event.get("duration_ms") or 0) / 1000
        print(f"\n[{stamp}] === {event.get('subtype')} in {secs:.0f}s"
              + (f", ${cost:.2f}" if cost is not None else "") + " ===", flush=True)
        if event.get("result"):
            print(event["result"], flush=True)
