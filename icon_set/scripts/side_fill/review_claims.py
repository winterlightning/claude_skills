"""Durable pair claims and serialized commits for the side review runner."""

from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
import fcntl
import hashlib
import json
import os
import random
import shutil
import sys
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

from .ai_variant_review import (DEFAULT_DECISIONS, DEFAULT_INPUT,
                                DEFAULT_LAYOUT_OUTPUT, REVIEW_PROTOCOL,
                                candidate_has_genuine_fill, candidate_sources,
                                preview_one, sha, stress_current)
from .adaptive_overlap import DEFAULT_LAYOUTS, fill_path, source_path
from .pair_layout_review import DEFAULT_SPECS

ROOT = WORK
RUN_DIR = WORK / 'ai-review-run'
QUEUE = RUN_DIR / 'queue.json'
STATE = RUN_DIR / 'state.json'
ELIGIBLE = {'pending', 'pending_unavailable', 'stale_decision', 'needs_repair'}
MIN_AI_SUB_SIZE = 28


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(value):
    if value is None:
        return None
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                          separators=(',', ':')).encode()).hexdigest()


def read_json(path, default=None):
    return json.loads(path.read_text()) if path.exists() else default


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f'.{path.name}.{os.getpid()}.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    os.replace(temporary, path)


@contextmanager
def locked_state():
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    with (RUN_DIR / 'state.lock').open('a+') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        state = read_json(STATE, {'schema': 'side-pair-review-run/v1', 'claims': {}})
        if state.get('schema') != 'side-pair-review-run/v1':
            raise ValueError('unknown claim state schema')
        yield state
        write_json(STATE, state)
        fcntl.flock(lock, fcntl.LOCK_UN)


def queue_rows():
    queue = read_json(QUEUE)
    if not queue or queue.get('schema') != 'side-ai-variant-review-queue/v1':
        raise ValueError('create the review queue before claiming')
    return [row for row in queue['rows'] if row['review_status'] in ELIGIBLE]


def gallery_rows():
    source = (WORK / 'gallery-data.js').read_text()
    prefix = 'window.SIDE_COMBINATIONS = '
    if not source.startswith(prefix):
        raise ValueError('gallery data has an unexpected format')
    return json.loads(source[len(prefix):].rstrip(' ;\n'))['rows']


def merge_missing():
    queue = read_json(QUEUE)
    if not queue or queue.get('schema') != 'side-ai-variant-review-queue/v1':
        raise ValueError('create the review queue before merging missing pairs')
    known = {row['id'] for row in queue['rows']}
    existing = decisions()
    added = 0
    for row in gallery_rows():
        if row['id'] in known:
            continue
        decision = existing.get(row['id'], {})
        status = decision.get('status', 'pending_unavailable')
        if status == 'accepted':
            status = 'stale_decision'
        queue['rows'].append({
            'id': row['id'], 'concept': row['concept'],
            'main': row['main']['key'], 'sub': row['sub']['key'],
            'reasons': [row.get('variant_unavailable') or row['status']],
            'priority': -1, 'options': [], 'review_status': status,
            'candidate_unavailable': True,
        })
        added += 1
    queue['counts']['gallery_pairs'] = len(known) + added
    queue['counts']['unavailable_pairs'] = added
    queue['counts']['pending_human'] = sum(
        row['review_status'] == 'pending_human' for row in queue['rows'])
    write_json(QUEUE, queue)
    print(json.dumps({'reviewable': len(known), 'unavailable': added,
                      'total': len(queue['rows'])}))


def sheet(pair_id, out):
    report = read_json(DEFAULT_INPUT / 'report.json')
    if any(row['id'] == pair_id for row in report['rows']):
        result = preview_one(pair_id, DEFAULT_INPUT, DEFAULT_DECISIONS,
                             DEFAULT_LAYOUTS, out, DEFAULT_LAYOUT_OUTPUT)
        print(json.dumps({**result, 'candidate_unavailable': False}))
        return
    import cairosvg
    from PIL import Image, ImageDraw

    row = next((row for row in gallery_rows() if row['id'] == pair_id), None)
    if row is None:
        raise ValueError('pair is absent from the gallery')
    panels = [('main source', row['main'].get('source')),
              ('main fill', row['main'].get('fill')),
              ('sub source', row['sub'].get('source')),
              ('sub fill', row['sub'].get('fill'))]
    canvas = Image.new('RGB', (720, 560), 'white')
    draw = ImageDraw.Draw(canvas)
    draw.text((12, 12), f'{row["concept"]} · {pair_id}', fill='black')
    draw.text((12, 34), 'No Normal combined candidate is available for visual approval.', fill='#a00')
    reason = str(row.get('variant_unavailable') or row['status'])
    draw.text((12, 55), reason[:105], fill='#a00')
    for index, (label, url) in enumerate(panels):
        x = 12 + (index % 2) * 350
        y = 90 + (index // 2) * 230
        draw.text((x, y), label, fill='black')
        path = ((DATA / url.lstrip('/')) if url.startswith('/')
                else (ROOT / url)).resolve() if url else None
        if path and path.is_file():
            try:
                data = cairosvg.svg2png(url=str(path), output_width=192, output_height=192)
                import io
                artwork = Image.open(io.BytesIO(data)).convert('RGBA')
                canvas.paste(artwork, (x + 40, y + 24), artwork)
            except Exception as error:
                draw.text((x, y + 32), f'Could not render: {str(error)[:38]}', fill='#a00')
        else:
            draw.text((x, y + 32), 'Source unavailable', fill='#a00')
    out.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out)
    print(json.dumps({'id': pair_id, 'candidate_unavailable': True,
                      'reason': reason, 'output': str(out)}))


def decisions():
    value = read_json(DEFAULT_DECISIONS, {'decisions': {}})
    return value.get('decisions', {})


def proposals():
    return read_json(DEFAULT_SPECS, {'pairs': {}}).get('pairs', {})


def claim_dir(pair_id, token):
    return RUN_DIR / 'claims' / f'{pair_id}-{token}'


def validate_layout_paths(pair_id, candidate):
    variant = candidate.get('variant', '')
    if not variant.startswith('layout-'):
        raise ValueError('staged layout candidate has an invalid variant')
    for field, folder, suffix in (
            ('svg', 'svg', '.svg'),
            ('stress_svg', 'stress', '--8px.svg')):
        relative = candidate.get(field)
        if relative is None and field == 'stress_svg':
            continue
        path = Path(relative or '')
        expected = f'{pair_id}--{variant}{suffix}'
        if path.is_absolute() or path.parts != (folder, expected):
            raise ValueError(f'staged {field} path is outside this pair')


def prepare_stage(pair_id, record, decision_map, proposal_map):
    directory = claim_dir(pair_id, record['token'])
    directory.mkdir(parents=True, exist_ok=True)
    decision_file = directory / 'decisions.json'
    specs_file = directory / 'layout-proposals.json'
    if not decision_file.exists():
        entry = decision_map.get(pair_id)
        write_json(decision_file, {'schema': 'side-ai-variant-decisions/v1',
                                  'decisions': {pair_id: entry} if entry else {}})
    if not specs_file.exists():
        write_json(specs_file, {'schema': 'side-ai-layout-proposals/v1',
                                'pairs': {pair_id: proposal_map.get(pair_id, [])}})
    return directory


def next_row(rows, state):
    current_decisions = decisions()
    report_items = None
    for row in rows:
        claim = state['claims'].get(row['id'])
        if claim and claim['status'] == 'active':
            continue
        if claim and claim['status'] == 'done':
            # The queue is a snapshot. A pair that was stale when the run
            # started may now have a valid committed review. Recheck that
            # decision against current candidate files before reclaiming it.
            decision = current_decisions.get(row['id'])
            if claim.get('decision_sha256') == digest(decision):
                # A historical repair label is unfinished work. It may be
                # claimed again under the accepted-only review protocol.
                if decision and decision.get('status') == 'needs_repair':
                    return row
                if decision and decision.get('status') == 'pending_human':
                    continue
                if decision and decision.get('status') == 'accepted' and \
                        decision.get('review_protocol') == REVIEW_PROTOCOL:
                    if report_items is None:
                        report_items = {item['id']: item for item in
                                        read_json(DEFAULT_INPUT / 'report.json')['rows']}
                    item = report_items.get(row['id'])
                    if item is not None:
                        sources = candidate_sources(item, DEFAULT_INPUT)
                        approved = dict(decision.get('acceptable_candidate_sha256', {}))
                        if decision.get('variant'):
                            approved[decision['variant']] = decision.get('candidate_sha256')
                        if approved and all(
                                variant in sources and sources[variant][1].is_file()
                                and sha(sources[variant][1]) == expected
                                and stress_current(variant, sources[variant][0],
                                                   decision, DEFAULT_LAYOUT_OUTPUT)
                                for variant, expected in approved.items()):
                            continue
        return row
    return None


def claim(owner, peek=False):
    rows = queue_rows()
    with locked_state() as state:
        active = next(((pair_id, claim) for pair_id, claim in state['claims'].items()
                       if claim['status'] == 'active'), None)
        if active:
            pair_id, record = active
            if not peek:
                prepare_stage(pair_id, record, decisions(), proposals())
            print(f'{pair_id} {record["token"]}')
            return
        row = next_row(rows, state)
        if row is None:
            return
        pair_id = row['id']
        token = uuid.uuid4().hex[:12]
        if not peek:
            current_decisions = decisions()
            current_proposals = proposals()
            state['claims'][pair_id] = {
                'status': 'active', 'owner': owner, 'token': token,
                'claimed_at': now(), 'queue_status': row['review_status'],
                'decision_sha_before': digest(current_decisions.get(pair_id)),
                'proposal_sha_before': digest(current_proposals.get(pair_id, [])),
            }
            prepare_stage(pair_id, state['claims'][pair_id], current_decisions,
                          current_proposals)
        print(f'{pair_id} {token}')


def claim_batch(owner, limit, *, randomize=False, seed=None, exclude_ids=(),
                active_only=False):
    if limit < 1:
        raise ValueError('claim batch limit must be positive')
    excluded = set(exclude_ids)
    rows = [row for row in queue_rows() if row['id'] not in excluded]
    if randomize:
        rows = [row for row in rows if not row.get('candidate_unavailable')]
        (random.Random(seed) if seed is not None else random.SystemRandom()).shuffle(rows)
    with locked_state() as state:
        current_decisions = decisions()
        current_proposals = proposals()
        active = ([] if randomize else sorted(
            ((pair_id, record) for pair_id, record in state['claims'].items()
             if record['status'] == 'active' and pair_id not in excluded),
            key=lambda item: item[1]['claimed_at']))
        selected = active[:limit]
        for pair_id, record in selected:
            prepare_stage(pair_id, record, current_decisions, current_proposals)
        while not active_only and len(selected) < limit:
            row = next_row(rows, state)
            if row is None:
                break
            pair_id = row['id']
            token = uuid.uuid4().hex[:12]
            record = {'status': 'active', 'owner': owner, 'token': token,
                      'claimed_at': now(), 'queue_status': row['review_status'],
                      'decision_sha_before': digest(current_decisions.get(pair_id)),
                      'proposal_sha_before': digest(current_proposals.get(pair_id, []))}
            state['claims'][pair_id] = record
            prepare_stage(pair_id, record, current_decisions, current_proposals)
            selected.append((pair_id, record))
        for pair_id, record in selected:
            print(f'{pair_id} {record["token"]}')


def reopen(pair_id, owner, reason):
    if not reason or not reason.strip():
        raise ValueError('reopening a pair needs a concrete visual defect')
    with locked_state() as state:
        prior = state['claims'].get(pair_id)
        if prior is None or prior['status'] != 'done':
            raise ValueError('only a completed pair can be reopened')
        current_decisions = decisions()
        current_proposals = proposals()
        record = {
            'status': 'active', 'owner': owner, 'token': uuid.uuid4().hex[:12],
            'claimed_at': now(), 'queue_status': 'visual_repair',
            'reopen_reason': reason.strip(),
            'supersedes_token': prior['token'],
            'decision_sha_before': digest(current_decisions.get(pair_id)),
            'proposal_sha_before': digest(current_proposals.get(pair_id, [])),
        }
        state['claims'][pair_id] = record
        prepare_stage(pair_id, record, current_decisions, current_proposals)
        print(f'{pair_id} {record["token"]}')


def evidence_files(decision):
    evidence = decision.get('evidence', [])
    if isinstance(evidence, str):
        evidence = [evidence]
    if not isinstance(evidence, list) or not evidence:
        raise ValueError('decision needs viewed image evidence paths')
    paths = []
    for value in evidence:
        if not isinstance(value, str) or not value:
            raise ValueError('evidence paths must be nonempty strings')
        path = Path(value)
        path = path if path.is_absolute() else DATA / path
        if not path.is_file():
            raise ValueError(f'evidence file is missing: {path}')
        paths.append(path)
    return paths


def require_ai_sub_size(variant, candidate, pair_id=None):
    # This exact 21px magnifier was previously published after a user correction.
    # Keep the exception pinned to the reviewed SVG, not future small layouts.
    if (pair_id == 'b193343f-83cb-42e1-b4d3-72d2792ce8ri'
            and variant == 'layout-phone-outline-48-search-21-x0-y1-clean'
            and candidate.get('candidate_sha256') ==
            '775475776f2ff6fc19ac51dd3aadcfc233c3ce5fb6f1f7fda499d32f9282e334'):
        return
    if variant.startswith('layout-') and candidate.get('sub', {}).get('size', 32) < MIN_AI_SUB_SIZE:
        bounds = candidate.get('sub_bounds')
        painted_size = (max(bounds[2] - bounds[0], bounds[3] - bounds[1])
                        if isinstance(bounds, list) and len(bounds) == 4 else 0)
        if painted_size < MIN_AI_SUB_SIZE:
            raise ValueError(f'{variant}: painted AI sub size must be at least {MIN_AI_SUB_SIZE}px')


def verify(pair_id):
    state = read_json(STATE, {'claims': {}})
    claim_record = state.get('claims', {}).get(pair_id)
    if not claim_record or claim_record['status'] != 'active':
        raise ValueError('pair is not the active claim')
    decision = decisions().get(pair_id)
    if not decision or decision.get('status') not in ('accepted', 'pending_human'):
        raise ValueError('review must save an accepted or pending_human decision')
    after = digest(decision)
    if after == claim_record.get('decision_sha_before'):
        raise ValueError('decision was not refreshed during this claim')
    if len(decision.get('reason', '').strip()) < 25:
        raise ValueError('decision needs a concrete visual reason')
    evidence_files(decision)
    if decision.get('review_protocol') != REVIEW_PROTOCOL:
        raise ValueError(f'decision needs {REVIEW_PROTOCOL} visual review')
    if not decision.get('reviewer'):
        raise ValueError('decision needs a reviewer')
    if decision['status'] == 'pending_human':
        if not decision.get('reviewed_at'):
            raise ValueError('pending_human decision needs reviewed_at')
        if decision.get('variant') or decision.get('candidate_sha256'):
            raise ValueError('pending_human cannot select an unapproved candidate')
        return after, decision['status']
    report = read_json(DEFAULT_INPUT / 'report.json')
    item = next((row for row in report['rows'] if row['id'] == pair_id), None)
    if item is None:
        raise ValueError('pair is missing from the current candidate report')
    sources = candidate_sources(item, DEFAULT_INPUT, DEFAULT_LAYOUT_OUTPUT)
    approved = dict(decision.get('acceptable_candidate_sha256', {}))
    primary = decision.get('variant')
    if not primary or not decision.get('candidate_sha256'):
        raise ValueError('accepted decision needs its first variant and SVG hash')
    approved[primary] = decision['candidate_sha256']
    for variant, expected in approved.items():
        if variant not in sources:
            raise ValueError(f'candidate is unavailable: {variant}')
        candidate, path = sources[variant]
        require_ai_sub_size(variant, candidate, pair_id)
        if not candidate_has_genuine_fill(pair_id, variant, candidate):
            raise ValueError(f'candidate has no genuine fill: {variant}')
        if not path.is_file() or sha(path) != expected:
            raise ValueError(f'candidate SVG hash changed: {variant}')
        if not stress_current(variant, candidate, decision, DEFAULT_LAYOUT_OUTPUT):
            raise ValueError(f'8px stress SVG is unpinned or changed: {variant}')
    return after, decision['status']


def staged_review(pair_id):
    state = read_json(STATE, {'claims': {}})
    record = state.get('claims', {}).get(pair_id)
    if not record or record['status'] != 'active':
        raise ValueError('pair is not an active claim')
    directory = claim_dir(pair_id, record['token'])
    staged_decisions = read_json(directory / 'decisions.json', {})
    staged_specs = read_json(directory / 'layout-proposals.json', {})
    if staged_decisions.get('schema') != 'side-ai-variant-decisions/v1' or \
            set(staged_decisions.get('decisions', {})) != {pair_id}:
        raise ValueError('staged decisions must contain exactly this pair')
    if staged_specs.get('schema') != 'side-ai-layout-proposals/v1' or \
            set(staged_specs.get('pairs', {})) != {pair_id}:
        raise ValueError('staged layout proposals must contain exactly this pair')
    decision = staged_decisions['decisions'][pair_id]
    pair_specs = staged_specs['pairs'][pair_id]
    if not isinstance(pair_specs, list):
        raise ValueError('staged pair proposals must be a list')
    after = digest(decision)
    if after == record.get('decision_sha_before'):
        raise ValueError('staged decision was not refreshed during this claim')
    if decision.get('status') not in ('accepted', 'pending_human'):
        raise ValueError('review must save an accepted or pending_human decision')
    if len(decision.get('reason', '').strip()) < 25:
        raise ValueError('decision needs a concrete visual reason')
    evidence_files(decision)
    if decision.get('status') == 'pending_human':
        if decision.get('review_protocol') != REVIEW_PROTOCOL:
            raise ValueError(f'pending_human decision needs {REVIEW_PROTOCOL} visual review')
        if not decision.get('reviewer') or not decision.get('reviewed_at'):
            raise ValueError('pending_human decision needs reviewer and reviewed_at')
        if decision.get('variant') or decision.get('candidate_sha256'):
            raise ValueError('pending_human cannot select an unapproved candidate')
        return after, decision, pair_specs, None
    layout_dir = directory / 'layout'
    layout_report = read_json(layout_dir / 'report.json', {'pairs': {}})
    layout_row = layout_report.get('pairs', {}).get(pair_id)
    pair_specs_hash = digest(pair_specs)
    proposals_changed = pair_specs_hash != record.get('proposal_sha_before')
    if not pair_specs:
        layout_row = None
    if pair_specs and (proposals_changed or layout_row):
        if not layout_row or layout_row.get('pair_specs_sha256') != pair_specs_hash:
            raise ValueError('staged layout render does not match staged proposals')
        if layout_row.get('layout_sha256') != sha(DEFAULT_LAYOUTS):
            raise ValueError('staged layout render uses an old production layout')
        layout_item = next((item for item in read_json(DEFAULT_LAYOUTS)['items']
                            if item['reference_id'] == pair_id), None)
        if layout_item is None:
            raise ValueError('pair is missing from production layouts')
        parts = {part['role']: part for part in layout_item['parts']}
        for field, path in (
                ('main_source_sha256', source_path(parts['main'], 'main')),
                ('sub_source_sha256', source_path(parts['sub'], 'sub')),
                ('main_fill_sha256', fill_path(parts['main'], 'main')),
                ('sub_fill_sha256', fill_path(parts['sub'], 'sub'))):
            if path is None or not path.is_file() or layout_row.get(field) != sha(path):
                raise ValueError(f'staged layout source changed: {field}')
        for candidate in layout_row.get('candidates', []):
            validate_layout_paths(pair_id, candidate)
            path = layout_dir / candidate['svg']
            if not path.is_file() or sha(path) != candidate['candidate_sha256']:
                raise ValueError('staged layout SVG is missing or changed')
            if candidate.get('stress_svg'):
                stress = layout_dir / candidate['stress_svg']
                if not stress.is_file() or sha(stress) != candidate['stress_sha256']:
                    raise ValueError('staged 8px SVG is missing or changed')
    if decision.get('review_protocol') != REVIEW_PROTOCOL:
        raise ValueError(f'accepted decision needs {REVIEW_PROTOCOL} visual review')
    if not decision.get('reviewer'):
        raise ValueError('accepted decision needs a reviewer')
    report = read_json(DEFAULT_INPUT / 'report.json')
    item = next((row for row in report['rows'] if row['id'] == pair_id), None)
    if item is None:
        raise ValueError('pair has no Normal combined candidate to accept')
    sources = candidate_sources(item, DEFAULT_INPUT, layout_dir)
    approved = dict(decision.get('acceptable_candidate_sha256', {}))
    primary = decision.get('variant')
    if not primary or not decision.get('candidate_sha256'):
        raise ValueError('accepted decision needs its first variant and SVG hash')
    approved[primary] = decision['candidate_sha256']
    for variant, expected in approved.items():
        if variant not in sources:
            raise ValueError(f'staged candidate is unavailable: {variant}')
        candidate, path = sources[variant]
        require_ai_sub_size(variant, candidate, pair_id)
        if not candidate_has_genuine_fill(pair_id, variant, candidate):
            raise ValueError(f'staged candidate has no genuine fill: {variant}')
        if not path.is_file() or sha(path) != expected:
            raise ValueError(f'staged candidate SVG hash changed: {variant}')
        if not stress_current(variant, candidate, decision, layout_dir):
            raise ValueError(f'staged 8px SVG is unpinned or changed: {variant}')
    return after, decision, pair_specs, layout_row


def commit_stage(pair_id):
    after, decision, pair_specs, layout_row = staged_review(pair_id)
    with locked_state() as state:
        record = state['claims'].get(pair_id)
        if not record or record['status'] != 'active':
            raise ValueError('claim changed before commit')
        all_decisions = read_json(DEFAULT_DECISIONS)
        all_specs = read_json(DEFAULT_SPECS)
        # Claims created by the earlier one-pair runner did not pin proposal
        # state. Their untouched shared proposal is the only available base.
        proposal_before = record.get('proposal_sha_before')
        if proposal_before is None:
            proposal_before = digest(all_specs['pairs'].get(pair_id, []))
        if digest(all_decisions['decisions'].get(pair_id)) not in \
                (record.get('decision_sha_before'), after):
            raise ValueError('shared decision changed while this pair was reviewed')
        if decision['status'] == 'pending_human':
            # The reviewer may have tested layouts in the stage, but none is
            # approved for publication. Keep all shared artwork and specs.
            all_decisions['decisions'][pair_id] = decision
            write_json(DEFAULT_DECISIONS, all_decisions)
            record.update(status='done', completed_at=now(), decision_sha256=after,
                          decision_status='pending_human')
            print(f'{pair_id} pending_human')
            return
        spec_after = digest(pair_specs)
        if digest(all_specs['pairs'].get(pair_id, [])) not in \
                (proposal_before, spec_after):
            raise ValueError('shared layout proposal changed while this pair was reviewed')
        directory = claim_dir(pair_id, record['token'])
        if layout_row:
            layout_dir = directory / 'layout'
            for candidate in layout_row['candidates']:
                for key in ('svg', 'stress_svg'):
                    relative = candidate.get(key)
                    if relative:
                        destination = DEFAULT_LAYOUT_OUTPUT / relative
                        destination.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(layout_dir / relative, destination)
            global_report = read_json(DEFAULT_LAYOUT_OUTPUT / 'report.json',
                                      {'schema': 'side-ai-layout-renderings/v1',
                                       'pairs': {}})
            global_report['pairs'][pair_id] = layout_row
            write_json(DEFAULT_LAYOUT_OUTPUT / 'report.json', global_report)
        elif not pair_specs and spec_after != proposal_before:
            global_report = read_json(DEFAULT_LAYOUT_OUTPUT / 'report.json',
                                      {'schema': 'side-ai-layout-renderings/v1',
                                       'pairs': {}})
            global_report['pairs'].pop(pair_id, None)
            write_json(DEFAULT_LAYOUT_OUTPUT / 'report.json', global_report)
        if layout_row or (not pair_specs and spec_after != proposal_before):
            keep = {DEFAULT_LAYOUT_OUTPUT / candidate['svg']
                    for candidate in layout_row.get('candidates', [])} if layout_row else set()
            keep_stress = {DEFAULT_LAYOUT_OUTPUT / candidate['stress_svg']
                           for candidate in layout_row.get('candidates', [])
                           if candidate.get('stress_svg')} if layout_row else set()
            for path in (DEFAULT_LAYOUT_OUTPUT / 'svg').glob(f'{pair_id}--layout-*.svg'):
                if path not in keep:
                    path.unlink()
            for path in (DEFAULT_LAYOUT_OUTPUT / 'stress').glob(f'{pair_id}--layout-*--8px.svg'):
                if path not in keep_stress:
                    path.unlink()
        if spec_after != proposal_before:
            if pair_specs:
                all_specs['pairs'][pair_id] = pair_specs
            else:
                all_specs['pairs'].pop(pair_id, None)
        all_decisions['decisions'][pair_id] = decision
        if spec_after != proposal_before:
            write_json(DEFAULT_SPECS, all_specs)
        write_json(DEFAULT_DECISIONS, all_decisions)
        record.update(status='done', completed_at=now(), decision_sha256=after,
                      decision_status=decision['status'])
    print(f'{pair_id} {decision["status"]}')


def complete(pair_id):
    after, status = verify(pair_id)
    with locked_state() as state:
        record = state['claims'][pair_id]
        if record['status'] != 'active':
            raise ValueError('claim changed before completion')
        record.update(status='done', completed_at=now(), decision_sha256=after,
                      decision_status=status)
    print(f'{pair_id} {status}')


def summary():
    rows = queue_rows()
    state = read_json(STATE, {'claims': {}})
    claims = state.get('claims', {})
    current_decisions = decisions()
    completed = sum(claim['status'] == 'done' for claim in claims.values())
    done_in_queue = sum(
        row['review_status'] != 'stale_decision'
        and claims.get(row['id'], {}).get('status') == 'done'
        and claims[row['id']].get('decision_sha256') == digest(current_decisions.get(row['id']))
        for row in rows)
    active = [pair_id for pair_id, claim in claims.items() if claim['status'] == 'active']
    print(json.dumps({'completed_claims': completed,
                      'remaining_review': len(rows)-done_in_queue,
                      'pending_human': sum(d.get('status') == 'pending_human'
                                           for d in current_decisions.values()),
                      'active': active}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['claim', 'claim-batch', 'peek', 'reopen',
                                            'verify', 'verify-stage', 'complete',
                                            'commit-stage', 'status',
                                            'merge-missing', 'sheet'])
    parser.add_argument('--owner', default='local-review')
    parser.add_argument('--limit', type=int, default=1)
    parser.add_argument('--random', action='store_true', help='Sample new eligible claims and skip active claims')
    parser.add_argument('--seed', type=int, help='Repeatable random order for --random')
    parser.add_argument('--exclude-file', type=Path,
                        help='Skip these pair IDs during this claim-batch pass')
    parser.add_argument('--active-only', action='store_true',
                        help='Claim only existing active pairs')
    parser.add_argument('--id')
    parser.add_argument('--reason')
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    try:
        if args.command in ('claim', 'peek'):
            claim(args.owner, peek=args.command == 'peek')
        elif args.command == 'reopen':
            reopen(args.id, args.owner, args.reason)
        elif args.command == 'claim-batch':
            excluded = args.exclude_file.read_text().splitlines() if args.exclude_file else ()
            claim_batch(args.owner, args.limit, randomize=args.random,
                        seed=args.seed, exclude_ids=excluded,
                        active_only=args.active_only)
        elif args.command == 'merge-missing':
            merge_missing()
        elif args.command == 'status':
            summary()
        elif args.command == 'sheet':
            if not args.id or not args.out:
                parser.error('sheet requires --id and --out')
            sheet(args.id, args.out)
        elif not args.id:
            parser.error(f'{args.command} requires --id')
        elif args.command == 'verify':
            after, status = verify(args.id)
            print(f'{args.id} {status} {after}')
        elif args.command == 'verify-stage':
            after, decision, _specs, _layout = staged_review(args.id)
            print(f'{args.id} {decision["status"]} {after}')
        elif args.command == 'commit-stage':
            commit_stage(args.id)
        else:
            complete(args.id)
    except (OSError, ValueError, KeyError) as error:
        print(f'review claim error: {error}', file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == '__main__':
    main()
