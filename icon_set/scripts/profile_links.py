"""Persistent many-to-one profile relationships, independent of variant ancestry."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def load_links(root=ROOT):
    path=root/'icon_set/data/icon-profile-links.json'
    return json.loads(path.read_text()).get('links',[]) if path.exists() else []


def annotate(records, root=ROOT):
    sources,derivatives={},{}
    for link in load_links(root):
        sources.setdefault(link['target'],[]).append(dict(key=link['source'],relationship=link['relationship'],source_svg_sha256=link.get('source_svg_sha256')))
        derivatives.setdefault(link['source'],[]).append(dict(key=link['target'],relationship=link['relationship']))
    for record in records:
        key=record.get('key') or record['family']+'/'+record['icon_id']
        for field,values in [('profile_sources',sources.get(key,[])),('profile_derivatives',derivatives.get(key,[]))]:
            if values:record[field]=values
            else:record.pop(field,None)


def validate(links, registered, external_keys=()):
    known={f.family+'/'+uid for uid,f in registered.items()} | set(external_keys)
    pairs=set()
    for link in links:
        source,target=link['source'],link['target']
        if source not in known or target not in known:
            raise ValueError(f'Unknown profile link: {source} -> {target}')
        if source==target or not target.startswith(('sub/','symbol/')):
            raise ValueError(f'Invalid profile link: {source} -> {target}')
        if (source,target) in pairs:raise ValueError('Duplicate profile link')
        pairs.add((source,target))
