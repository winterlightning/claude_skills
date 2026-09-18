"""Canonicalize identical sub artwork while retaining source identities and files."""
from __future__ import annotations
import copy
import hashlib
import html
import json
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def fingerprint(document):
    root = ET.fromstring(document)
    # IDs can affect rendering through CSS/references; keep these SVGs exact.
    if 'url(' in document or 'href=' in document or '<style' in document:
        return hashlib.sha256(document.encode()).hexdigest()
    def node(element):
        if element.tag.rsplit('}', 1)[-1] in ('title', 'desc', 'metadata'):
            return None
        return [element.tag, sorted((k, v) for k, v in element.attrib.items() if k != 'id'),
                (element.text or '').strip(), [value for child in element if (value := node(child)) is not None]]
    return hashlib.sha256(json.dumps(node(root), separators=(',', ':')).encode()).hexdigest()


def canonical_map(manifest, root=ROOT):
    groups = defaultdict(list)
    for uid, record in manifest.items():
        path = root / record['svg']
        if not path.is_file():
            raise FileNotFoundError(path)
        groups[fingerprint(path.read_text())].append(uid)
    parent = {uid: uid for uid in manifest}
    def find(uid):
        while parent[uid] != uid:
            uid = parent[uid]
        return uid
    def join(a, b):
        parent[find(b)] = find(a)
    for members in groups.values():
        for uid in members[1:]:
            join(members[0], uid)
    review_path = root / 'icon_set/data/sub-deduplication-review.json'
    if review_path.exists():
        for decision in json.loads(review_path.read_text())['decisions']:
            if decision['decision'] != 'merge':
                continue
            a, b = decision['icons']
            # Reviewed visual mappings are bound to the exact reviewed artwork.
            if all(uid in manifest and fingerprint((root/manifest[uid]['svg']).read_text()) == decision['fingerprints'][uid] for uid in (a, b)):
                join(a, b)
    merged = defaultdict(list)
    for uid in manifest:
        merged[find(uid)].append(uid)
    aliases, duplicates = {}, []
    for members in merged.values():
        members.sort(key=lambda uid: (manifest[uid]['family'] != 'sub', len(uid), uid))
        canonical = members[0]
        if len(members) > 1:
            aliases.update({uid: canonical for uid in members[1:]})
            fingerprints = {fingerprint((root/manifest[uid]['svg']).read_text()) for uid in members}
            duplicates.append(dict(canonical=canonical, aliases=members[1:],
                match='exact' if len(fingerprints) == 1 else 'reviewed-concept',
                artwork_sha256=fingerprint((root/manifest[canonical]['svg']).read_text())))
    return aliases, duplicates


def update_catalog(catalog, manifest, aliases, root=ROOT):
    for row in catalog['rows']:
        generated, exports, seen = [], [], set()
        for item in catalog['references'][row['sub_id']]['generated']:
            uid = aliases.get(item['icon_id'], item['icon_id'])
            record = manifest.get(uid)
            key = record['family'] + '/' + uid if record else item['key']
            if key in seen:
                continue
            seen.add(key)
            generated.append(dict(item, icon_id=uid, key=key,
                                  preview_url=record['export_url'] if record else item['preview_url']))
            if record:
                exports.append(record)
        row['sub_generated'] = generated
        row['sub_exports'] = exports
        trial = row.get('trial_preview')
        if trial and trial.get('sub_key', '').split('/', 1)[-1] in aliases:
            row.pop('trial_preview')
            row['trial_status'] = 'stale'


    from .activate_sub_profiles import stage_catalog
    stage_catalog(catalog, root)


def deduplicate_pairs(pairs, manifest, aliases, root=ROOT):
    changed = 0
    for row in pairs['rows']:
        subs, seen = [], set()
        for item in row['subs']:
            uid = aliases.get(item['icon'], item['icon'])
            replacement = copy.deepcopy(item)
            if uid != item['icon']:
                record = manifest[uid]
                document = (root / record['svg']).read_text()
                # Only replace if the live pair actually contains the same artwork.
                source_document = (root / manifest[item['icon']]['svg']).read_text()
                if fingerprint(source_document) != fingerprint(item['document']):
                    raise ValueError('Stale pair artwork: ' + row['id'] + '/' + item['icon'])
                replacement.update(record, document=document,
                                   sha256=hashlib.sha256(document.encode()).hexdigest())
                if fingerprint(document) != fingerprint(item['document']):
                    replacement.update(bounds=record['ink32']['bounds'], canvas=32, export_size=32)
                    for field in ('target_keyshape', 'target_keyshape_bounds', 'source_radial_extent', 'source_bounds'):
                        replacement.pop(field, None)
                    replacement.update(sub32_status='ink32_normalized', sub32_reason='Reviewed canonical sub artwork.')
            key = (replacement['family'], replacement['icon'])
            if key not in seen:
                seen.add(key)
                subs.append(replacement)
        if subs != row['subs']:
            changed += 1
            row.setdefault('sub_dedup_original_keys', [s['family']+'/'+s['icon'] for s in row['subs']])
            row['subs'] = subs
    return changed


def run(root=ROOT):
    data = root / 'icon_set/data'
    gallery = root / 'icon_set/dist/gallery'
    manifest = json.loads((data/'combination-sub32.json').read_text())
    aliases, groups = canonical_map(manifest, root)
    pairs = json.loads((data/'combination-pairs.json').read_text())
    changed = deduplicate_pairs(pairs, manifest, aliases, root)
    report = dict(schema='pictographic.sub-deduplication.v1', policy='Identical SVG artwork plus visually reviewed same-concept drawings; prefer native sub, then shortest ID. Reviewed mappings are bound to artwork fingerprints.',
                  scanned=len(manifest), canonical_count=len(manifest)-len(aliases),
                  aliases=aliases, groups=groups,
                  affected_pairs=[r['id'] for r in pairs['rows'] if 'sub_dedup_original_keys' in r])
    # All validation above precedes writes. Authored icons/exports remain available
    # for old links and source-reference provenance; active pair choices are unique.
    (data/'sub-deduplication.json').write_text(json.dumps(report, indent=2)+'\n')
    (data/'canonical-sub32.json').write_text(json.dumps({uid: record for uid, record in manifest.items() if uid not in aliases}, indent=2)+'\n')
    payload = json.dumps(pairs)
    (data/'combination-pairs.json').write_text(payload)
    (gallery/'experiment-combination.json').write_text(payload)
    catalog_path = gallery/'combinations.json'
    if catalog_path.exists():
        catalog = json.loads(catalog_path.read_text())
        update_catalog(catalog, manifest, aliases, root)
        catalog_path.write_text(json.dumps(catalog, separators=(',', ':'))+'\n')
    cards = []
    for group in sorted(groups, key=lambda g:g['canonical']):
        figures = []
        for uid in [group['canonical'], *group['aliases']]:
            record = manifest[uid]
            figures.append('<figure><img src="'+html.escape(record['export_url'])+'"><figcaption>'+html.escape(record['family']+'/'+uid)+('</figcaption><b>Retained</b>' if uid == group['canonical'] else '</figcaption>')+'</figure>')
        cards.append('<section><p>'+html.escape(group['match'])+'</p>'+''.join(figures)+'</section>')
    (gallery/'sub-deduplication.html').write_text('<!doctype html><meta charset="utf-8"><title>Sub icon deduplication</title><style>body{font:15px system-ui;margin:32px}section{display:flex;flex-wrap:wrap;border-top:1px solid #ccc;padding:16px}figure{width:190px;margin:12px;overflow-wrap:anywhere}img{width:64px;height:64px}b{color:#167348}</style><h1>Sub icon deduplication</h1><p>'+f'{len(manifest)} entries → {len(manifest)-len(aliases)} distinct artworks. {len(aliases)} aliases in {len(groups)} groups. '+f'{len(report["affected_pairs"])} side pairs updated. Original source files preserved.</p>'+''.join(cards))
    print(f'Scanned {len(manifest)}; merged {len(aliases)} aliases in {len(groups)} groups; updated {changed} side pairs.')
    from .activate_sub_profiles import run as activate_profiles
    activate_profiles(root)
    return report


if __name__ == '__main__':
    run()
