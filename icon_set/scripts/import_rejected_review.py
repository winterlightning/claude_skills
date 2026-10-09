#!/usr/bin/env python3
"""Import a visual rejection review into offline correction worklists.

This is a files-only review handoff. It never fetches evidence, calls an API,
opens a database, creates drawings, or changes the review status of an icon.
See docs/rejected-review-import.md for the input contract and review workflow.
"""
from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import re
from tempfile import TemporaryDirectory
from urllib.parse import urlencode

SOURCE_SCHEMA = 'pictographic-rejected-visual-review/v1'
PLAN_SCHEMA = 'pictographic-rejected-correction-plan/v1'
SPLIT = 'split_into_components'
GROUPS = ('container_combinations', 'side_combinations', 'other_recommendations', 'unresolved_splits')
KINDS = {'container_combination': GROUPS[0], 'side_combination': GROUPS[1]}
KNOWN_ACTIONS = {SPLIT, 'retain_family_review', 'author_new_drawing', 'recategorize_family', 'unknown'}
SHA256 = re.compile(r'^[0-9a-f]{64}$')


def text(value):
    return isinstance(value, str) and bool(value.strip())


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'Duplicate JSON field: {key}')
        result[key] = value
    return result


def invalid_constant(value):
    raise ValueError(f'Invalid JSON constant: {value}')


def read_review(path):
    raw = Path(path).read_bytes()
    data = json.loads(raw, object_pairs_hook=unique_object, parse_constant=invalid_constant)
    return data, hashlib.sha256(raw).hexdigest()


def component_rows(components, location='components'):
    """Retain parent and child components; never flatten a nested split into a pair."""
    if not isinstance(components, list):
        raise ValueError(f'{location} must be an array')
    for index, part in enumerate(components):
        path = f'{location}[{index}]'
        if not isinstance(part, dict):
            raise ValueError(f'{path} must be an object')
        yield path, part
        if 'components' in part:
            yield from component_rows(part['components'], path + '.components')


def normalized_role(part, kind):
    role = part.get('role')
    # This is a display alias within SIDE pairs only, never a symbol -> sub conversion.
    if kind == 'side_combination' and role == 'side_sub':
        return 'sub'
    return role if isinstance(role, str) else None


def component_check(path, part, kind):
    issues = []
    status, reference = part.get('match_status'), part.get('reference_id')
    verified = status == 'verified_existing' and text(reference)
    if status == 'ambiguous':
        issues.append('ambiguous_reference')
    elif status != 'verified_existing':
        issues.append('reference_unverified')
    elif not verified:
        issues.append('verified_reference_missing_id')
    if not verified and part.get('absence_proven') is not True:
        issues.append('reference_absence_not_proven')
    if part.get('assembly_readiness_verified') is not True:
        issues.append('assembly_readiness_unverified')
    if part.get('requires_role_adaptation') is True:
        issues.append('role_adaptation_required')
    elif part.get('requires_role_adaptation') is not False:
        issues.append('role_adaptation_unassessed')
    if part.get('match_kind') == 'functional_equivalent':
        issues.append('functional_equivalent_contour_review')
    if part.get('limitation'):
        issues.append('reference_limitation_review')
    if part.get('components'):
        issues.append('nested_component_review')
    if not text(part.get('visual_description')):
        issues.append('visual_description_missing')
    role = normalized_role(part, kind)
    allowed = {'container', 'symbol'} if kind == 'container_combination' else {'main', 'sub'}
    if kind not in KINDS or role not in allowed:
        issues.append('component_role_review')
    return {'path': path, 'role': role, 'verified_reference_id': reference if verified else None,
            'issues': issues}


def record_plan(record):
    action, kind = record.get('recommended_action'), record.get('combination_type')
    group = (KINDS.get(kind, 'unresolved_splits') if action == SPLIT else 'other_recommendations')
    issues = ['human_review_required']
    if record.get('current_state') != 'rejected':
        issues.append('source_state_is_not_rejected')
    sha = record.get('current_effective_svg_sha256')
    if not isinstance(sha, str) or not SHA256.fullmatch(sha):
        issues.append('source_revision_missing_or_invalid')
    if not text(record.get('source_reference_id')):
        issues.append('source_reference_missing')
    if action not in KNOWN_ACTIONS:
        issues.append('unrecognized_action')
    elif action == 'unknown':
        issues.append('recommendation_unresolved')
    elif action == 'author_new_drawing':
        issues.append('drawing_brief_requires_review')
    elif action == 'recategorize_family':
        issues.append('family_change_requires_review')
    components = record.get('components', [])
    checks = [component_check(path, part, kind) for path, part in component_rows(components)]
    if action == SPLIT:
        expected = {'container', 'symbol'} if kind == 'container_combination' else {'main', 'sub'}
        if kind not in KINDS:
            issues.append('combination_type_unresolved')
        roles = [normalized_role(part, kind) for part in components]
        if len(roles) != 2 or set(roles) != expected:
            issues.append('split_roles_require_review')
        if any(part.get('components') for part in components):
            issues.append('nested_split_requires_review')
        # Neither existing write route represents this reviewed reference mapping faithfully:
        # reject-combination uses container+sub briefs; pair creates side-only draw: placeholders.
        issues.append('reference_mapping_requires_api_support')
    return {
        'key': record['key'], 'group': group, 'status': 'pending_human_review',
        'source_revision': sha, 'issues': issues, 'component_checks': checks,
        'read_checks': [
            {'method': 'GET', 'path': '/api/icon?' + urlencode({'key': record['key']})},
            {'method': 'GET', 'path': '/api/review-detail?' + urlencode({'icon': record['key']})},
        ],
        # Exact original evidence and all unknown fields survive the import.
        'review': deepcopy(record),
    }


def build_plan(data, source_sha256, expected=None):
    if not isinstance(data, dict) or not isinstance(data.get('metadata'), dict):
        raise ValueError('Expected {metadata, records}')
    if data['metadata'].get('schema') != SOURCE_SCHEMA:
        raise ValueError(f'Expected metadata.schema={SOURCE_SCHEMA}')
    if not isinstance(data.get('records'), list):
        raise ValueError('records must be an array')
    groups = {name: [] for name in GROUPS}
    keys, references, actions = set(), {}, Counter()
    for index, record in enumerate(data['records']):
        if not isinstance(record, dict) or not text(record.get('key')):
            raise ValueError(f'records[{index}] needs a nonempty key')
        if record['key'] in keys:
            raise ValueError(f'Duplicate reviewed icon: {record["key"]}')
        keys.add(record['key'])
        if record.get('recommendation_only') is not True:
            raise ValueError(f'{record["key"]}: recommendation_only must be true')
        if not text(record.get('recommended_action')):
            raise ValueError(f'{record["key"]}: recommended_action must be nonempty text')
        if record.get('combination_type') is not None and not isinstance(record['combination_type'], str):
            raise ValueError(f'{record["key"]}: combination_type must be text or null')
        try:
            plan = record_plan(record)
        except (ValueError, RecursionError) as error:
            raise ValueError(f'{record["key"]}: {error}') from error
        groups[plan['group']].append(plan)
        actions[record['recommended_action']] += 1
        for check, (_, part) in zip(plan['component_checks'], component_rows(record.get('components', []))):
            reference = check['verified_reference_id']
            if reference is not None:
                references.setdefault(reference, []).append({
                    'key': record['key'], 'component_path': check['path'], 'role': check['role'],
                    'matched_key': part.get('matched_key'), 'match_kind': part.get('match_kind'),
                    'issues': check['issues'],
                })
    counts = {'total': len(keys), **{name: len(rows) for name, rows in groups.items()},
              'split_into_components': actions[SPLIT]}
    for name, count in (expected or {}).items():
        actual = counts.get(name, actions.get(name, 0))
        if actual != count:
            raise ValueError(f'Expected {name}={count}, got {actual}; nothing written')
    return {'schema': PLAN_SCHEMA, 'mode': 'files_only', 'source_sha256': source_sha256,
            'source_metadata': deepcopy(data['metadata']), 'counts': counts,
            'actions': dict(sorted(actions.items())), 'groups': groups,
            'reference_index': {'verification_source': 'supplied_review', 'independently_rechecked': False,
                                'references': dict(sorted(references.items()))}}


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + '\n').encode('utf-8')


def bundle_files(plan, source_bytes):
    summary = {key: value for key, value in plan.items() if key not in ('groups', 'reference_index')}
    summary['worklists'] = {group: group + '.json' for group in GROUPS}
    summary['reference_index'] = 'verified-references.json'
    files = {'source-review.json': source_bytes, 'manifest.json': encode(summary),
             'verified-references.json': encode(plan['reference_index'])}
    files.update({group + '.json': encode(records) for group, records in plan['groups'].items()})
    counts = plan['counts']
    files['README.md'] = ('# Rejected-icon correction review\n\n'
        f"Imported {counts['total']} recommendation records; {counts[SPLIT]} request a split.\n\n"
        f"- Container + symbol: {counts['container_combinations']}\n"
        f"- Main + side-sub: {counts['side_combinations']}\n"
        f"- Other recommendations: {counts['other_recommendations']}\n"
        f"- Splits with unresolved type: {counts['unresolved_splits']}\n\n"
        'Every record remains pending human review. No API or database writes were made.\n'
        'Reference identities come from the supplied review and have not been independently rechecked.\n'
        'Candidate IDs remain candidates; functional equivalence does not establish matching contour.\n'
        'Inspect the source pixels, reference limitations, role adaptation and assembly readiness before acting.\n'
        'The GET paths in each record are review checks only; the importer does not execute them.\n'
        'Compare the current icon SHA and review state with the saved source before any later correction.\n'
        'See docs/rejected-review-import.md in the repository for API compatibility limits.\n').encode('utf-8')
    return files


def write_bundle(output, files):
    """Stage a complete new bundle; identical retries are no-ops and edited work is protected."""
    output = Path(output)
    if output.is_symlink():
        raise ValueError('Output must not be a symlink')
    if output.exists():
        if output.is_dir() and all((output / name).is_file() and not (output / name).is_symlink()
                                   and (output / name).read_bytes() == content for name, content in files.items()):
            return False
        raise FileExistsError(f'{output}: existing bundle differs; choose another --out directory')
    output.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix='.rejected-review-', dir=output.parent) as temp:
        staged = Path(temp) / 'bundle'
        staged.mkdir()
        for name, content in files.items():
            (staged / name).write_bytes(content)
        os.rename(staged, output)
    return True


def expected_count(value):
    name, separator, raw = value.partition('=')
    allowed = set(GROUPS) | KNOWN_ACTIONS | {'total'}
    if separator != '=' or name not in allowed or not raw.isdigit():
        raise argparse.ArgumentTypeError('Use a known group/action or total followed by = and a nonnegative count')
    return name, int(raw)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--file', required=True, type=Path, help='Reviewed JSON with metadata and records')
    parser.add_argument('--out', required=True, type=Path, help='New local review bundle directory')
    parser.add_argument('--expect-count', action='append', type=expected_count, default=[], metavar='NAME=N')
    args = parser.parse_args(argv)
    try:
        data, digest = read_review(args.file)
        plan = build_plan(data, digest, dict(args.expect_count))
        raw = args.file.read_bytes()
        if hashlib.sha256(raw).hexdigest() != digest:
            raise ValueError('Source changed during import; nothing written')
        changed = write_bundle(args.out, bundle_files(plan, raw))
    except (OSError, ValueError, RecursionError) as error:
        parser.exit(1, f'error: {error}\n')
    print(json.dumps({'directory': str(args.out.absolute()), 'created': changed, 'counts': plan['counts'],
                      'mode': 'files_only'}, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
