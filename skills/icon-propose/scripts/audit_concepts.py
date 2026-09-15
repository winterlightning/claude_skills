#!/usr/bin/env python3
"""Read-only name coverage audit; matches are not visual identity judgments."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import unicodedata


def normalize(value):
    text = unicodedata.normalize('NFKC', str(value)).casefold()
    return ' '.join(re.findall(r'[^\W_]+', text, flags=re.UNICODE))


def read_json(path, missing):
    if not path.is_file():
        missing.append(str(path))
        return {}
    return json.loads(path.read_text(encoding='utf-8'))


def audit(repo, category=None, terms=(), limit=12):
    missing = []
    catalog = read_json(repo / 'icon_set/dist/gallery/primitives.json', missing)
    library = read_json(repo / 'icon_set/dist/gallery/icons.json', missing)
    dictionary = read_json(repo / 'icon_set/scripts/templates/concept-dictionary.json', missing)
    rows = catalog.get('rows', [])
    chosen = [r for r in rows if category is None or r['category'] == category]
    names = Counter(normalize(r['concept']) for r in chosen)
    records = []
    for r in rows:
        records.append({'kind': 'source', 'category': r['category'],
                        'name': r['concept'], 'aliases': [r.get('old_concept', '')],
                        'id': r.get('uuid'), 'path': r.get('path')})
    for r in library.get('icons', []) + library.get('failed_icons', []):
        records.append({'kind': 'model', 'name': r.get('name', r['icon_id']),
                        'aliases': [r['icon_id']], 'id': r['icon_id'],
                        'family': r.get('family'), 'category': r.get('category')})
    for cat, data in dictionary.get('categories', {}).items():
        for r in data.get('entries', []):
            records.append({'kind': 'dictionary', 'category': cat,
                            'name': r['name'], 'aliases': r.get('aliases', []) + [r['id']],
                            'id': r['id'], 'status': r.get('status')})
    model_dir = repo / 'icon_set/model/icons'
    if not model_dir.is_dir():
        missing.append(str(model_dir))
    else:
        for path in sorted(model_dir.rglob('*.py')):
            if not path.name.startswith('_'):
                records.append({'kind': 'model_filename', 'name': path.stem,
                                'path': str(path.relative_to(repo)), 'aliases': []})
    matches = {}
    for term in terms:
        query = normalize(term)
        if not query:
            raise ValueError('Search terms must contain a letter or digit.')
        found = []
        for r in records:
            labels = [normalize(v) for v in [r['name'], *r['aliases']]]
            exact = query in labels
            if exact or any(set(query.split()) <= set(v.split()) for v in labels):
                found.append(dict(r, exact=exact))
        found.sort(key=lambda r: (not r['exact'], r['kind'], r['name']))
        matches[term] = {'total_name_matches': len(found), 'shown': found[:limit]}
    return {'category': category, 'source_count': len(chosen),
            'distinct_normalized_source_names': len(names),
            'repeated_names': [{'name': n, 'count': c} for n, c in names.most_common() if c > 1][:limit],
            'source_name_sample': [r['concept'] for r in chosen[:limit]],
            'category_counts': dict(sorted(Counter(r['category'] for r in rows).items())),
            'existing_dictionary_counts': {c: dict(Counter(e.get('status', 'unknown') for e in d.get('entries', []))) for c, d in dictionary.get('categories', {}).items() if category is None or c == category},
            'searches': matches, 'unavailable_paths': missing,
            'interpretation': 'Names and aliases only. Search synonyms and inspect artwork. No match is not proof of absence.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--category')
    parser.add_argument('--terms', nargs='+', default=[])
    parser.add_argument('--limit', type=int, default=12)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error('--limit must be positive')
    repo = args.repo.expanduser().resolve()
    if not (repo / 'icon_set').is_dir():
        parser.error('--repo must contain an icon_set directory')
    try:
        print(json.dumps(audit(repo, args.category, args.terms, args.limit), ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f'Cannot audit catalog: {error}\n')


if __name__ == '__main__':
    main()
