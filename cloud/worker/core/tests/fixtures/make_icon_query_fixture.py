#!/usr/bin/env python3
"""Write icon-query.json: a made-up catalog with reviews, feedback, picks and facets covering every filter of Icon
review, plus the list queries to check. The expected answers come from the page itself:

    python3 cloud/worker/core/tests/fixtures/make_icon_query_fixture.py
    node cloud/worker/core/tests/fixtures/make_icon_query_expected.mjs     # runs gallery.html's own list functions

Checked by core/tests/icon_query.rs (the Worker's SQL) and icon_set/tests/test_icon_query.py (deploy.py's).
"""
import hashlib
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
rng = random.Random(7)
sha = lambda text: hashlib.sha256(text.encode()).hexdigest()  # noqa: E731
WORDS = ['cup', 'arrow', 'bell', 'cloud', 'gear', 'house', 'lock', 'moon', 'pen', 'star', 'tree', 'wave']
CATEGORIES = ['food', 'arrows', 'weather', 'tools', '']
KEYSHAPES = ['SQUARE', 'CIRCLE', 'TALL_M', None]
AUTHORS = ['claude-opus-5-5', 'gpt-x', None]
PEOPLE = ['ray', 'hina', 'jakes']


def model(n):
    primitives = [{'kind': rng.choice(['line', 'bezier']), 'element_id': f'e{i}', 'segments': [0] * rng.randint(0, 3)} for i in range(n)]
    contours = [{'members': [p['element_id'] for p in primitives[:2]]}] if n >= 3 and rng.random() < 0.6 else []
    return primitives, contours


records = []
for index in range(64):
    family = rng.choice(['solo'] * 5 + ['sub', 'icon-72', 'side_combination64', 'container_combination64', 'symbol'])
    word = WORDS[index % len(WORDS)]
    icon_id = f'{word}-{index:02d}'
    record = {'key': f'{family}/{icon_id}', 'icon_id': icon_id, 'name': f'{word} {index:02d}', 'family': family,
              'category': rng.choice(CATEGORIES), 'keywords': rng.sample(WORDS, 2), 'aliases': [word.upper()] if index % 5 == 0 else [],
              'svg_sha256': sha(f'{family}/{icon_id}/1'), 'preview_url': f'{family}/{icon_id}.svg', 'profile': family.upper(),
              'canvas_size': 48, 'validation': {'status': 'valid', 'errors': []}}
    if rng.random() < 0.8:
        record['created_at'] = f'2026-0{rng.randint(1, 9)}-{rng.randint(10, 28)}T0{rng.randint(0, 9)}:00:00+07:00'
    if rng.random() < 0.6:
        record['modified_at'] = f'2026-09-{rng.randint(10, 28)}T10:{rng.randint(10, 59)}:00.123456+00:00'
    if (author := rng.choice(AUTHORS)):
        record['author'] = author
    if (keyshape := rng.choice(KEYSHAPES)):
        record['keyshape'] = keyshape
    if family == 'solo' and rng.random() < 0.3:
        record['side_role'] = rng.choice(['main', 'sub'])
    if rng.random() < 0.6:
        record['original_sources'] = [{'url': f'originals/{index}.svg'}]
    uploaded = rng.random() < 0.15
    if uploaded:
        record['uploaded_icon'] = True
    else:
        record['artwork_source'] = rng.choice(['use_org', None])
        if rng.random() < 0.8:
            record['primitives'], record['contours'] = model(rng.randint(1, 13))
    if rng.random() < 0.12:
        record['build_failed'] = True
        record['validation'] = {'status': 'invalid', 'exception': None}
        record['errors'] = ['too thin']
    records.append(record)

# Revisions: v2 / v3 of a few icons (same family, variant_of / variant_root).
for base in [r for r in records if r['family'] == 'solo' and not r.get('uploaded_icon')][:4]:
    for n in (2, 3)[:rng.randint(1, 2)]:
        icon_id = f"{base['icon_id']}-v{n}"
        records.append({**{k: v for k, v in base.items() if k not in ('build_failed', 'errors')}, 'key': f"solo/{icon_id}",
                        'icon_id': icon_id, 'name': base['name'] + f' v{n}', 'variant_of': base['icon_id'],
                        'variant_root': base['icon_id'], 'variant_label': f'Revision {n}', 'svg_sha256': sha(f'solo/{icon_id}/1')})

reviews, splits, feedback, artwork, graphs, facets = [], [], [], [], [], {}
stamp = iter(f'2026-09-{d:02d}T{h:02d}:00:00Z' for d in range(1, 29) for h in range(24))
current = {r['key']: r['svg_sha256'] for r in records}
for record in records:
    key, sha_now = record['key'], record['svg_sha256']
    roll = rng.random()
    if roll < 0.15:
        # A decision on an older drawing only: ignored (a rejected one still rejects).
        reviews.append({'icon': key, 'svg_sha256': sha(key + '/old'), 'status': rng.choice(['approve', 'rejected']),
                        'updated_at': next(stamp), 'updated_by': rng.choice(PEOPLE)})
    elif roll < 0.85:
        status = rng.choice(['approve', 'approve', 'pending', 'ready', 're-generated', 'claimed', 'rejected'])
        row = {'icon': key, 'svg_sha256': sha_now, 'status': status, 'updated_at': next(stamp), 'updated_by': rng.choice(PEOPLE + [None])}
        if status in ('claimed', 'pending', 'ready') and rng.random() < 0.4:
            row.update(worker='thuan-mac', claimed_at='2026-09-30T00:00:00Z', note='checked')
        reviews.append(row)
    if rng.random() < 0.05:
        splits.append({'icon': key, 'svg_sha256': sha_now, 'created_by': 'hina', 'created_at': next(stamp), 'active': 1})
    for _ in range(rng.choice([0, 0, 1, 2])):
        feedback.append({'id': len(feedback) + 1, 'icon': key, 'svg_sha256': rng.choice([sha_now, sha_now, sha(key + '/old')]),
                         'author': rng.choice(PEOPLE + [None]), 'reason': rng.choice(['bad-draw', 'meaning', 'manual-fix-request', 'other', ''])})
    if not record.get('uploaded_icon') and rng.random() < 0.85:
        graphs.append(sha_now)
    if rng.random() < 0.5:
        facets[key] = {'axes': rng.choice([[], ['vertical'], ['horizontal'], ['vertical', 'horizontal']]),
                       'svg_sha256': rng.choice([sha_now, sha_now, sha_now, sha(key + '/old')])}

# Artwork picked since the push (store_documents icon-artwork): the icon row then holds the picked drawing.
for record in [r for r in records if not r.get('uploaded_icon')][5:14]:
    mode = rng.choice(['use_edited', 'use_upload', 'use_org', 'stale'])
    baseline = record['svg_sha256']
    if mode == 'use_edited':
        picked = sha(record['key'] + '/edited')
        document = {'source_mode': mode, 'source_svg_sha256': baseline, 'selected_svg_sha256': picked}
    elif mode == 'use_upload':
        picked = sha(record['key'] + '/upload')
        document = {'source_mode': mode, 'source_svg_sha256': baseline, 'selected_upload': {'svg_sha256': picked}}
    elif mode == 'use_org':
        picked = baseline
        document = {'source_mode': mode, 'source_svg_sha256': baseline}
    else:
        # Made for a drawing the icon has since been rebuilt from: no longer applies.
        picked = baseline
        document = {'source_mode': 'use_edited', 'source_svg_sha256': sha(record['key'] + '/older'), 'selected_svg_sha256': sha('x')}
        if baseline not in graphs:
            graphs.append(baseline)
    current[record['key']] = picked
    artwork.append({'key': record['key'], 'document': document})

C = lambda **params: params  # noqa: E731
cases = [C(), C(family='solo'), C(family=''), C(family='side_main'), C(family='side_sub'), C(family='sub', sort='newest'),
         *[C(family='', status=s) for s in ('ready', 'failed', 'pending', 'approve', 'rejected')],
         C(family='', q='cup'), C(family='', q='ARROW'), C(family='', q='revision'), C(family='', category='food'), C(family='', category='nope'),
         *[C(family='', symmetry=s) for s in ('symmetric', 'vertical', 'horizontal', 'both', 'asymmetric', 'unknown')],
         *[C(family='', strokes=s) for s in ('1-3', '4-6', '7-10', '11+', 'unknown')],
         C(family='', keyshape='CIRCLE'), C(family='', author='unknown'), C(family='', author='gpt-x'),
         C(family='', revision='variant'), C(family='', revision='original'), C(family='', reference='with'), C(family='', reference='without'),
         *[C(family='', artwork=a) for a in ('original', 'modified', 'edited', 'uploaded', 'work_fix')],
         *[C(family='', reason=r) for r in ('bad-stroke', 'meaning', 'manual-fix-request', 'other', 'missing', 'cannot-fix')],
         C(family='', reviewer='ray'), C(family='', reviewer='hina', status='rejected'), C(family='', icon_feedback_by='jakes'),
         C(family='', status='pending', pending_feedback='with'), C(family='', status='pending', pending_feedback='without'),
         *[C(family='', sort=s) for s in ('newest', 'oldest', 'modified-newest', 'modified-oldest', 'strokes-asc', 'strokes-desc',
                                         'segments-asc', 'segments-desc')],
         C(family='', limit=24, offset=24), C(family='', limit=24, offset=48), C(family='solo', view='versions'),
         C(family='', view='versions', limit=24), C(family='', view='versions', q='cup'), C(family='', view='versions', author='gpt-x'),
         C(family='', category='food', status='approve', sort='strokes-desc', strokes='1-3')]

fixture = {'records': records, 'current_sha': current, 'reviews': reviews, 'splits': splits, 'feedback': feedback,
           'artwork': artwork, 'graphs': sorted(set(graphs)), 'facets': facets, 'cases': cases}
(HERE / 'icon-query.json').write_text(json.dumps(fixture, indent=1) + '\n')
print(f'{len(records)} icons, {len(reviews)} reviews, {len(feedback)} feedback, {len(artwork)} picks, {len(cases)} cases')
