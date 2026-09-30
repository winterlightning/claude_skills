"""Local report of container pairs whose symbol is text, from icon_set/data/container-text-v2.json.

    /opt/homebrew/bin/python3 -m icon_set.scripts.container_text_report
    open http://127.0.0.1:8801/gallery/container-text-report.html

Each row shows the original pair, the container artwork, the text rendered with
typeface v2 (native size, translation only) and the symbol currently drawn for it.
"""
from __future__ import annotations
import html
import json
from pathlib import Path
from .side_text import glyph_map, native_text
from .workspace import REPO_ROOT

DATA = REPO_ROOT/'icon_set/data/container-text-v2.json'
GALLERY = REPO_ROOT/'published/gallery'
OUTPUT = GALLERY/'container-text-report.html'
SPACE_ADVANCE = 4  # provisional: the typeface has no space glyph yet


TEMPLATES = REPO_ROOT/'icon_set/scripts/templates'


def typeface_layout_js():
    # layout() and svg() from the Text combine page, without that page's own UI code.
    source = (TEMPLATES/'text-combine.js').read_text()
    marker = "if(typeof document==='undefined'||!document.getElementById('glyphData'))return;"
    if source.count(marker) != 1:
        raise RuntimeError('text-combine.js changed; cannot extract the typeface layout')
    return source.replace(marker, 'return;')


def glyphs_with_space():
    glyphs = glyph_map()
    ref = glyphs['I']
    left, top, _, bottom = ref['bounds']
    glyphs[' '] = dict(ref, character=' ', icon_id='space', paths=[], bounds=[left, top, left+SPACE_ADVANCE, bottom])
    return glyphs


def text_svg(text, glyphs):
    document, width, height, _ = native_text(text, glyphs)
    document = document.replace('ns0:', '').replace(':ns0', '')
    # Shown at 2x, the same scale as the 32-unit symbols drawn at 64 px.
    document = document.replace(f'width="{width:.12g}" height="{height:.12g}"', f'width="{2*width:.12g}" height="{2*height:.12g}"', 1)
    return document.replace('<svg ', '<svg class="text-art" ', 1), width, height


def current_symbols(combinations):
    found = {}
    for row in combinations['rows']:
        if row['kind'] == 'container':
            for g in row.get('sub_generated') or []:
                found.setdefault(row['sub_id'], {})[g['icon_id']] = g.get('preview_url')
    return found


def img(src, cls, alt):
    if not src:
        return f'<div class="{cls} none">none</div>'
    return f'<img class="{cls}" src="{html.escape(src)}" alt="{html.escape(alt)}" loading="lazy">'


def edit_attr(c, on=True):
    return f' data-edit="{c["combination_id"]}" title="Edit text and combine"' if on else ''


def combo(c):
    # Filled in by container-text-report.js with the container plus the v2 text.
    return f'<div class="combo" data-cid="{c["combination_id"]}">{img(c["container_preview"], "cont", c["container_icon_id"] or "")}</div>'


def rows_html(items, glyphs, symbols, render):
    out = []
    for e in items:
        text = e.get('text')
        flags = []
        if e.get('underline'): flags.append('underline bar not drawn')
        if text and ' ' in text: flags.append(f'space = provisional {SPACE_ADVANCE}u')
        if e.get('layout'): flags.append(f'layout: {e["layout"]} in reference')
        if e.get('in_side_text_v2'): flags.append('already in side-text-v2')
        if e.get('reason'): flags.append(e['reason'])
        art, size = '<div class="text-art none">—</div>', ''
        if render and text:
            svg, w, h = text_svg(text, glyphs)
            art, size = svg, f'{w:.0f}×{h:.0f}'
        current = ''.join(img(u, 'sym', i) + f'<span class="cap">{html.escape(i)}</span>'
                          for i, u in symbols.get(e['source_id'], {}).items()) or '<div class="sym none">none</div>'
        pairs = ''.join(
            f'<figure class="pair{" editable" if render else ""}"{edit_attr(c, render)}><div class="duo">{img("combination-originals/"+c["combination_id"]+".svg", "orig", c["concept"])}'
            f'{combo(c) if render else img(c["container_preview"], "cont", c["container_icon_id"] or "")}</div>'
            f'<figcaption><b>{html.escape(c["concept"])}</b><br>{html.escape(c["container_icon_id"] or "no container")}</figcaption></figure>'
            for c in e['combinations'])
        label = html.escape(text).replace('\n', ' / ') if text else '—'
        search = html.escape(' '.join([e['name'], text or '', *[c['concept']+' '+(c['container_icon_id'] or '') for c in e['combinations']]]).lower())
        out.append(
            f'<article class="row" data-q="{search}"><header><h3><code>{label}</code> · {html.escape(e["name"])}</h3>'
            f'<span class="meta">{len(e["combinations"])} pair(s) · marked by {html.escape(e.get("marked_by", "?"))} · {e["source_id"]}</span>'
            + ''.join(f'<span class="flag">{html.escape(f)}</span>' for f in flags) + '</header>'
            f'<div class="body"><div class="col"><p class="lbl">Reference</p>{img(e["reference_url"], "ref", e["name"])}</div>'
            f'<div class="col"><p class="lbl">Typeface v2 {size}</p>{art}</div>'
            f'<div class="col"><p class="lbl">Current symbol</p><div class="syms">{current}</div></div>'
            f'<div class="col pairs"><p class="lbl">Container pairs (original · {"combined, click to edit" if render else "container"})</p><div class="plist">{pairs}</div></div></div></article>')
    return '\n'.join(out)


def letter_count(text):
    return len(text.replace(' ', '').replace('\n', ''))


def letter_groups_html(items, glyphs, symbols):
    groups = {}
    for e in items:
        n = letter_count(e['text'])
        groups.setdefault(n if n <= 4 else 5, []).append(e)
    out = []
    for n in sorted(groups):
        rows = sorted(groups[n], key=lambda e: e['text'])
        title = f'{n} letter{"s" if n > 1 else ""}' if n <= 4 else '5+ letters'
        out.append(f'<section class="group" id="letters-{n}"><h2>{title} — {len(rows)} symbols, '
                   f'{sum(len(e["combinations"]) for e in rows)} pairs</h2>{rows_html(rows, glyphs, symbols, True)}</section>')
    return '\n'.join(out)


def container_groups_html(items, glyphs):
    groups = {}
    for e in items:
        for c in e['combinations']:
            groups.setdefault(c['container_icon_id'] or 'no container', dict(preview=c['container_preview'], pairs=[]))['pairs'].append((e, c))
    out = []
    for cid, g in sorted(groups.items(), key=lambda kv: (-len(kv[1]['pairs']), kv[0])):
        tiles = []
        for e, c in sorted(g['pairs'], key=lambda p: (letter_count(p[0]['text']), p[0]['text'])):
            label = html.escape(e['text']).replace('\n', ' / ')
            search = html.escape(' '.join([cid, e['name'], e['text'], c['concept']]).lower())
            tiles.append(f'<figure class="ctile row editable" data-q="{search}"{edit_attr(c)}>{img("combination-originals/"+c["combination_id"]+".svg", "orig", c["concept"])}'
                         f'{combo(c)}<figcaption><code>{label}</code> · {letter_count(e["text"])}L'
                         f'<br>{html.escape(c["concept"])}</figcaption></figure>')
        texts = len({e['source_id'] for e, _ in g['pairs']})
        out.append(f'<section class="cgroup"><header class="chead">{img(g["preview"], "cont", cid)}<div><h3>{html.escape(cid)}</h3>'
                   f'<span class="meta">{len(g["pairs"])} pair(s) · {texts} text symbol(s)</span></div></header>'
                   f'<div class="ctiles">{"".join(tiles)}</div></section>')
    return len(groups), '\n'.join(out)


CSS = """
:root{--line:#d8dfd9;--muted:#5f6b66;--bg:#f6f7f4;--card:#fff;--ink:#1f2b27;--flag:#fff3d6;--flagink:#7a5200}
@media (prefers-color-scheme:dark){:root{--line:#34403b;--muted:#9aa7a1;--bg:#121816;--card:#1a221f;--ink:#e6ece9;--flag:#3b3016;--flagink:#f0cf86}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.45 system-ui,sans-serif}
main{max-width:1280px;margin:0 auto;padding:20px 16px 60px}h1{margin:0 0 4px;font-size:22px}.muted{color:var(--muted)}
.stats{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0}.stats div{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px}.stats strong{display:block;font-size:22px}
.toolbar{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 16px;position:sticky;top:0;background:var(--bg);padding:8px 0;z-index:2}
.toolbar input{flex:1;min-width:200px;font:inherit;padding:7px 10px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink)}
.toolbar a{padding:7px 12px;border:1px solid var(--line);border-radius:999px;text-decoration:none;color:inherit;background:var(--card)}
section{margin-top:26px}h2{font-size:18px;margin:0 0 10px}
.row{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:10px 0}
.row header{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 10px}.row h3{margin:0;font-size:15px}.row h3 code{font-size:15px;background:#eef2ee;color:#1f2b27;padding:1px 6px;border-radius:5px}
.meta{font-size:11px;color:var(--muted)}.flag{font-size:11px;background:var(--flag);color:var(--flagink);border-radius:999px;padding:2px 8px}
.body{display:grid;grid-template-columns:110px 150px 160px 1fr;gap:14px;margin-top:10px;align-items:start}
.lbl{margin:0 0 4px;font-size:11px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.03em}
img,.text-art{background:#fff;box-shadow:inset 0 0 0 1px #c6d1cb;border-radius:6px}
.ref{width:96px;height:96px;object-fit:contain;padding:6px}.text-art{display:block;box-sizing:content-box;max-width:140px;height:auto;padding:4px;color:#111;overflow:visible}
.syms{display:flex;flex-wrap:wrap;gap:6px;align-items:flex-start}.sym{width:64px;height:64px}.cap{font-size:10px;color:var(--muted);max-width:140px;overflow-wrap:anywhere}
.none{display:grid;place-items:center;width:64px;height:64px;border:1px dashed var(--line);border-radius:6px;color:var(--muted);font-size:11px;background:none;box-shadow:none}
.plist{display:flex;flex-wrap:wrap;gap:10px}.pair{margin:0;width:170px}.duo{display:flex;gap:6px}.orig,.cont{width:80px;height:80px;object-fit:contain;padding:4px}
.pair figcaption{font-size:11px;color:var(--muted);margin-top:3px;overflow-wrap:anywhere}.pair b{color:var(--ink);font-weight:600}
details>summary{cursor:pointer;font-size:18px;font-weight:700;margin:26px 0 10px}
.views{display:flex;gap:6px;margin:8px 0 0}.views button{font:inherit;padding:7px 14px;border:1px solid var(--line);border-radius:999px;background:var(--card);color:var(--ink);cursor:pointer}.views button[aria-pressed=true]{background:#2f6b45;border-color:#2f6b45;color:#fff}
.cgroup{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:12px 0}.chead{display:flex;gap:12px;align-items:center}.chead h3{margin:0;font-size:16px}
.ctiles{display:flex;flex-wrap:wrap;gap:12px;margin-top:10px}.ctile{margin:0;width:176px;display:grid;grid-template-columns:80px 1fr;gap:6px;align-items:center;border:0;padding:0;background:none}
.ctile figcaption{grid-column:1/-1;font-size:11px;color:var(--muted);overflow-wrap:anywhere}.ctile code{color:var(--ink);font-weight:600}.ctext .text-art{max-width:88px}
.group h2{margin-top:20px}.cgroup[hidden],.group[hidden]{display:none}
.combo{width:80px;height:80px;background:#fff;box-shadow:inset 0 0 0 1px #c6d1cb;border-radius:6px;padding:4px;color:#111}.combo svg{width:100%;height:100%;display:block}.combo img{width:100%;height:100%;box-shadow:none;opacity:.35}
.combo.edited{box-shadow:inset 0 0 0 2px #2f6b45}.combo-error{font-size:10px;color:#b91c1c}.editable{cursor:pointer}.editable:hover .combo{box-shadow:inset 0 0 0 2px #d9534f}
.editbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:0 0 6px}.editbar button,#editor button{font:inherit;font-size:13px;padding:6px 12px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink);cursor:pointer}
#editor{width:min(980px,96vw);border:1px solid var(--line);border-radius:14px;padding:18px;background:var(--card);color:var(--ink)}#editor::backdrop{background:#0b1210b0}
.ed-head{display:flex;justify-content:space-between;gap:12px;align-items:start}.ed-head h2{margin:0;font-size:18px}.ed-grid{display:grid;grid-template-columns:384px 1fr;gap:20px;margin-top:12px}
#edPreview svg{width:384px;height:384px;background:#fff;border-radius:8px;display:block}.ed-small{display:flex;gap:12px;align-items:end;margin-top:10px}.ed-small div{background:#fff;border-radius:6px;padding:4px;color:#111}
#edSmall svg{width:64px;height:64px;display:block}#edTiny svg{width:32px;height:32px;display:block}.ed-small img{width:72px;height:72px;background:#fff;border-radius:6px;padding:4px;object-fit:contain}
.ed-form{display:grid;gap:10px;align-content:start}.ed-form label{display:grid;gap:3px;font-size:12px;font-weight:600;color:var(--muted)}.ed-form textarea,.ed-form input,.ed-form select{font:inherit;font-size:15px;padding:6px 8px;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--ink)}
.ed-form textarea{font-size:20px;letter-spacing:.08em;min-height:64px;resize:vertical;text-transform:uppercase}.ed-row{display:flex;flex-wrap:wrap;gap:10px}.ed-row label{flex:1;min-width:90px}.ed-check{display:flex!important;align-items:center;gap:6px;grid-template-columns:none}
.ed-nudge{display:flex;gap:4px;align-items:end}#edStatus{font-size:13px;margin:0}#edStatus.warn{color:#b45309}#edSource{font-size:12px;color:var(--muted);margin:0}.ed-actions{display:flex;flex-wrap:wrap;gap:8px}
@media(max-width:760px){.ed-grid{grid-template-columns:1fr}#edPreview svg{width:100%;height:auto}}
@media(max-width:760px){.body{grid-template-columns:1fr 1fr}.pairs{grid-column:1/-1}}
"""


def build(output=OUTPUT):
    spec = json.loads(DATA.read_text())
    glyphs = glyphs_with_space()
    symbols = current_symbols(json.loads((GALLERY/'combinations.json').read_text()))
    v2, lower, other = spec['icons'], spec['lowercase_later'], spec['not_typeface']
    count = lambda items: sum(len(e['combinations']) for e in items)
    stats = [('Text symbols · typeface v2', len(v2)), ('Container pairs · v2', count(v2)),
             ('Already in side-text-v2', sum(e['in_side_text_v2'] for e in v2)),
             ('Lowercase (later)', f'{len(lower)} · {count(lower)} pairs'), ('Not typeface', f'{len(other)} · {count(other)} pairs')]
    containers, container_html = container_groups_html(v2, glyphs)
    safe = lambda text: text.replace('</', '<\\/')
    report_data = safe(json.dumps(dict(icons=v2), ensure_ascii=False, separators=(',', ':')))
    glyph_v2 = safe((REPO_ROOT/'icon_set/typeface/glyphs-v2.json').read_text())
    glyph_sizes = safe((REPO_ROOT/'icon_set/typeface/glyphs-v2-sizes.json').read_text())
    typeface_js = typeface_layout_js()
    report_js = (TEMPLATES/'container-text-report.js').read_text()
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Container Text Pairs</title><style>{CSS}</style></head><body><main>
<h1>Container text pairs</h1>
<p class="muted">Container combinations whose 32×32 symbol is text (primitive status <code>text_number</code>), read from <code>icon_set/data/container-text-v2.json</code>. Text renders use typeface v2 at native size, translation only. Rebuild: <code>/opt/homebrew/bin/python3 -m icon_set.scripts.container_text_report</code>. <a href="primitives.html?view=container">← Container pairs</a></p>
<div class="stats">{''.join(f'<div><strong>{v}</strong><span class="muted">{k}</span></div>' for k, v in stats)}</div>
<div class="views" role="group" aria-label="Group by"><button data-view="text">By text</button><button data-view="letters">By letter count</button><button data-view="container">By container</button></div>
<div class="toolbar"><input id="q" type="search" placeholder="Filter by text, name, concept or container" aria-label="Filter"><span class="jump" data-for="text"><a href="#v2">Typeface v2</a> <a href="#lower">Lowercase</a> <a href="#other">Not typeface</a></span><span class="jump" data-for="letters">{' '.join(f'<a href="#letters-{n}">{n if n < 5 else "5+"}L</a>' for n in range(1, 6))}</span></div>
<div class="editbar"><span id="editCount" class="muted">No edits yet</span><button id="copyEdits" type="button">Copy edits JSON</button><button id="downloadEdits" type="button">Download edits JSON</button><button id="clearEdits" type="button">Clear all edits</button><span class="muted">Edits are saved in this browser only; export them for the combine script.</span></div>
<div class="view" data-view="text">
<section id="v2"><h2>Typeface v2 — {len(v2)} symbols, {count(v2)} pairs</h2>{rows_html(v2, glyphs, symbols, True)}</section>
<details id="lower"><summary>Lowercase, for later — {len(lower)} symbols, {count(lower)} pairs</summary>{rows_html(lower, glyphs, symbols, False)}</details>
<details id="other"><summary>Not typeface characters — {len(other)} symbols, {count(other)} pairs</summary>{rows_html(other, glyphs, symbols, False)}</details>
</div>
<div class="view" data-view="letters"><p class="muted">Typeface v2 symbols only. Letters are counted without spaces and line breaks.</p>{letter_groups_html(v2, glyphs, symbols)}</div>
<div class="view" data-view="container"><p class="muted">{containers} containers holding typeface v2 text, most pairs first. Each tile: original pair · combined container + v2 text (click to edit) · letter count.</p>{container_html}</div>
</main>
<dialog id="editor" aria-labelledby="edTitle"><div class="ed-head"><div><h2 id="edTitle">Edit</h2><p id="edMeta" class="meta"></p></div><button id="edClose" type="button">Close</button></div>
<div class="ed-grid"><div><div id="edPreview"></div><div class="ed-small"><div id="edSmall"></div><div id="edTiny"></div><img id="edOriginal" alt="Original pair"><img id="edReference" alt="Text reference"></div>
<p class="meta">64 px · 32 px · original pair · text reference. Grid lines every 2 units, darker every 8; red box = text ink, red cross = center.</p></div>
<div class="ed-form"><label>Text (A–Z, 0–9, space, Enter for a new line)<textarea id="edText" spellcheck="false" rows="2"></textarea></label>
<div class="ed-row"><label>Size (ink height)<select id="edSize"></select></label><label>Letter spacing<input id="edTracking" type="number" min="0" max="40" step="0.5"></label><label>Line spacing<input id="edLineGap" type="number" min="0" max="40" step="0.5"></label></div>
<label class="ed-check"><input id="edUnderline" type="checkbox"> Underline</label>
<div class="ed-row"><label>Center X<input id="edX" type="number" min="0" max="64" step="0.5"></label><label>Center Y<input id="edY" type="number" min="0" max="64" step="0.5"></label>
<div class="ed-nudge"><button id="edLeft" type="button" aria-label="Left">←</button><button id="edUp" type="button" aria-label="Up">↑</button><button id="edDown" type="button" aria-label="Down">↓</button><button id="edRight" type="button" aria-label="Right">→</button></div></div>
<p id="edStatus" role="status"></p><p id="edSource"></p>
<div class="ed-actions"><button id="edApplyContainer" type="button">Use size, spacing and center for every pair in this container</button><button id="edDownload" type="button">Download combined SVG</button><button id="edReset" type="button">Reset to defaults</button></div></div></div></dialog>
<script type="application/json" id="reportData">{report_data}</script><script type="application/json" id="glyphV2">{glyph_v2}</script><script type="application/json" id="glyphV2Sizes">{glyph_sizes}</script>
<script>{typeface_js}</script><script>{report_js}</script><script>
const views=[...document.querySelectorAll('.views button')];
function setView(v){{if(!views.some(b=>b.dataset.view===v))v='text';for(const b of views)b.setAttribute('aria-pressed',String(b.dataset.view===v));for(const el of document.querySelectorAll('.view,.jump'))el.hidden=(el.dataset.view||el.dataset.for)!==v;const u=new URL(location);u.searchParams.set('group',v);history.replaceState(null,'',u);filter();}}
function filter(){{const q=document.getElementById('q').value.trim().toLowerCase();for(const r of document.querySelectorAll('.row'))r.hidden=!!q&&!r.dataset.q.includes(q);for(const g of document.querySelectorAll('.cgroup,.group'))g.hidden=!!q&&!g.querySelector('.row:not([hidden])');if(q)for(const d of document.querySelectorAll('details'))d.open=true;}}
for(const b of views)b.onclick=()=>setView(b.dataset.view);
document.getElementById('q').oninput=filter;
setView(new URLSearchParams(location.search).get('group')||'text');
</script></body></html>
"""
    output.write_text(page)
    return output


if __name__ == '__main__':
    print(build())
