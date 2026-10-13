#!/usr/bin/env python3
"""Rehearse/apply all reviewed corrections on an explicit local D1 copy.

Reference registration and text routing are data migrations. Drawing repairs,
uncertain references and reviewer decisions remain explicit report items.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from cloud.migrate import migrate_container_review as combinations
from icon_set.scripts.import_rejected_review import read_review, text, encode

SCHEMA = 'pictographic-all-rejected-migration/v1'


def load_source(path, expect_count=379):
    data, digest = read_review(path)
    if not isinstance(data, dict) or data.get('schema') != 'pictographic-correction-handoff/v1':
        raise ValueError('Expected pictographic-correction-handoff/v1')
    records = data.get('records')
    if not isinstance(records, list) or len(records) != expect_count:
        raise ValueError(f'Expected {expect_count} records')
    keys = set()
    for r in records:
        if not isinstance(r, dict) or not text(r.get('key')) or r['key'] in keys:
            raise ValueError('Records need unique nonempty keys')
        keys.add(r['key'])
        if not isinstance(r.get('current_effective_svg_sha256'), str) or not combinations.SHA256.fullmatch(r['current_effective_svg_sha256']):
            raise ValueError(f'{r["key"]}: missing drawing revision')
    return data, digest


def item(r):
    return {'icon': r['key'], 'svg_sha256': r['current_effective_svg_sha256'],
            'source_reference_id': r.get('source_reference_id'), 'concept': r['current_name'], 'review': r}


def source_issues(db, r):
    row = db.execute('SELECT name,family,svg_sha256,state FROM icons WHERE key=?', (r['key'],)).fetchone()
    if row is None:
        return ['source_missing']
    issues = []
    if row[2] != r['current_effective_svg_sha256']:
        issues.append('source_drawing_changed')
    if row[0] != r['current_name']:
        issues.append('source_name_changed')
    # Effective state is important: any historic rejection cannot override a new approval.
    if row[3] != 'rejected':
        issues.append('source_no_longer_rejected')
    current = db.execute('SELECT status FROM reviews WHERE icon=? AND svg_sha256=?', (r['key'], row[2])).fetchone()
    if current and current[0] in ('approve', 'claimed'):
        issues.append('current_revision_approved_or_claimed')
    return issues


def audit(db, key, digest, actor, operation, before, after):
    details = {'source_icon': key, 'input_sha256': digest, 'operation': operation,
               'before': before, 'after': after}
    payload = json.dumps(details, sort_keys=True)
    identity = 'rejected-routing:' + hashlib.sha256(payload.encode()).hexdigest()
    now = datetime.now(timezone.utc).isoformat()
    db.execute('INSERT INTO review_data_migrations VALUES (?,?,?)', (identity, now, payload))
    db.execute('INSERT INTO activity_log(username,action,icon,details,created_at) VALUES (?,?,?,?,?)',
               (actor, 'rejected_review_routing', key, payload, now))


def font_family(db, actor, create=True):
    rows = db.execute("SELECT id,canvas_size FROM upload_families WHERE lower(trim(name))='font 48'").fetchall()
    if len(rows) > 1 or (rows and rows[0][1] != 48):
        raise ValueError('Conflicting Font 48 family definitions')
    if rows:
        return rows[0][0]
    if db.execute("SELECT 1 FROM upload_families WHERE id='font-48'").fetchone():
        raise ValueError('font-48 family ID is already used by a different family')
    if not create:
        return 'font-48'
    db.execute('INSERT INTO upload_families VALUES (?,?,?,?,?)',
               ('font-48', 'Font 48', 48, datetime.now(timezone.utc).isoformat(), actor))
    return 'font-48'


def route(db, r, digest, actor):
    d = r['latest_diagnosis']
    row = db.execute('SELECT family,side_role,canvas_size,record,card,version_group FROM icons WHERE key=?', (r['key'],)).fetchone()
    old_family, old_role, canvas, raw, card_raw, group = row
    target = d.get('proposed_section')
    if target == 'Font 48':
        token = d.get('text_identity') or {}
        if token.get('character_count') != 1 or canvas != 48:
            return 'held', ['font_character_or_canvas_needs_review']
        family, role = font_family(db, actor, create=False), None
    elif target == 'Sub-icon':
        token = d.get('text_identity') or {}
        if not isinstance(token.get('character_count'), int) or token['character_count'] <= 1:
            return 'held', ['multi_character_identity_needs_review']
        # Sub-icon is the existing side_sub list, filtered by side_role='sub'.
        # Native text keeps its actual canvas/profile; do not relabel a 48px drawing SUB32.
        family, role = old_family, 'sub'
    else:
        return 'held', ['unsupported_routing_target']
    before, after = {'family': old_family, 'side_role': old_role}, {'family': family, 'side_role': role}
    if before == after:
        return 'already_routed', []
    if old_family != r['current_family']:
        return 'held', ['source_family_changed']
    if target == 'Font 48':
        font_family(db, actor)
    record, card = json.loads(raw), json.loads(card_raw or '{}')
    record.update(after)
    card.update(after)
    root = record.get('variant_root') or record.get('variant_of') or record.get('icon_id')
    db.execute('UPDATE icons SET family=?,side_role=?,record=?,card=?,version_group=? WHERE key=?',
               (family, role, json.dumps(record, ensure_ascii=False), json.dumps(card, ensure_ascii=False),
                family + '/' + root, r['key']))
    audit(db, r['key'], digest, actor, 'route_text', before, after)
    return 'routed', []


def recount(db):
    # Same groupings as the Worker's refresh/count migration, with original state untouched.
    db.execute('DELETE FROM icon_counts')
    db.execute("""INSERT INTO icon_counts SELECT COALESCE(family,''),COALESCE(side_role,''),style,
        COALESCE(state,''),COALESCE(category,''),build_failed,COUNT(*) FROM icons GROUP BY 1,2,3,4,5,6""")
    db.execute("DELETE FROM icon_facet_counts WHERE kind='family'")
    db.execute("INSERT INTO icon_facet_counts SELECT 'family',COALESCE(family,''),COUNT(*) FROM icons GROUP BY family")


def migrate_all(db, data, digest, actor, choices):
    combinations.validate_schema(db)
    results, split = [], []
    for r in data['records']:
        d = r.get('latest_diagnosis') or {}
        row = {'icon': r['key'], 'group': r['work_group'], 'status': 'held', 'issues': source_issues(db, r),
               'required_fix': d.get('required_fix') or r.get('exact_new_drawing_brief') or r.get('reason_wrong'),
               'artwork_required_fix': d.get('artwork_required_fix'),
               'decision_question': d.get('decision_question')}
        results.append(row)
        if row['issues']:
            continue
        if r['recommended_action'] == 'split_into_components':
            family = db.execute('SELECT family FROM icons WHERE key=?', (r['key'],)).fetchone()[0]
            if family != r['current_family']:
                row['issues'].append('source_family_changed')
                continue
            if r.get('combination_type') not in ('container_combination', 'side_combination'):
                row['issues'].append('unknown_combination_type')
            else:
                candidate = item(r)
                if not candidate['source_reference_id']:
                    links = db.execute('SELECT reference_id FROM icon_references WHERE icon=?', (r['key'],)).fetchall()
                    if len(links) == 1:
                        candidate['source_reference_id'] = links[0][0]
                split.append(candidate)
            continue
        if d.get('user_decision_needed') or d.get('execution_lane') == 'decision_required':
            row['issues'].append('human_decision_required')
        elif d.get('proposed_section') in ('Font 48', 'Sub-icon'):
            row['status'], row['issues'] = route(db, r, digest, actor)
            if d.get('artwork_required_fix'):
                row['issues'].append('artwork_repair_still_required')
        elif r['work_group'] == 'plausible_mistaken_rejection':
            row['status'] = 'human_reverification'
            row['issues'].append('rejection_preserved_no_demonstrated_defect')
        elif r['recommended_action'] == 'recategorize_family':
            row['issues'].append('canvas_role_adaptation_requires_artwork_review')
        elif d.get('execution_lane') == 'artwork_fix_brief_ready' or r['recommended_action'] == 'author_new_drawing':
            row['status'] = 'artwork_required'
            row['issues'].append('drawing_repair_not_a_data_migration')
        else:
            row['issues'].append('unresolved_recommendation')
    if split:
        combo_report = combinations.migrate_rows(db, {'records': split}, digest, actor, choices)
        by_key = {row['icon']: row for row in combo_report['records']}
        for row in results:
            if row['icon'] in by_key:
                row.update(by_key[row['icon']])
    if any(row['status'] == 'routed' for row in results):
        recount(db)
    return {'schema': SCHEMA, 'input_sha256': digest, 'counts': dict(Counter(r['status'] for r in results)),
            'records': results}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--review', type=Path, required=True)
    parser.add_argument('--db', type=Path, required=True)
    parser.add_argument('--actor', required=True)
    parser.add_argument('--expect-count', type=int, default=379)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        data, digest = load_source(args.review, args.expect_count)
        # Preflight the report destination before any database write.
        if args.report.exists():
            raise ValueError('Report already exists; use a new path')
        if not args.report.parent.is_dir():
            raise ValueError('Report parent directory must exist')
        report = combinations.run(args.db, data, digest, args.actor, apply=args.apply, runner=migrate_all)
        with args.report.open('xb') as output:
            output.write(encode(report))
        print(json.dumps({'report': str(args.report), 'counts': report['counts'], 'mode': report['mode']}))
    except (ValueError, OSError, sqlite3.Error) as error:
        parser.exit(1, f'error: {error}\n')


if __name__ == '__main__':
    main()
