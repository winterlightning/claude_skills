#!/usr/bin/env python3
"""Prepare and migrate reviewed container+symbol references on a local D1 snapshot.

prepare extracts Dots' container split cases into input.json. migrate defaults to
a read-only rehearsal; --apply backs up and changes the specified local database.
No network requests, drawings, approvals, review changes or deployments.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from contextlib import closing
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from icon_set.scripts.import_rejected_review import (  # noqa: E402
    SOURCE_SCHEMA, SHA256, encode, read_review, text, write_bundle,
)
from icon_set.scripts.rejected_to_pending import backup_database  # noqa: E402

SCHEMA = 'pictographic-container-reference-migration/v1'
ROLES = ('container', 'symbol')

def roles_for(item):
    return ('main', 'sub') if item['review'].get('combination_type') == 'side_combination' else ROLES



def prepare(review_path, output, expect_count=90):
    review, digest = read_review(review_path)
    metadata = review.get('metadata', review.get('source_metadata'))
    handoff = review.get('schema') == 'pictographic-correction-handoff/v1'
    if not isinstance(metadata, dict) or metadata.get('schema') != SOURCE_SCHEMA:
        raise ValueError('Unsupported review source schema')
    if not isinstance(review.get('records'), list):
        raise ValueError('Review records must be an array')
    rows, keys = [], set()
    for record in review['records']:
        if not isinstance(record, dict) or not text(record.get('key')) or record['key'] in keys:
            raise ValueError('Review records need unique nonempty keys')
        keys.add(record['key'])
        if record.get('recommended_action') != 'split_into_components' or record.get('combination_type') != 'container_combination':
            continue
        if not handoff and record.get('recommendation_only') is not True:
            raise ValueError('Expected a recommendation-only source record')
        rows.append({'icon': record['key'], 'svg_sha256': record.get('current_effective_svg_sha256'),
                     'source_reference_id': record.get('source_reference_id'),
                     'concept': record.get('current_name'), 'review': record})
    if len(rows) != expect_count:
        raise ValueError(f'Expected {expect_count} container records, got {len(rows)}')
    data = {'schema': SCHEMA, 'source_sha256': digest, 'source_metadata': metadata, 'records': rows}
    raw = Path(review_path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != digest:
        raise ValueError('Review changed during preparation')
    checks = []
    for item in rows:
        parts, issues = selected_parts(item, None)
        checks.append({'icon': item['icon'], 'parts': parts, 'issues': issues,
                       'status': 'held' if issues else 'ready_for_database_check'})
    preflight = {'source_sha256': digest, 'database_checked': False,
                 'counts': dict(Counter(row['status'] for row in checks)), 'records': checks}
    write_bundle(output, {'input.json': encode(data), 'source-review.json': raw,
                          'component-check.json': encode(preflight)})
    return data


def load_input(path):
    data, digest = read_review(path)
    if not isinstance(data, dict) or data.get('schema') != SCHEMA or not isinstance(data.get('records'), list):
        raise ValueError(f'Expected {SCHEMA} input')
    keys = set()
    for item in data['records']:
        if not isinstance(item, dict) or not text(item.get('icon')) or item['icon'] in keys:
            raise ValueError('Migration records need distinct nonempty icon keys')
        keys.add(item['icon'])
        review = item.get('review')
        if not isinstance(review, dict) or review.get('recommended_action') != 'split_into_components' \
                or review.get('combination_type') != 'container_combination':
            raise ValueError(f'{item["icon"]}: not a container split recommendation')
        for field, original in (('icon', 'key'), ('svg_sha256', 'current_effective_svg_sha256'),
                                ('source_reference_id', 'source_reference_id')):
            if item.get(field) != review.get(original):
                raise ValueError(f'{item["icon"]}: {field} disagrees with its source review')
    return data, digest


def load_decisions(path, known):
    if path is None:
        return {}
    data, _ = read_review(path)
    if not isinstance(data, dict) or not isinstance(data.get('decisions'), dict):
        raise ValueError('Decisions must be {"decisions": {"icon/key": {...}}}')
    for key, choice in data['decisions'].items():
        fields = ('container_reference_id', 'symbol_reference_id', 'reason', 'reviewed_by')
        if key not in known or not isinstance(choice, dict) or not all(text(choice.get(f)) for f in fields):
            raise ValueError(f'{key}: a decision needs both reference IDs, reason and reviewed_by')
    return data['decisions']


def selected_parts(item, choice):
    """Known identity is enough for registration; this never picks a drawing for assembly."""
    roles = roles_for(item)
    if choice:
        return {role: choice[role + '_reference_id'] for role in roles}, []
    components = item['review'].get('components')
    if isinstance(components, list):
        components = [dict(p, role='sub') if isinstance(p, dict) and p.get('role') == 'side_sub' and roles == ('main', 'sub') else p for p in components]
    if not isinstance(components, list) or len(components) != 2 \
            or not all(isinstance(p, dict) for p in components) \
            or sorted(str(p.get('role')) for p in components) != list(roles):
        return None, ['needs_' + '_and_'.join(roles) + '_decision']
    parts, issues = {}, []
    for part in components:
        role = part['role']
        if part.get('components'):
            issues.append(role + ':nested_component')
        if part.get('match_status') != 'verified_existing' or not text(part.get('reference_id')):
            issues.append(role + ':reference_unresolved')
        else:
            parts[role] = part['reference_id']
        if part.get('match_kind') == 'functional_equivalent' or any(
                part.get(field) for field in ('limitation', 'match_limitation', 'match_limitations')):
            issues.append(role + ':match_needs_decision')
        if part.get('requires_role_adaptation') is not False:
            issues.append(role + ':role_adaptation_needs_decision')
    return parts, issues


def validate_schema(db):
    required = {
        'references': {'reference_id', 'kind', 'concept', 'source'},
        'reference_parts': {'reference_id', 'role', 'part_reference_id', 'icon', 'updated_at', 'updated_by'},
        'icons': {'key', 'name', 'svg_sha256'},
        'icon_references': {'icon', 'reference_id'},
        'reviews': {'icon', 'svg_sha256', 'status'},
        'split_requests': {'icon', 'svg_sha256', 'active'},
        'activity_log': {'username', 'action', 'icon', 'details', 'created_at'},
        'review_data_migrations': {'id', 'applied_at', 'details'},
    }
    for table, columns in required.items():
        found = {row[1] for row in db.execute(f'PRAGMA table_info("{table}")')}
        if not columns <= found:
            raise ValueError(f'Unsupported snapshot: {table} is missing {sorted(columns - found)}')


def matching_pairs(db, parts, roles=ROLES):
    # Match ordered roles, never a name, drawing key, reversed pair, side pair or extra-part composite.
    return [row[0] for row in db.execute('''
        SELECT r.reference_id FROM "references" r JOIN reference_parts p USING(reference_id)
        WHERE r.kind='combination' GROUP BY r.reference_id HAVING count(*)=2
        AND sum(p.role=? AND p.part_reference_id=?)=1
        AND sum(p.role=? AND p.part_reference_id=?)=1 ORDER BY r.reference_id
    ''', (roles[0], parts[roles[0]], roles[1], parts[roles[1]]))]


def migrate_rows(db, data, input_digest, actor, choices):
    """Caller owns the transaction (an in-memory rehearsal or a locked local database)."""
    validate_schema(db)
    selected = {item['icon']: selected_parts(item, choices.get(item['icon'])) for item in data['records']}
    proposed = defaultdict(set)
    for item in data['records']:
        parts, issues = selected[item['icon']]
        if not issues and text(item.get('source_reference_id')):
            proposed[item['source_reference_id']].add(tuple((role, parts[role]) for role in roles_for(item)))
    results = []
    now = datetime.now(timezone.utc).isoformat()
    for item in data['records']:
        roles = roles_for(item)
        key, source = item['icon'], item.get('source_reference_id')
        parts, issues = selected[key]
        issues = list(issues)
        row = {'icon': key, 'source_reference_id': source, 'parts': parts, 'issues': issues,
               'decision': choices.get(key), 'status': 'held'}
        results.append(row)
        if not text(source):
            issues.append('source_reference_missing')
        elif len(proposed[source]) > 1:
            issues.append('conflicting_input_for_source_reference')
        if issues:
            continue
        if parts[roles[0]] == parts[roles[1]] or source in parts.values():
            issues.append('self_or_duplicate_component_reference')
            continue
        icon = db.execute('SELECT name, svg_sha256 FROM icons WHERE key=?', (key,)).fetchone()
        if not icon or not isinstance(item.get('svg_sha256'), str) or not SHA256.fullmatch(item['svg_sha256']) or icon[1] != item['svg_sha256']:
            issues.append('source_drawing_changed_or_missing')
            continue
        # A rejection of an older revision does not authorize changing the current one.
        rejected = db.execute("SELECT 1 FROM reviews WHERE icon=? AND svg_sha256=? AND status='rejected'",
                              (key, item['svg_sha256'])).fetchone()
        split = db.execute('SELECT 1 FROM split_requests WHERE icon=? AND svg_sha256=? AND active=1',
                           (key, item['svg_sha256'])).fetchone()
        if not rejected and not split:
            issues.append('source_is_no_longer_rejected')
            continue
        if not db.execute('SELECT 1 FROM icon_references WHERE icon=? AND reference_id=?', (key, source)).fetchone():
            issues.append('source_reference_not_linked_to_icon')
            continue
        for role in roles:
            reference = db.execute('SELECT kind FROM "references" WHERE reference_id=?', (parts[role],)).fetchone()
            if not reference:
                issues.append(role + ':reference_missing_in_database')
            elif reference[0] != 'single':
                issues.append(role + ':reference_is_a_combination')
        if issues:
            continue
        matches = matching_pairs(db, parts, roles)
        if len(matches) > 1:
            issues.append('multiple_existing_combinations')
            row['candidate_reference_ids'] = matches
            continue
        if matches:
            row.update(status='reused', combination_reference_id=matches[0])
            continue
        source_row = db.execute('SELECT kind FROM "references" WHERE reference_id=?', (source,)).fetchone()
        existing = db.execute('SELECT role, part_reference_id FROM reference_parts WHERE reference_id=?', (source,)).fetchall()
        if existing or (source_row and source_row[0] != 'single'):
            issues.append('source_already_has_different_combination')
            continue
        # The original reference is the combination; keep its ID and any metadata/image location.
        if source_row:
            db.execute('UPDATE "references" SET kind=\'combination\' WHERE reference_id=?', (source,))
            operation = 'classified_existing_reference'
        else:
            db.execute('INSERT INTO "references"(reference_id,kind,concept,source) VALUES (?,\'combination\',?,?)',
                       (source, item.get('concept') or icon[0], 'rejected-review'))
            operation = 'created_reference'
        for role in roles:
            db.execute('''INSERT INTO reference_parts
                (reference_id,role,part_reference_id,updated_at,updated_by) VALUES (?,?,?,?,?)''',
                       (source, role, parts[role], now, actor))
        details = {'source_icon': key, 'source_svg_sha256': item['svg_sha256'],
                   'combination_reference_id': source, 'parts': parts, 'input_sha256': input_digest,
                   'decision': choices.get(key), 'operation': operation}
        encoded = json.dumps(details, sort_keys=True)
        migration_id = 'combination-review:' + hashlib.sha256(encoded.encode()).hexdigest()
        db.execute('INSERT INTO review_data_migrations(id,applied_at,details) VALUES (?,?,?)',
                   (migration_id, now, encoded))
        db.execute('INSERT INTO activity_log(username,action,icon,details,created_at) VALUES (?,?,?,?,?)',
                   (actor, 'combination_reference_migration', key, encoded, now))
        row.update(status='registered', combination_reference_id=source, operation=operation)
    return {'schema': SCHEMA, 'input_sha256': input_digest,
            'counts': dict(Counter(row['status'] for row in results)), 'records': results}


def run(database, data, digest, actor, choices=None, apply=False, runner=migrate_rows):
    database = Path(database).resolve()
    if not database.is_file():
        raise ValueError('Database must be an existing local D1 snapshot')
    if not text(actor):
        raise ValueError('actor must be nonempty')
    backup = None
    if not apply:
        # Rehearse sequentially in a copy so same-batch pairs also deduplicate.
        with closing(sqlite3.connect(database.as_uri() + '?mode=ro', uri=True)) as source, \
                closing(sqlite3.connect(':memory:')) as scratch:
            source.backup(scratch)
            report = runner(scratch, data, digest, actor, choices or {})
            scratch.rollback()
    else:
        with closing(sqlite3.connect(database.as_uri() + '?mode=rw', uri=True, isolation_level=None)) as db:
            db.execute('BEGIN IMMEDIATE')
            try:
                validate_schema(db)
                backup = backup_database(database)
                report = runner(db, data, digest, actor, choices or {})
                db.commit()
            except BaseException:
                db.rollback()
                if backup:
                    print(f'Rolled back. Backup retained: {backup}', file=sys.stderr)
                raise
    return {**report, 'mode': 'applied_local' if apply else 'dry_run',
            'backup': str(backup) if backup else None}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    prep = sub.add_parser('prepare', help='Extract container split cases from the visual review')
    prep.add_argument('--review', type=Path, required=True)
    prep.add_argument('--out', type=Path, required=True)
    prep.add_argument('--expect-count', type=int, default=90)
    migrate = sub.add_parser('migrate', help='Dry-run or apply to an explicit local D1 snapshot')
    migrate.add_argument('--input', type=Path, required=True)
    migrate.add_argument('--db', type=Path, required=True)
    migrate.add_argument('--actor', required=True)
    migrate.add_argument('--decisions', type=Path, help='Explicit resolutions of uncertain component matches')
    migrate.add_argument('--apply', action='store_true', help='Back up and migrate this local database transactionally')
    args = parser.parse_args(argv)
    try:
        if args.command == 'prepare':
            data = prepare(args.review, args.out, args.expect_count)
            report = {'input': str(args.out / 'input.json'), 'records': len(data['records'])}
        else:
            data, digest = load_input(args.input)
            choices = load_decisions(args.decisions, {item['icon'] for item in data['records']})
            report = run(args.db, data, digest, args.actor, choices, args.apply)
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    except (OSError, ValueError, sqlite3.Error) as error:
        parser.exit(1, f'error: {error}\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
