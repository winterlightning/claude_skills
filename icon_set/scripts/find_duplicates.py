#!/usr/bin/env python3
"""Find assets that are drawn identically, or nearly so.

Two detectors run over every ``*.svg`` under a root folder (default ``published/``):

1. **exact** -- the SVG geometry is normalised (title, ids, whitespace and
   colour stripped) and hashed. Files with the same hash are the same drawing
   even if they were saved under different names.
2. **similar** -- every SVG is rasterised onto a fixed square grid and turned
   into an ink mask. Two icons are scored by IoU (intersection over union of
   their ink pixels), which is reported as a percentage. 100% means the two
   renders are pixel-identical.

Rasters are cached in an ``.npz`` file so re-runs with a different threshold
are instant.

Examples::

    python icon_set/scripts/find_duplicates.py                    # >= 90 %
    python icon_set/scripts/find_duplicates.py --min 0.8 --top 200
    python icon_set/scripts/find_duplicates.py --root published/solo48 --json dups.json
    python icon_set/scripts/find_duplicates.py --within-folder    # only compare siblings
    python icon_set/scripts/find_duplicates.py --exact-only       # skip rasterising
    python icon_set/scripts/find_duplicates.py --html report.html # visual report
    python icon_set/scripts/find_duplicates.py --same-source same.csv  # drops for apply_same_source_dedupe.py
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ROOT = ROOT / "published"
DEFAULT_CACHE = ROOT / "icon_set" / "state" / "find_duplicates_cache.npz"

# ---------------------------------------------------------------- exact hash

_TITLE_RE = re.compile(r"<title>.*?</title>", re.S)
_ATTR_RE = re.compile(r'\s(?:id|class|data-[\w-]+|aria-[\w-]+)="[^"]*"')
_COLOR_RE = re.compile(r'\s(?:stroke|fill|color)="[^"]*"')
_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
_WS_RE = re.compile(r"\s+")
_NUM_RE = re.compile(r"-?\d+\.\d+")


def _round_numbers(text: str) -> str:
    # 12.0000001 and 12 are the same coordinate.
    return _NUM_RE.sub(lambda m: f"{float(m.group()):g}", text)


def normalise_svg(text: str) -> str:
    text = _COMMENT_RE.sub("", text)
    text = _TITLE_RE.sub("", text)
    text = _ATTR_RE.sub("", text)
    text = _COLOR_RE.sub("", text)
    text = _round_numbers(text)
    text = _WS_RE.sub(" ", text)
    text = text.replace("> <", "><").strip()
    return text


def geometry_hash(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    return hashlib.sha1(normalise_svg(text).encode("utf-8")).hexdigest()


# ---------------------------------------------------------------- rasterise

_CURRENT_COLOR_RE = re.compile(r"currentColor", re.I)


def rasterise(args: tuple[str, int]) -> np.ndarray:
    """Return a packed (uint8) ink mask of ``size*size`` bits for one SVG."""
    path, size = args
    try:
        import cairosvg
        from PIL import Image
        import io

        text = Path(path).read_text(encoding="utf-8", errors="replace")
        text = _CURRENT_COLOR_RE.sub("#000000", text)
        png = cairosvg.svg2png(
            bytestring=text.encode("utf-8"),
            output_width=size,
            output_height=size,
        )
        alpha = np.asarray(Image.open(io.BytesIO(png)).convert("RGBA"))[..., 3]
        mask = alpha > 127
    except Exception:  # broken SVG: treat as empty so it never matches
        mask = np.zeros((size, size), dtype=bool)
    return np.packbits(mask.ravel())


def load_or_build_rasters(
    files: list[Path], size: int, cache: Path, workers: int, quiet: bool
) -> np.ndarray:
    """Return a bool matrix (n_files, size*size). Uses/updates the cache."""
    def mtime(p: Path) -> int:
        try:
            return int(p.stat().st_mtime)
        except OSError:  # file vanished mid-run (parallel build); still hashed by path
            return -1

    keys = [f"{p}|{mtime(p)}|{size}" for p in files]
    cached: dict[str, np.ndarray] = {}
    if cache.exists():
        try:
            with np.load(cache, allow_pickle=False) as z:
                cached = dict(zip(z["keys"].tolist(), z["packed"]))
        except Exception:
            cached = {}

    todo = [(i, p) for i, (p, k) in enumerate(zip(files, keys)) if k not in cached]
    packed = [cached.get(k) for k in keys]
    if todo:
        if not quiet:
            print(f"rasterising {len(todo)} of {len(files)} files at {size}px "
                  f"({workers} workers)...", file=sys.stderr)
        with ProcessPoolExecutor(max_workers=workers) as pool:
            jobs = [(str(p), size) for _, p in todo]
            for n, (idx, result) in enumerate(
                zip((i for i, _ in todo), pool.map(rasterise, jobs, chunksize=64)), 1
            ):
                packed[idx] = result
                if not quiet and n % 5000 == 0:
                    print(f"  {n}/{len(todo)}", file=sys.stderr)
        cache.parent.mkdir(parents=True, exist_ok=True)
        keep_keys = list(cached.keys()) + [keys[i] for i, _ in todo]
        keep_packed = list(cached.values()) + [packed[i] for i, _ in todo]
        np.savez_compressed(
            cache, keys=np.array(keep_keys), packed=np.stack(keep_packed)
        )
    stacked = np.stack(packed)
    return np.unpackbits(stacked, axis=1)[:, : size * size].astype(bool)


# ---------------------------------------------------------------- similarity


def similar_pairs(
    masks: np.ndarray,
    threshold: float,
    group_of: np.ndarray | None,
    block: int = 1024,
    quiet: bool = False,
):
    """Yield (i, j, iou) for i < j with iou >= threshold.

    Uses a blocked matmul: intersection = A_block @ A.T, union from ink counts.
    """
    a = masks.astype(np.float32)
    counts = a.sum(axis=1)
    n = len(a)
    at = a.T.copy()
    for start in range(0, n, block):
        stop = min(start + block, n)
        inter = a[start:stop] @ at  # (b, n)
        union = counts[start:stop, None] + counts[None, :] - inter
        with np.errstate(divide="ignore", invalid="ignore"):
            iou = np.where(union > 0, inter / union, 0.0)
        # keep only j > i
        rows, cols = np.nonzero(iou >= threshold)
        for r, c in zip(rows, cols):
            i = start + r
            if c <= i:
                continue
            if group_of is not None and group_of[i] != group_of[c]:
                continue
            yield int(i), int(c), float(iou[r, c])
        if not quiet:
            print(f"  compared {stop}/{n}", file=sys.stderr)


def clusters(n: int, pairs) -> list[list[int]]:
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i, j in pairs:
        parent[find(i)] = find(j)
    groups: dict[int, list[int]] = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    return [g for g in groups.values() if len(g) > 1]


# ---------------------------------------------------------------- same-source drops

FAMILY_FOLDER = {"solo48": "solo", "sub32": "sub", "symbol32": "symbol", "container64": "container",
                 "combination_main48": "combination_main", "text28": "text", "text32": "text", "text44": "text"}
_SOURCE_ID_RE = re.compile(r"^SOURCE_ICON_ID\s*=\s*['\"]([^'\"]*)", re.M)
_VARIANT_RE = re.compile(r"variant_of\s*=\s*['\"]([^'\"]+)")
_PLAIN_PENALTY = re.compile(r"-v\d+\b|batch|draft|state32")


def same_source_rows(groups: list[list[str]], root: Path) -> list[dict]:
    """Drops for members of a pixel-identical group whose models resolve to one canonical primitive.

    Sources are read from each model's SOURCE_ICON_ID and resolved through
    data/primitive-aliases.json. A drop is ``blocked`` (listed, never applied) when its
    icon_id is quoted in any icon_set/data/*.json, another model is a variant of it, it holds
    a keyshape exception, or its family has no model-based discard (sub, text).
    """
    try:
        icons = json.loads((root / "gallery" / "icons.json").read_text(encoding="utf-8"))["icons"]
    except (OSError, ValueError, KeyError):
        return []
    by_key = {(x.get("family"), x.get("icon_id")): x for x in icons}
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from icon_set.scripts.primitives_catalog import load_aliases
    aliases = load_aliases()
    if not aliases:
        print("warning: no primitive aliases loaded; same-source grouping uses raw SOURCE_ICON_ID",
              file=sys.stderr)
    data_text = "".join(p.read_text(encoding="utf-8", errors="replace")
                        for p in sorted((ROOT / "icon_set" / "data").glob("*.json")))
    exceptions = ROOT / "icon_set" / "model" / "contracts" / "exceptions.v1.json"
    exceptions_text = exceptions.read_text(encoding="utf-8") if exceptions.is_file() else ""
    children: dict[str, list[str]] = defaultdict(list)
    for module in (ROOT / "icon_set" / "model" / "icons").glob("*/*.py"):
        for parent in _VARIANT_RE.findall(module.read_text(encoding="utf-8", errors="replace")):
            children[parent].append(module.name)

    def info(rel: str):
        folder, name = rel.split("/", 1)
        icon_id = name[:-4]
        rec = by_key.get((FAMILY_FOLDER.get(folder), icon_id), {})
        source = rec.get("python_source") or {}
        uid = None
        if source.get("path"):
            m = _SOURCE_ID_RE.search((ROOT / source["path"]).read_text(encoding="utf-8", errors="replace"))
            uid = (m.group(1).lower() if m else "") or None
        elif rec.get("source_ids"):
            uid = rec["source_ids"][0]
        return icon_id, rec, uid, (aliases.get(uid, uid) if uid else None)

    rows = []
    for group in groups:
        members = [(rel,) + info(rel) for rel in group]
        by_canonical: dict[str, list] = defaultdict(list)
        for rel, icon_id, rec, uid, canonical in members:
            if canonical:
                by_canonical[canonical].append((rel, icon_id, rec, uid))
        for canonical, same in by_canonical.items():
            if len(same) < 2:
                continue
            # the canonical primitive's own icon first, then the plainest, shortest name
            keep = min(same, key=lambda m: (m[3] != canonical, bool(_PLAIN_PENALTY.search(m[1])), len(m[1]), m[1]))
            for rel, icon_id, rec, uid in same:
                if rel is keep[0]:
                    continue
                family = FAMILY_FOLDER.get(rel.split("/", 1)[0], "")
                blocked = []
                if family in ("sub", "text"):
                    blocked.append(f"family {family} is not model-discarded")
                if not (rec.get("python_source") or {}).get("path"):
                    blocked.append("no python model")
                if f'"{icon_id}"' in data_text:
                    blocked.append("referenced in icon_set/data")
                if children.get(icon_id):
                    blocked.append("has variant " + children[icon_id][0])
                if f'"{icon_id}"' in exceptions_text:
                    blocked.append("keyshape exception")
                rows.append({"family": family, "keep": keep[0], "drop": rel, "drop_key": rec.get("key", ""),
                             "drop_model": (rec.get("python_source") or {}).get("path", ""),
                             "canonical_uuid": canonical, "source_icon_id": uid or "",
                             "blocked": "; ".join(blocked)})
    return rows


# ---------------------------------------------------------------- primitives map

DEFAULT_PRIMITIVES = ROOT / "published" / "gallery" / "primitives.json"
DEFAULT_GALLERY_URL = "http://localhost:8000/gallery/primitives.html"


def load_primitive_map(path: Path) -> dict[str, list[dict]]:
    """rel svg path (e.g. solo48/add.svg) -> primitives whose generated icon it is."""
    try:
        rows = json.loads(path.read_text(encoding="utf-8"))["rows"]
    except (OSError, ValueError, KeyError):
        return {}
    out: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        for gen in row.get("generated") or []:
            url = gen.get("preview_url") or ""
            rel = url[3:] if url.startswith("../") else url
            if not rel:
                continue
            out[rel].append({
                "uuid": row.get("uuid"),
                "concept": row.get("concept") or row.get("old_concept") or "",
                "category": row.get("category") or "",
                "state": row.get("state") or "",
                "key": gen.get("key") or "",
            })
    return out


def choose_keeper(group: list[str], prim: dict[str, list[dict]]) -> str:
    """Most-referenced icon wins; then the shortest, plainest file name."""
    def rank(rel: str):
        name = Path(rel).stem
        return (-len(prim.get(rel, [])), len(name), name)
    return min(group, key=rank)


def build_remap(groups: list[list[str]], prim: dict[str, list[dict]]) -> list[dict]:
    remap = []
    for g in groups:
        keep = choose_keeper(g, prim)
        remap.append({
            "keep": keep,
            "keep_primitives": prim.get(keep, []),
            "drop": [
                {"path": rel, "primitives": prim.get(rel, [])}
                for rel in g if rel != keep
            ],
        })
    return remap


# ---------------------------------------------------------------- html report

_HTML_TEMPLATE = """<title>Duplicate Icons</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{
  --bg:#f3f4f7;--surface:#ffffff;--surface-2:#e9ebf1;--line:#d5d9e3;
  --ink:#1c2130;--text:#242a3a;--muted:#6b7385;--accent:#3d5a99;--accent-ink:#ffffff;
  --exact:#2f7d5a;--near:#b5771d;--sans:"IBM Plex Sans",system-ui,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#171a22;--surface:#1f232d;--surface-2:#2a2f3b;--line:#363c4a;
  --ink:#eef0f5;--text:#e2e5ec;--muted:#98a0b3;--accent:#8fa8e0;--accent-ink:#0f1320;
  --exact:#6fc79c;--near:#e0a84a;}}
:root[data-theme="dark"]{
  --bg:#171a22;--surface:#1f232d;--surface-2:#2a2f3b;--line:#363c4a;
  --ink:#eef0f5;--text:#e2e5ec;--muted:#98a0b3;--accent:#8fa8e0;--accent-ink:#0f1320;
  --exact:#6fc79c;--near:#e0a84a;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:14px/1.45 var(--sans)}
.wrap{padding-inline:16px;padding-block:0 48px;max-width:1400px;margin:0 auto}
header{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);
  border-bottom:1px solid var(--line);padding-block:14px 12px;display:flex;flex-direction:column;gap:12px}
h1{font-size:18px;font-weight:600;margin:0;letter-spacing:-.01em}
h1 small{font-family:var(--mono);font-weight:400;color:var(--muted);font-size:12px;margin-left:10px}
.stats{display:flex;flex-wrap:wrap;gap:8px 20px;font-size:13px;color:var(--muted)}
.stats b{color:var(--text);font-variant-numeric:tabular-nums;font-weight:600}
.controls{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center}
.tabs{display:flex;gap:4px;background:var(--surface-2);padding:3px;border-radius:8px}
.tabs button{border:0;background:transparent;color:var(--muted);font:inherit;font-weight:500;
  padding:6px 12px;border-radius:6px;cursor:pointer}
.tabs button[aria-selected="true"]{background:var(--surface);color:var(--text);box-shadow:0 1px 2px rgba(0,0,0,.12)}
.tabs button:focus-visible,input:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
label.ctl{display:flex;align-items:center;gap:8px;color:var(--muted);font-size:13px}
input[type=range]{accent-color:var(--accent);width:160px}
input[type=search]{font:inherit;padding:6px 10px;border:1px solid var(--line);border-radius:6px;
  background:var(--surface);color:var(--text);min-width:200px}
#thrval{font-family:var(--mono);color:var(--text);min-width:4ch;text-align:right}
.count{color:var(--muted);font-size:13px;margin:16px 0 10px}
.count b{color:var(--text);font-variant-numeric:tabular-nums}
.group{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px;margin-bottom:10px;
  display:flex;flex-wrap:wrap;gap:12px;align-items:flex-start}
.group .n{flex:0 0 100%;font-size:12px;color:var(--muted);display:flex;gap:8px;align-items:center}
.tile{width:132px;display:flex;flex-direction:column;gap:6px}
.tile .box{width:132px;height:96px;border:1px solid var(--line);border-radius:6px;background:var(--surface-2);
  display:flex;align-items:center;justify-content:center;color:var(--ink)}
.tile .box svg{width:64px;height:64px}
.tile .path{font-family:var(--mono);font-size:11px;line-height:1.35;color:var(--text);word-break:break-all}
.fam{display:inline-block;font-family:var(--mono);font-size:10px;letter-spacing:.04em;text-transform:uppercase;
  color:var(--muted);border:1px solid var(--line);border-radius:4px;padding:1px 5px}
.pairs{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:10px}
.pair{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px;
  display:grid;grid-template-columns:132px 1fr 132px;gap:10px;align-items:start}
.pair .score{align-self:center;text-align:center;font-family:var(--mono);font-size:15px;font-weight:500;
  font-variant-numeric:tabular-nums}
.pair .score.full{color:var(--exact)}.pair .score.near{color:var(--near)}
.pair .score span{display:block;font-size:10px;color:var(--muted);letter-spacing:.06em;text-transform:uppercase;margin-top:4px}
.more{display:block;margin:16px auto 0;font:inherit;font-weight:500;padding:8px 18px;border-radius:8px;
  border:1px solid var(--line);background:var(--surface);color:var(--accent);cursor:pointer}
.empty{color:var(--muted);padding:32px 0;text-align:center}
.tile.keep .box{border-color:var(--exact);box-shadow:inset 0 0 0 1px var(--exact)}
.keepmark{display:inline-block;font-family:var(--mono);font-size:10px;letter-spacing:.06em;text-transform:uppercase;
  color:var(--exact);border:1px solid var(--exact);border-radius:4px;padding:1px 5px}
.prims{font-size:11px;line-height:1.35;color:var(--muted);display:flex;flex-direction:column;gap:2px}
.prims a{color:var(--accent);text-decoration:none}.prims a:hover{text-decoration:underline}
.prims .cat{color:var(--muted)}
.famtab{display:flex;flex-wrap:wrap;gap:6px 18px;font-family:var(--mono);font-size:12px;color:var(--muted);
  font-variant-numeric:tabular-nums}
.famtab b{color:var(--text);font-weight:500}
.legend{font-size:12px;color:var(--muted);margin-top:-2px}
@media (max-width:420px){.pair{grid-template-columns:1fr 1fr}.pair .score{grid-column:1/-1;order:-1}
  .tile,.tile .box{width:100%}}
@media (prefers-reduced-motion:no-preference){.tabs button{transition:background .15s}}
</style>
<div class="wrap">
<header>
  <h1>Duplicate Icons <small id="root"></small></h1>
  <div class="stats" id="stats"></div>
  <div class="famtab" id="famtab"></div>
  <div class="legend">Outlined tile = suggested keeper (most primitives linked, then shortest name). Concept links open the primitive in the review page.</div>
  <div class="controls">
    <div class="tabs" role="tablist">
      <button role="tab" id="tab-similar" data-tab="similar" aria-selected="true">Similar pairs</button>
      <button role="tab" id="tab-pixel" data-tab="pixel">Pixel-identical</button>
      <button role="tab" id="tab-exact" data-tab="exact">Same geometry</button>
    </div>
    <label class="ctl" id="thr-wrap">Min IoU <input type="range" id="thr" min="0" max="100" step="1"> <span id="thrval"></span></label>
    <input type="search" id="q" placeholder="Filter by path">
  </div>
</header>
<div class="count" id="count"></div>
<div id="out"></div>
</div>
<script>
const DATA = __DATA__;
const ICONS = DATA.files;
const PAGE = 300;
const state = {tab:'similar', thr: DATA.min_iou, q:'', shown: PAGE};
const $ = id => document.getElementById(id);
$('root').textContent = DATA.root;
$('stats').innerHTML =
  `<span><b>${DATA.n_files.toLocaleString()}</b> svg files</span>` +
  `<span><b>${DATA.exact.length}</b> same-geometry groups</span>` +
  `<span><b>${DATA.pixel.length}</b> pixel-identical groups at ${DATA.size}px</span>` +
  `<span><b>${DATA.pairs.length.toLocaleString()}</b> pairs at ≥ ${Math.round(DATA.min_iou*100)}%</span>`;
const thr = $('thr'); thr.min = Math.round(DATA.min_iou*100); thr.value = thr.min;
const fam = p => p.includes('/') ? p.slice(0, p.indexOf('/')) : '';
const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
function tile(p, markKeep){
  const f = fam(p), keep = markKeep && KEEP.has(p);
  return `<div class="tile${keep?' keep':''}"><div class="box">${ICONS[p]||''}</div>` +
    `<div class="path">${keep?'<span class="keepmark">keep</span> ':''}${f?`<span class="fam">${esc(f)}</span> `:''}${esc(f?p.slice(f.length+1):p)}</div>` +
    prims(p) + `</div>`;
}
function groupHtml(g, markKeep){
  const nprim = g.reduce((n,p) => n + ((DATA.prim[p]||[]).length), 0);
  return `<div class="group"><div class="n"><b>${g.length}</b> files` +
    (nprim ? ` \u00b7 ${nprim} primitive${nprim>1?'s':''}` : '') + `</div>${g.map(p => tile(p, markKeep)).join('')}</div>`;
}
function pairHtml([a,b,s]){
  const pct = s>=0.9999 ? '100%' : (s*100).toFixed(1)+'%';
  return `<div class="pair">${tile(a)}<div class="score ${s>=0.9999?'full':'near'}">${pct}<span>IoU</span></div>${tile(b)}</div>`;
}
function render(){
  const q = state.q.toLowerCase();
  const hit = p => !q || p.toLowerCase().includes(q) ||
    (DATA.prim[p]||[]).some(x => (x.concept+' '+x.uuid+' '+x.category).toLowerCase().includes(q));
  let items, html, label;
  if (state.tab === 'similar'){
    items = DATA.pairs.filter(([a,b,s]) => s >= state.thr - 1e-9 && (hit(a)||hit(b)));
    label = 'pairs';
    html = `<div class="pairs">${items.slice(0,state.shown).map(pairHtml).join('')}</div>`;
  } else {
    items = (state.tab==='pixel' ? DATA.pixel : DATA.exact).filter(g => g.some(hit));
    label = 'groups';
    html = items.slice(0,state.shown).map(g => groupHtml(g, state.tab==='pixel')).join('');
  }
  $('count').innerHTML = `<b>${items.length.toLocaleString()}</b> ${label}` +
    (items.length > state.shown ? `, showing first ${state.shown}` : '');
  $('out').innerHTML = items.length ? html +
    (items.length > state.shown ? `<button class="more" id="more">Show ${Math.min(PAGE, items.length-state.shown)} more</button>` : '')
    : `<div class="empty">Nothing matches.</div>`;
  const more = $('more'); if (more) more.onclick = () => { state.shown += PAGE; render(); };
  $('thr-wrap').hidden = state.tab !== 'similar';
  $('thrval').textContent = Math.round(state.thr*100)+'%';
}
document.querySelectorAll('.tabs button').forEach(b => b.onclick = () => {
  document.querySelectorAll('.tabs button').forEach(x => x.setAttribute('aria-selected', x===b));
  state.tab = b.dataset.tab; state.shown = PAGE; render();
});
thr.oninput = () => { state.thr = thr.value/100; state.shown = PAGE; render(); };
$('q').oninput = () => { state.q = $('q').value.trim(); state.shown = PAGE; render(); };
render();
</script>
"""


def write_html(out: Path, root: Path, rel: list[str], report: dict) -> None:
    """Write a self-contained HTML report with every referenced icon inlined."""
    needed: set[str] = set()
    for g in report["exact_groups"]:
        needed.update(g)
    for g in report.get("pixel_identical_groups", []):
        needed.update(g)
    for p in report.get("similar_pairs", []):
        needed.add(p["a"]); needed.add(p["b"])
    files = {}
    for r in sorted(needed):
        try:
            svg = (root / r).read_text(encoding="utf-8", errors="replace")
        except OSError:
            svg = ""
        svg = _COMMENT_RE.sub("", svg)
        svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
        svg = re.sub(r"<!DOCTYPE[^>]*>", "", svg)
        files[r] = svg.strip()
    data = {
        "root": str(root),
        "n_files": report["files"],
        "size": report.get("size"),
        "min_iou": report.get("min_iou", 1.0),
        "exact": report["exact_groups"],
        "pixel": report.get("pixel_identical_groups", []),
        "pairs": [[p["a"], p["b"], p["iou"]] for p in report.get("similar_pairs", [])],
        "files": files,
        "unique": report.get("unique_at_100"),
        "per_family": report.get("per_family", {}),
        "keep": [e["keep"] for e in report.get("remap", [])],
        "prim": report.get("primitives", {}),
        "gallery_url": report.get("gallery_url", ""),
    }
    blob = json.dumps(data, separators=(",", ":")).replace("</", "<\\/")
    out.write_text(_HTML_TEMPLATE.replace("__DATA__", blob), encoding="utf-8")


# ---------------------------------------------------------------- main


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT,
                    help="folder to scan recursively for *.svg")
    ap.add_argument("--min", type=float, default=0.90,
                    help="report pairs with IoU >= this fraction (default 0.90)")
    ap.add_argument("--identical", type=float, default=0.9999,
                    help="IoU at or above which two icons count as the same drawing for the "
                         "identical groups, --remap and --same-source (default 0.9999)")
    ap.add_argument("--size", type=int, default=32,
                    help="raster grid in px (default 32; 48 is stricter/slower)")
    ap.add_argument("--within-folder", action="store_true",
                    help="only compare files that sit in the same folder")
    ap.add_argument("--exact-only", action="store_true",
                    help="only run the geometry-hash detector (no rasterising)")
    ap.add_argument("--top", type=int, default=0,
                    help="print at most N similar pairs (0 = all)")
    ap.add_argument("--json", type=Path, help="also write the full report here")
    ap.add_argument("--csv", type=Path, help="also write similar pairs as CSV")
    ap.add_argument("--html", type=Path,
                    help="also write a self-contained visual report (icons inlined)")
    ap.add_argument("--primitives", type=Path, default=DEFAULT_PRIMITIVES,
                    help="gallery/primitives.json used to map icons back to their "
                         "source primitives (pass an empty string to skip)")
    ap.add_argument("--gallery-url", default=DEFAULT_GALLERY_URL,
                    help="review page that links in the HTML report get pointed at")
    ap.add_argument("--remap", type=Path,
                    help="write a CSV of 100%% duplicates: drop -> keep, with primitives")
    ap.add_argument("--same-source", type=Path, metavar="CSV",
                    help="write drops for 100%% duplicates whose models share one canonical primitive "
                         "(input for apply_same_source_dedupe.py)")
    ap.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 4)
    ap.add_argument("--exclude", action="append", default=[],
                    help="substring of a path to skip (repeatable); hidden "
                         "folders such as .icon-build-* are always skipped")
    ap.add_argument("-q", "--quiet", action="store_true")
    args = ap.parse_args(argv)

    files = sorted(
        p for p in args.root.rglob("*.svg")
        if not any(part.startswith(".") for part in p.relative_to(args.root).parts)
        and not any(x in str(p) for x in args.exclude)
        and p.is_file()
    )
    if not files:
        print(f"no .svg files under {args.root}", file=sys.stderr)
        return 1
    rel = [str(p.relative_to(args.root)) for p in files]
    if not args.quiet:
        print(f"{len(files)} svg files under {args.root}", file=sys.stderr)

    # 1. exact geometry duplicates
    by_hash: dict[str, list[int]] = defaultdict(list)
    for i, p in enumerate(files):
        h = geometry_hash(p)
        if h:
            if args.within_folder:
                h = f"{p.parent}|{h}"
            by_hash[h].append(i)
    exact_groups = sorted(
        (v for v in by_hash.values() if len(v) > 1), key=len, reverse=True
    )

    report = {
        "root": str(args.root),
        "files": len(files),
        "exact_groups": [[rel[i] for i in g] for g in exact_groups],
    }

    print(f"# exact duplicates (same geometry): {len(exact_groups)} groups, "
          f"{sum(len(g) for g in exact_groups)} files")
    for g in exact_groups:
        print(f"  [{len(g)}]")
        for i in g:
            print(f"    {rel[i]}")

    if args.exact_only:
        if args.json:
            args.json.write_text(json.dumps(report, indent=2))
        if args.html:
            write_html(args.html, args.root, rel, report)
            print(f"wrote {args.html}", file=sys.stderr)
        return 0

    # 2. pixel similarity
    masks = load_or_build_rasters(files, args.size, args.cache, args.workers, args.quiet)
    group_of = None
    if args.within_folder:
        folders = {p.parent for p in files}
        ids = {f: k for k, f in enumerate(sorted(folders))}
        group_of = np.array([ids[p.parent] for p in files])

    if not args.quiet:
        print("comparing...", file=sys.stderr)
    pairs = list(similar_pairs(masks, args.min, group_of, quiet=args.quiet))
    pairs.sort(key=lambda t: -t[2])

    if args.identical < args.min:
        ap.error("--identical must be at least --min")
    pixel_identical = clusters(len(files), ((i, j) for i, j, s in pairs if s >= args.identical))
    pixel_identical.sort(key=len, reverse=True)

    print(f"\n# same drawing (IoU >= {args.identical:.2%}) at {args.size}px: {len(pixel_identical)} groups, "
          f"{sum(len(g) for g in pixel_identical)} files")
    for g in pixel_identical:
        print(f"  [{len(g)}]")
        for i in g:
            print(f"    {rel[i]}")

    removable = sum(len(g) - 1 for g in pixel_identical)
    per_family: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for r in rel:
        per_family[r.split("/")[0] if "/" in r else "."][0] += 1
    for g in pixel_identical:
        for i in g[1:]:
            per_family[rel[i].split("/")[0] if "/" in rel[i] else "."][1] += 1
    print(f"\n# unique drawings at 100% IoU: {len(files) - removable} "
          f"({len(files)} files - {removable} duplicates)")
    for fam, (n, d) in sorted(per_family.items()):
        print(f"  {fam:14s} {n:6d} files  -{d:4d} dup  = {n - d:6d} unique")

    prim: dict[str, list[dict]] = {}
    if args.primitives and str(args.primitives):
        prim = load_primitive_map(args.primitives)
        if not prim:
            print(f"warning: no primitive links read from {args.primitives}", file=sys.stderr)
    remap = build_remap([[rel[i] for i in g] for g in pixel_identical], prim)
    if args.remap:
        with args.remap.open("w") as fh:
            fh.write("family,drop,keep,primitive_uuid,concept,category,state\n")
            for entry in remap:
                for d in entry["drop"]:
                    fam = d["path"].split("/")[0]
                    prims = d["primitives"] or [{}]
                    for pr in prims:
                        cells = [fam, d["path"], entry["keep"], pr.get("uuid", ""),
                                 pr.get("concept", ""), pr.get("category", ""), pr.get("state", "")]
                        fh.write(",".join('"' + str(c).replace('"', '""') + '"' for c in cells) + "\n")
        print(f"wrote {args.remap}", file=sys.stderr)

    if args.same_source:
        rows_ss = same_source_rows([[rel[i] for i in g] for g in pixel_identical], args.root)
        with args.same_source.open("w", newline="") as fh:
            import csv
            fields = ["family", "keep", "drop", "drop_key", "drop_model", "canonical_uuid", "source_icon_id", "blocked"]
            writer = csv.DictWriter(fh, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows_ss)
        ok = [r for r in rows_ss if not r["blocked"]]
        print(f"\n# same-source drops: {len(ok)} applicable, {len(rows_ss) - len(ok)} blocked "
              f"-> {args.same_source}")
        for fam, n in sorted(Counter(r["family"] for r in ok).items()):
            print(f"  {fam:8s} {n}")

    shown = pairs if not args.top else pairs[: args.top]
    print(f"\n# similar pairs (IoU >= {args.min:.0%}): {len(pairs)} pairs"
          + (f", showing {len(shown)}" if args.top and len(pairs) > args.top else ""))
    for i, j, s in shown:
        print(f"  {s:6.1%}  {rel[i]}  <->  {rel[j]}")

    empty = int((masks.sum(axis=1) == 0).sum())
    if empty:
        print(f"\n# {empty} files rendered empty (broken or blank) and were ignored")

    referenced: set[str] = set()
    for g in report["exact_groups"]:
        referenced.update(g)
    for g in pixel_identical:
        referenced.update(rel[i] for i in g)
    for i, j, _ in pairs:
        referenced.add(rel[i]); referenced.add(rel[j])
    report.update({
        "size": args.size,
        "min_iou": args.min,
        "pixel_identical_groups": [[rel[i] for i in g] for g in pixel_identical],
        "similar_pairs": [
            {"a": rel[i], "b": rel[j], "iou": round(s, 4)} for i, j, s in pairs
        ],
        "empty": [rel[i] for i in np.nonzero(masks.sum(axis=1) == 0)[0]],
        "unique_at_100": len(files) - removable,
        "per_family": {k: {"files": v[0], "duplicates": v[1], "unique": v[0] - v[1]}
                       for k, v in sorted(per_family.items())},
        "remap": remap,
        "primitives": {r: prim[r] for r in prim if r in referenced},
        "gallery_url": args.gallery_url,
    })
    if args.json:
        args.json.write_text(json.dumps(report, indent=2))
        print(f"\nwrote {args.json}", file=sys.stderr)
    if args.csv:
        with args.csv.open("w") as fh:
            fh.write("iou,a,b\n")
            for i, j, s in pairs:
                fh.write(f"{s:.4f},{rel[i]},{rel[j]}\n")
        print(f"wrote {args.csv}", file=sys.stderr)
    if args.html:
        write_html(args.html, args.root, rel, report)
        print(f"wrote {args.html}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
