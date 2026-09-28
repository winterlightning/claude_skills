#!/usr/bin/env python3
"""Seed the meaning layer of data-model.html from today's reference data (read-only on sources).

    python3 cloud/migrate/seed_reference.py            # → cloud/exports/seed-reference.sql + .report.json
    wrangler d1 execute pictographic --local --file cloud/exports/seed-reference.sql     # (from cloud/worker)

Fills:
* ``references``        every original SVG (pictographic-primitives, pictographic-combinations),
                        with its R2 key under references/…
* ``reference_parts``   main/sub (side) and container/symbol (container) of each combination, from
                        combination_data.json
* ``categories``        the (parent) - (child) tree of concepts_streamline.json
* ``concepts``          concepts_streamline.json names, with their categories
* ``physicals``         CANDIDATES only: the `main_icon`/`sub_icon` form names, numbered sets folded
                        (cog, cog_1, cog_2 → cog) — status 'candidate' until reviewed
* ``concept_physicals`` concept → the physical its reference file draws
* ``icon_references``   authored icon → the reference UUID it was drawn from (catalog original_sources)

Nothing is guessed silently: the report lists references whose concept name matches no concept,
combinations missing from one of the two combination files, and numbered sets that may be
distinct forms rather than variants (e.g. dice_1…dice_6).
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_d1_import import inserts  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
NUMBERED = re.compile(r'_(\d+|one|two|three|four|five|six)$')


def slug(text: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', str(text).strip().lower()).strip('-') or 'unnamed'


def form_name(name: str) -> str:
    """A physical's name from a main_icon/sub_icon value, typos kept for review, numbers folded."""
    clean = re.sub(r'[\s-]+', '_', str(name).strip().lower())
    return NUMBERED.sub('', clean)


def locate(root: Path) -> dict[str, str]:
    """file name → path relative to root (manifests name files, folders nest by batch)."""
    return {path.name: path.relative_to(root).as_posix() for path in root.rglob('*.svg')}


def build() -> tuple[list[str], dict]:
    report = {}
    statements = []
    # ---- references
    references, by_concept_name = [], defaultdict(list)
    for folder, kind, prefix in (('pictographic-primitives', 'single', 'references/primitives'),
                                 ('pictographic-combinations', 'combination', 'references/combinations')):
        root = ROOT / folder
        paths = locate(root)
        missing = 0
        with (root / '_manifest.csv').open(newline='', encoding='utf-8') as stream:
            for row in csv.DictReader(stream):
                relative = paths.get(row['file'])
                missing += relative is None
                digest = hashlib.sha256((root / relative).read_bytes()).hexdigest() + '.svg' if relative else None
                references.append((row['id'], kind, row['concept'], row['old_concept'], row['categories'], row['folder'],
                                   row['file'], f'{prefix}/{relative}' if relative else None, 'pictographic', None, digest))
                by_concept_name[form_name(row['old_concept'])].append(row['id'])
        report[f'{folder} rows'] = sum(1 for r in references if r[1] == kind)
        report[f'{folder} files not found'] = missing
    # The Lucide and human reference library (icons may be drawn from these too).
    library = ROOT / 'icon_set' / 'references'
    for path in sorted(library.rglob('*')):
        if path.is_file() and path.suffix.lower() in ('.svg', '.png'):
            relative = path.relative_to(library).as_posix()
            digest = hashlib.sha256(path.read_bytes()).hexdigest() + path.suffix.lower()
            references.append((f'library:{relative}', 'single', path.stem, path.stem, None, relative.split('/')[0], path.name,
                               f'references/library/{relative}', relative.split('/')[0], None, digest))
    report['library references'] = sum(1 for r in references if r[0].startswith('library:'))
    # ---- concepts and categories
    streamline = json.loads((ROOT / 'concepts_streamline.json').read_text(encoding='utf-8'))
    categories, concept_rows, concept_categories = {}, [], set()
    physicals, concept_physicals, numbered = {}, set(), defaultdict(set)
    concept_ids = {}
    for key, entry in streamline.items():
        concept_id = slug(key)
        if concept_id in concept_ids.values():
            concept_id = f'{concept_id}-{len(concept_ids)}'
        concept_ids[key] = concept_id
        concept_rows.append((concept_id, concept_id, entry.get('name') or key, '', 'active', 'concepts_streamline'))
        for label in entry.get('category_names') or []:
            parts = re.findall(r'\(([^)]*)\)', label) or [label]
            parent = None
            for depth, part in enumerate(parts):
                category_id = '/'.join(slug(p) for p in parts[:depth + 1])
                categories.setdefault(category_id, (category_id, parent, slug(part), part))
                parent = category_id
            concept_categories.add((concept_id, parent, int(slug(parts[0]) == slug(entry.get('main_category') or ''))))
        for file in entry.get('files') or []:
            for field in ('main_icon', 'sub_icon'):
                raw = (file.get(field) or '').strip()
                if not raw:
                    continue
                name = form_name(raw)
                physicals.setdefault(slug(name), (slug(name), slug(name), name.replace('_', ' '), '', 'single', 'candidate'))
                if NUMBERED.search(re.sub(r'[\s-]+', '_', raw.lower())):
                    numbered[name].add(raw)
                if field == 'main_icon' and file.get('type') == 'physical':
                    concept_physicals.add((concept_id, slug(name), 1))
    statements += inserts('categories', ['category_id', 'parent_id', 'slug', 'name'], list(categories.values()))
    statements += inserts('concepts', ['concept_id', 'slug', 'name', 'description', 'status', 'source'], concept_rows)
    statements += inserts('concept_categories', ['concept_id', 'category_id', 'is_primary'], sorted(concept_categories))
    statements += inserts('physicals', ['physical_id', 'slug', 'name', 'description', 'kind', 'status'], list(physicals.values()))
    statements += inserts('concept_physicals', ['concept_id', 'physical_id', 'rank'], sorted(concept_physicals))
    # ---- link references to concepts by their original concept name
    known = {form_name(k): v for k, v in concept_ids.items()}
    linked = []
    unmatched = []
    for row in references:
        concept_id = None if row[0].startswith('library:') else known.get(form_name(row[3]))
        linked.append(row[:11] + (concept_id,))
        if concept_id is None and not row[0].startswith('library:'):
            unmatched.append(row[3])
    statements += inserts('references', ['reference_id', 'kind', 'concept', 'old_concept', 'categories', 'folder', 'file', 'r2_key',
                                         'source', 'license', 'sha256', 'concept_id'], linked)
    # ---- combination parts
    combos = json.loads((ROOT / 'combination_data.json').read_text(encoding='utf-8'))
    parts = []
    for kind, rows in combos.items():
        for row in rows:
            if kind == 'container':
                parts += [(row['id'], 'container', row['main_id'], 'center'), (row['id'], 'symbol', row['sub_id'], 'center')]
            else:
                position = {'tl': 'tl', 'tr': 'tr', 'bl': 'bl', 'br': 'br'}.get(row.get('position'))
                parts += [(row['id'], 'main', row['main_id'], None), (row['id'], 'sub', row['sub_id'], position)]
    reference_ids = {r[0] for r in references}
    missing_part = [p for p in parts if not p[2]]
    kept = [p for p in parts if p[0] in reference_ids and p[2]]
    statements += inserts('reference_parts', ['reference_id', 'role', 'part_reference_id', 'position'], kept)
    listed = {row['id'] for rows in combos.values() for row in rows}
    in_manifest = {r[0] for r in references if r[1] == 'combination'}
    # ---- authored icons → references
    catalog = json.loads((ROOT / 'published' / 'gallery' / 'icons.json').read_text(encoding='utf-8'))
    icon_refs = set()
    for field in ('icons', 'failed_icons'):
        for record in catalog.get(field, []):
            for source in record.get('original_sources') or []:
                match = re.search(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{10}[0-9a-z]{2}', json.dumps(source))
                if match and match.group(0) in reference_ids:
                    icon_refs.add((record['key'], match.group(0)))
    statements += inserts('icon_references', ['icon', 'reference_id'], sorted(icon_refs))
    report.update({
        'concepts': len(concept_rows), 'categories': len(categories), 'physical candidates': len(physicals),
        'concept → physical links': len(concept_physicals), 'references': len(references),
        'references whose concept name matches a concept': len(references) - len(unmatched) - report['library references'],
        'references without a concept (to link by review)': len(unmatched),
        'combination parts': len(kept),
        'combination parts without a main/sub id in combination_data.json': len(missing_part),
        'combination parts skipped (reference not in a manifest)': len(parts) - len(kept) - len(missing_part),
        'combinations only in combination_data.json': len(listed - in_manifest),
        'combinations only in the combinations manifest': len(in_manifest - listed),
        'authored icon → reference links': len(icon_refs),
        'numbered form sets to review (variants or distinct forms?)': len(numbered),
        'examples: numbered sets': {k: sorted(v) for k, v in sorted(numbered.items(), key=lambda kv: -len(kv[1]))[:15]},
        'examples: unmatched concept names': Counter(unmatched).most_common(15),
    })
    return statements, report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--out', type=Path, default=ROOT / 'cloud' / 'exports' / 'seed-reference.sql')
    args = parser.parse_args(argv)
    statements, report = build()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text('\n'.join(statements) + '\n', encoding='utf-8')
    args.out.with_suffix('.report.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k: v for k, v in report.items() if not k.startswith('examples')}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
