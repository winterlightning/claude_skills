"""Persistent preview results, isolated from artwork and review approval state."""
import hashlib
import json
import sqlite3
from contextlib import closing
from pathlib import Path
from collections import Counter
from functools import lru_cache
from threading import RLock

_snapshot_lock = RLock()
from .latest_container_combinations import LatestContainerPairs


def service(root, data_root):
    return LatestContainerPairs(root, data_root)


def snapshot(root, data_root):
    root, data_root = Path(root), Path(data_root)
    paths = [root/p for p in ("gallery/combinations.json", "gallery/icons.json", "container64/manifest.json", "symbol32/manifest.json")]
    paths += [data_root/p for p in ("container-content-areas.json", "container-placement-preferences.json")]
    stamps = tuple((p.stat().st_mtime_ns, p.stat().st_size) for p in paths)
    with _snapshot_lock:
        return _snapshot(str(root.resolve()), str(data_root.resolve()), stamps)


@lru_cache(maxsize=4)
def _snapshot(root, data_root, stamps):
    root, data_root = Path(root), Path(data_root)
    catalog = json.loads((root/"gallery/combinations.json").read_text())
    gallery = json.loads((root/"gallery/icons.json").read_text())
    metadata = [{k:r.get(k) for k in ("key", "variant_of", "variant_root", "created_at")}
                for r in gallery["icons"] if r.get("family") in ("container", "symbol")]
    pairs = []
    for row in catalog["rows"]:
        if row["kind"] != "container": continue
        refs=catalog["references"]
        pair={k:row.get(k) for k in ("id", "main_id", "sub_id", "concept", "main_icon_id")}
        for role, family in (("main", "container"), ("sub", "symbol")):
            choices=row.get(role+"_generated", refs[row[role+"_id"]].get("generated", []))
            pair[role]=sorted(g.get("key",family+"/"+g["icon_id"]) for g in choices
                              if g.get("key",family+"/").startswith(family+"/"))
        pairs.append(pair)
    payload=[sorted(pairs,key=lambda r:r["id"]),sorted(metadata,key=lambda r:r["key"])]
    for path in (root/"container64/manifest.json",root/"symbol32/manifest.json",
                 data_root/"container-content-areas.json",data_root/"container-placement-preferences.json"):
        payload.append(json.loads(path.read_text()))
    return hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(",",":")).encode()).hexdigest()


def connect(state_root):
    path = Path(state_root)/"container-combinations.sqlite3"
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path, timeout=30)
    db.execute("CREATE TABLE IF NOT EXISTS previews (id TEXT PRIMARY KEY, snapshot TEXT, result TEXT)")
    return db


def public(pair):
    return {k:v for k,v in pair.items() if k != "svg"}


def combine(root, data_root, state_root, query):
    stamp = snapshot(root, data_root)
    expected = query.pop("snapshot", [stamp])[0]
    if expected != stamp:
        raise ValueError("The catalog changed. Start Combine all pairs again.")
    result = service(root, data_root).response(query)
    if snapshot(root, data_root) != stamp:
        raise ValueError("The catalog changed during processing. Start again.")
    with closing(connect(state_root)) as db, db:
        db.executemany("INSERT OR REPLACE INTO previews VALUES (?,?,?)",
                       [(p["pair_id"], stamp, json.dumps(p)) for p in result["pairs"]])
    return dict(result, snapshot=stamp, pairs=[public(p) for p in result["pairs"]])


def listing(root, data_root, state_root):
    stamp = snapshot(root, data_root)
    s = service(root, data_root)
    containers, symbols = {}, {}
    selections = {}
    rows = [r for r in s.catalog["rows"] if r["kind"] == "container"]
    for row in rows:
        refs = s.catalog["references"]
        main = s.latest(row.get("main_generated", refs[row["main_id"]].get("generated", [])), "container", "32")
        sub = s.latest(row.get("sub_generated", refs[row["sub_id"]].get("generated", [])), "symbol", "32")
        selections[row["id"]] = dict(main_key=main["key"] if main else None, symbol_key=sub["key"] if sub else None)
        key = main["key"] if main else (row.get("main_icon_id") or row["main_id"])
        containers[key] = containers.get(key, False) or bool(main)
        symbols[row["sub_id"]] = symbols.get(row["sub_id"], False) or bool(sub)
    with closing(connect(state_root)) as db:
        pairs = [public(json.loads(r[0])) for r in db.execute("SELECT result FROM previews WHERE snapshot=? ORDER BY id", (stamp,))]
    return dict(snapshot=stamp, total=len(rows), processed=len(pairs),
                counts=dict(Counter(p["status"] for p in pairs)), pairs=pairs, selections=selections,
                containers=dict(total=len(containers), ready=sum(containers.values()), missing=sum(not x for x in containers.values())),
                symbols=dict(total=len(symbols), ready=sum(symbols.values()), missing=sum(not x for x in symbols.values())))


def saved_svg(root, data_root, state_root, uid):
    if not (Path(state_root)/"container-combinations.sqlite3").exists():
        return None
    with closing(connect(state_root)) as db:
        row = db.execute("SELECT result FROM previews WHERE id=? AND snapshot=?", (uid, snapshot(root, data_root))).fetchone()
    return json.loads(row[0]).get("svg") if row else None
