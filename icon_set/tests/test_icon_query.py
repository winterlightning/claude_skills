"""deploy.py's icon list (icon_query) against the answers gallery.html gave over the same made-up catalog
(cloud/worker/core/tests/fixtures/icon-query*.json; the Worker's SQL is checked against them in core/tests/icon_query.rs)."""
import json
from pathlib import Path
import sqlite3
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'icon_set/scripts'))
import icon_query  # noqa: E402
from reviewer_stats import current_reviews  # noqa: E402

FIXTURES = ROOT / 'cloud/worker/core/tests/fixtures'


def catalog():
    fixture = json.loads((FIXTURES / 'icon-query.json').read_text())
    records = [dict(r) for r in fixture['records']]
    by_key = {r['key']: r for r in records}
    graphs = set(fixture['graphs'])
    # deploy.py's catalog has picked artwork applied, as the Worker's overrides apply it.
    for pick in fixture['artwork']:
        now, document = fixture['current_sha'][pick['key']], pick['document']
        if document.get('source_svg_sha256') and (now not in graphs or document['source_svg_sha256'] == now):
            by_key[pick['key']].update(artwork_source=document.get('source_mode') or 'use_org', svg_sha256=now)
    db = sqlite3.connect(':memory:')
    db.execute('CREATE TABLE reviews(icon, svg_sha256, status, updated_at, updated_by, worker, claimed_at, note)')
    db.execute('CREATE TABLE split_requests(icon, svg_sha256, created_by, created_at, active)')
    for r in fixture['reviews']:
        db.execute('INSERT INTO reviews VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (r['icon'], r['svg_sha256'], r['status'], r['updated_at'],
                   r.get('updated_by'), r.get('worker'), r.get('claimed_at'), r.get('note')))
    for s in fixture['splits']:
        db.execute('INSERT INTO split_requests VALUES (?, ?, ?, ?, ?)', (s['icon'], s['svg_sha256'], s['created_by'], s['created_at'], s['active']))
    statuses, approved, disapproved, rejected = current_reviews(db, by_key)
    current = {k: r['svg_sha256'] for k, r in by_key.items()}
    work = icon_query.work_claims([row for row in db.execute(
        'SELECT icon, svg_sha256, status, worker, claimed_at, note, updated_at FROM reviews') if current.get(row[0]) == row[1]])
    return fixture, icon_query.Catalog(records, statuses, approved, disapproved, rejected, fixture['feedback'], work, fixture['facets'])


class IconQueryTest(unittest.TestCase):
    def test_decisions(self):
        expected = json.loads((FIXTURES / 'icon-query-expected.json').read_text())
        self.assertEqual(catalog()[1].statuses, expected['statuses'])

    def test_lists_what_the_page_listed(self):
        fixture, listing = catalog()
        expected = json.loads((FIXTURES / 'icon-query-expected.json').read_text())
        for case, want in zip(fixture['cases'], expected['results']):
            with self.subTest(case=case):
                got = listing.list(icon_query.params({k: [str(v)] for k, v in case.items()}))
                self.assertEqual({'keys': [i['key'] for i in got['items']], **{k: got[k] for k in ('total', 'versions', 'offset', 'states', 'categories')}},
                                 {k: want[k] for k in ('keys', 'total', 'versions', 'offset', 'states', 'categories')})

    def test_cards_and_details(self):
        _, listing = catalog()
        item = listing.by_keys(['solo/arrow-01'])['items'][0] if listing.by_keys(['solo/arrow-01'])['items'] else listing.list(icon_query.params({}))['items'][0]
        self.assertNotIn('primitives', item)
        self.assertIn(item['review']['state'], icon_query.STATES)
        detail = listing.detail(item['key'])
        self.assertEqual(detail['review'], item['review'])
        self.assertIn('keywords', detail)
        self.assertEqual(sum(listing.facet_choices()['families'].values()), len(listing.records))

    def test_words_profile_uncategorized_and_families(self):
        _, listing = catalog()
        run = lambda **q: listing.list(icon_query.params({k: [v] for k, v in {'limit': '192', **q}.items()}))  # noqa: E731
        words = run(terms='Cup  00')['items']
        self.assertTrue(words and all('cup' in icon_query.search_text(i) and '00' in icon_query.search_text(i) for i in words))
        profile = run(profile='SUB')['items']
        self.assertTrue(profile and all(i['key'].startswith('sub/') for i in profile))
        none = run(category_group='uncategorized')['items']
        self.assertTrue(none and all(not i.get('category') for i in none))
        everything = run()
        self.assertEqual(sum(everything['families'].values()), everything['total'])


if __name__ == '__main__':
    unittest.main()
