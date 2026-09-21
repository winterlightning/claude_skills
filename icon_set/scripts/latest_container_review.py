"""Render one latest original per container used by the combination pairs.

Run with python3 -m icon_set.scripts.latest_container_review.
Older originals and all saved reviews are preserved.
"""
from pathlib import Path
from collections import Counter
import html
import json
import re

from icon_set.model.icons.registry import factories
from icon_set.scripts.consolidate_variants import plan_groups
from icon_set.scripts.workspace import development_dist

ROOT = Path(__file__).resolve().parents[2]


def main():
    registered = {k: v for k, v in factories().items() if v.family == 'container'}
    groups, blockers = plan_groups(registered)
    if blockers:
        raise ValueError('\n'.join(blockers))
    replacements = {old['icon_id']: group['latest']
                    for group in groups for old in group['olds']}
    mappings = json.loads((ROOT / 'icon_set/data/container-main-icons.json').read_text())['mappings']
    catalog = json.loads((development_dist(ROOT) / 'gallery/combinations.json').read_text())
    definitions = [row for row in catalog['rows'] if row['kind'] == 'container']
    counts = Counter()
    for pair in definitions:
        key = pair.get('main_key') or pair.get('main_id') or ''
        ident = key.split('/', 1)[1] if key.startswith('container/') else mappings.get(key, {}).get('icon_id') or pair.get('main_icon_id')
        # A cached catalog may still name a revision consolidated into its base.
        if ident not in registered and ident:
            ident = re.sub(r'-v\d+$', '', ident)
        if ident not in registered:
            raise ValueError(f"Unresolved main for {pair['id']}: {ident}")
        counts[replacements.get(ident, ident)] += 1
    out = ROOT / 'icon_set/.local/latest-container-review'
    out.mkdir(parents=True, exist_ok=True)
    cards, rows = [], []
    for ident, count in sorted(counts.items()):
        svg = registered[ident]().to_svg()
        (out / (ident + '.svg')).write_text(svg)
        older = sorted(k for k, v in replacements.items() if v == ident)
        rows.append(dict(icon_id=ident, pairs=count, older_versions=older))
        name = html.escape(ident.replace('-', ' '))
        cards.append(f'<article data-name="{name}"><a href="{ident}.svg"><img src="{ident}.svg" alt="{name}"></a>'
                     f'<h2>{name}</h2><p>{count} pairs</p></article>')
    (out / 'selection.json').write_text(json.dumps(rows, indent=2) + '\n')
    page = '''<!doctype html><html lang="en"><meta charset="utf-8"><title>Latest container mains</title>
<style>body{font:16px system-ui;background:#f5f6f8;color:#202630;margin:32px}header{max-width:900px}p{line-height:1.5}input{padding:12px;font:inherit;width:320px;margin:12px 0 24px}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px}article{background:white;border:1px solid #dde0e5;border-radius:12px;padding:24px;text-align:center}article[hidden]{display:none}img{width:64px;height:64px;padding:20px}h2{font-size:15px}article p{color:#657080}</style>
<header><h1>Latest container mains</h1>'''
    page += f'<p><b>{len(rows)} main containers · {sum(counts.values()):,} defined pairs</b></p>'
    page += '<p>One current drawing per container. Consolidated revisions use the original name; retired artwork is backed up separately. These drawings are for visual review and are not automatically approved or fit-validated.</p></header><input id="search" placeholder="Find a container" aria-label="Find a container"><main>'
    page += ''.join(cards) + "</main><script>document.querySelector('#search').oninput=e=>{for(const c of document.querySelectorAll('article'))c.hidden=!c.dataset.name.includes(e.target.value.toLowerCase())}</script></html>"
    (out / 'index.html').write_text(page)
    print(json.dumps(dict(review=str(out / 'index.html'), main_containers=len(rows),
                          pairs=sum(counts.values()), older_versions=sum(len(r['older_versions']) for r in rows))))


if __name__ == '__main__':
    main()
