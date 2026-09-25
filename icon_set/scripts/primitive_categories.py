#!/usr/bin/env python3
"""Give Uncategorized primitives a topic category without moving their artwork.

python3 icon_set/scripts/primitive_categories.py propose --rows .../pg_d1_app_search_worker/sql/rows.json
python3 icon_set/scripts/primitive_categories.py summary

The ``_uncategorized_NN`` folders hold primitives whose D1 ``categories`` carry no
topic (``primitives primitives-generate``). ``propose`` ranks the topic folders for
each of them by tf-idf nearest neighbours over the D1 rows that do carry a topic
(concept, old concept and tags), and writes data/primitive-categories.json:

    {"categories": {uuid: {"category", "confidence", "candidates", "method"}}}

primitives_catalog.py moves each listed row into ``category``. Entries whose
method is ``reviewed`` (set by hand or by an agent review) are never overwritten;
a ``category`` of ``Uncategorized`` keeps the row where it is.
"""
from __future__ import annotations

import argparse
import collections
import json
import math
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.scripts.primitives_catalog import (CATEGORIES_PATH, UNCATEGORIZED, primitives_root,  # noqa: E402
                                                 scan)

# Folders that are families or leftovers rather than topics; never proposed.
NOT_TOPICS = {'other', 'combination', 'container', 'text', 'typeface', 'companies'}
FIELDS = (('concept', 3), ('old_concept', 3), ('primary_tags', 2), ('tags', 1), ('secondary_tags', 1))
_WORD = re.compile(r'[a-z0-9]+')


def topics(root: Path) -> set[str]:
    return {path.name for path in root.iterdir()
            if path.is_dir() and not path.name.startswith(('_', '.')) and path.name not in NOT_TOPICS}


def tokens(record: dict) -> collections.Counter:
    weights = collections.Counter()
    for field, weight in FIELDS:
        for word in set(_WORD.findall(str(record.get(field) or '').lower())):
            if len(word) > 1:
                weights[word] += weight
    return weights


class Neighbours:
    """Cosine tf-idf nearest neighbours; votes are squared similarities."""

    def __init__(self, examples: list[tuple[collections.Counter, set[str]]]):
        self.labels = [labels for _, labels in examples]
        self.df = collections.Counter(word for words, _ in examples for word in words)
        self.n = len(examples)
        self.index = collections.defaultdict(list)
        for i, (words, _) in enumerate(examples):
            for word, weight in self.vector(words).items():
                self.index[word].append((i, weight))

    def vector(self, words: collections.Counter) -> dict[str, float]:
        vector = {w: c * math.log(self.n / (1 + self.df[w])) for w, c in words.items() if w in self.df}
        norm = math.sqrt(sum(v * v for v in vector.values())) or 1.0
        return {w: v / norm for w, v in vector.items()}

    def rank(self, words: collections.Counter, k: int = 15) -> list[tuple[str, float]]:
        scores = collections.Counter()
        for word, weight in self.vector(words).items():
            for i, other in self.index[word]:
                scores[i] += weight * other
        votes = collections.Counter()
        for i, score in scores.most_common(k):
            for label in self.labels[i]:
                votes[label] += score * score
        total = sum(votes.values()) or 1.0
        return [(label, round(vote / total, 3)) for label, vote in votes.most_common(3)]


def load(path: Path) -> dict:
    if not path.is_file():
        return {'categories': {}}
    return json.loads(path.read_text(encoding='utf-8'))


def save(path: Path, data: dict) -> None:
    data['categories'] = dict(sorted(data['categories'].items()))
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def propose(rows_json: Path, root: Path, target: Path) -> collections.Counter:
    known = topics(root)
    records = json.loads(rows_json.read_text(encoding='utf-8'))
    by_id = {str(r.get('id') or '').lower(): r for r in records}
    examples = [(tokens(r), labels) for r in records
                if (labels := set(str(r.get('categories') or '').split()) & known)]
    neighbours = Neighbours(examples)
    data = load(target)
    entries = data.setdefault('categories', {})
    counts = collections.Counter()
    for row in scan(root):
        uid = row['uuid']
        if row['category'] != UNCATEGORIZED or not uid:
            continue
        if (entries.get(uid) or {}).get('method') == 'reviewed':
            counts['reviewed'] += 1
            continue
        record = by_id.get(uid) or {'concept': row['concept'], 'old_concept': row['old_concept']}
        ranked = neighbours.rank(tokens(record))
        if not ranked:
            counts['no match'] += 1
            continue
        entries[uid] = {'category': ranked[0][0], 'confidence': ranked[0][1],
                        'candidates': [label for label, _ in ranked], 'method': 'knn',
                        'concept': row['concept']}
        counts['proposed'] += 1
    save(target, data)
    return counts


def summary(target: Path) -> None:
    entries = load(target)['categories']
    methods = collections.Counter(e.get('method', '?') for e in entries.values())
    categories = collections.Counter(e.get('category') for e in entries.values())
    print(f'{len(entries)} entries in {target}: ' + ', '.join(f'{m}={n}' for m, n in methods.most_common()))
    for category, n in categories.most_common():
        print(f'  {n:5d}  {category}')


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--primitives', type=Path)
    parser.add_argument('--target', type=Path, default=CATEGORIES_PATH)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('propose', help='rank topic folders for every Uncategorized primitive')
    p.add_argument('--rows', type=Path, required=True, help='D1 rows.json from pg_d1_app_search_worker/sql')
    sub.add_parser('summary', help='count entries by method and category')
    args = parser.parse_args(argv)
    if args.command == 'propose':
        counts = propose(args.rows, primitives_root(args.primitives), args.target)
        print(' '.join(f'{k}={v}' for k, v in counts.items()), '->', args.target)
    else:
        summary(args.target)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
