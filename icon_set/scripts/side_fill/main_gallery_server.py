"""Serve local galleries and save main-variant rejections or side-pair selections."""

from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock, Timer

from .adaptive_overlap import MAIN_VARIANT_POLICY, ROOT
from .ai_variant_review import (DEFAULT_LAYOUT_OUTPUT, apply as apply_side_decisions,
                                REVIEW_PROTOCOL, candidate_has_genuine_fill,
                                candidate_sources)
from .build_gallery import build as build_pair_gallery, layout_entry as layout_gallery_entry
from .find_multi_region_mains import DEFAULT_LAYOUTS, DEFAULT_OUT, inventory
from .pair_layout_review import DEFAULT_SPECS as LAYOUT_SPECS, render_one as render_layout_one
from .pair_layout_review import repo_layout_svg, checked_source, DEFAULT_LAYOUTS


WORKSPACE = WORK
REVIEW_LOCK = Lock()
NAME_PATTERN = re.compile(r"[a-z0-9][a-z0-9-]*\Z")
VARIANT_PATTERN = re.compile(r"(?:region-[0-9]+|group-[a-z0-9-]+)\Z")
SIDE_REPORT = (WORK / 'recombined-all/report.json' if (WORK / 'recombined-all/report.json').exists()
               else WORK / 'adaptive-8px-all/report.json')
SIDE_DECISIONS = DATA / 'data/ai-variant-decisions.json'
SIDE_HISTORY = DATA / 'data/side-variant-selection-history.jsonl'
SIDE_SELECTED = WORK / 'selected-combinations'


def layout_editor_parts(pair_id):
    """Return original path artwork and the saved per-element boxes for the editor."""
    if not isinstance(pair_id, str) or not NAME_PATTERN.fullmatch(pair_id):
        raise ValueError('Invalid pair ID')
    item = next((row for row in json.loads(DEFAULT_LAYOUTS.read_text())['items']
                 if row['reference_id'] == pair_id), None)
    if item is None:
        raise ValueError('Pair is not in the layout collection')
    cls = repo_layout_svg()
    result = {}
    for role in ('main', 'sub'):
        part = next(part for part in item['parts'] if part['role'] == role)
        source = checked_source(part, role)
        raw = cls.component({'role': role, 'document': source.read_text(),
                             'scale': 1, 'tx': 0, 'ty': 0}, 64)
        boxes = json.loads(json.dumps(part['layout']))
        # Some saved placements were measured on tilted artwork and are fractional; the
        # layout renderer takes integer grid units, so the editor starts from the nearest ones.
        for box in boxes:
            for axis in ('x', 'y', 'w', 'h'):
                box[axis] = int(round(box[axis]))
        if len(boxes) == 1 and 'paths' not in boxes[0]:
            boxes[0]['paths'] = [i for i, bounds in enumerate(raw['sources']) if bounds]
        result[role] = {'markup': raw['markup'], 'names': raw['names'],
                        'sources': raw['sources'], 'units': boxes}
    return result


def preview_side_layout(pair_id, proposal):
    """Compose one draft with the same renderer used by saved layout candidates."""
    if not isinstance(pair_id, str) or not isinstance(proposal, dict):
        raise ValueError('Pair ID and layout proposal are required')
    if not NAME_PATTERN.fullmatch(proposal.get('id', '')):
        raise ValueError('Use a short lowercase layout name')
    with tempfile.TemporaryDirectory(prefix='side-layout-preview-') as directory:
        tmp = Path(directory)
        specs = tmp / 'specs.json'
        specs.write_text(json.dumps({'schema': 'side-ai-layout-proposals/v1',
                                     'pairs': {pair_id: [proposal]}}))
        result = render_layout_one(pair_id, specs_path=specs, out=tmp / 'render',
                                   allow_keyshape_mismatch=True)
        candidate = result['candidates'][0]
        return {'candidate': candidate,
                'svg': (tmp / 'render' / candidate['svg']).read_text(),
                'stress_svg': ((tmp / 'render' / candidate['stress_svg']).read_text()
                               if candidate['stress_svg'] else None)}


PLACEMENT_OVERRIDES = DATA / 'data/pair-placement-overrides.json'


def placement_only(pair_id, proposal):
    """True when a layout only moves or resizes a normal variant's parts (user rule, 2026-10-28):
    then it is applied to the pair's own placement instead of becoming a separate layout record."""
    base = proposal.get('base_variant', '')
    return (isinstance(base, str) and base and not base.startswith('layout-')
            and proposal.get('sub_variant', 'fill') == 'fill'
            and proposal.get('overlap_mode', 'clear') == 'clear'
            and not proposal.get('omit_main_elements')
            and proposal.get('position', pair_id[-2:]) == pair_id[-2:])


def apply_placement(pair_id, proposal):
    """Move the pair's saved placement to the layout's boxes and recombine the pair.

    Records the original boxes in data/pair-placement-overrides.json (needed again after a production
    re-import), re-renders the pair's other layouts against the new placement, and refreshes the
    whole-file layout hash in the layout report (every row's own placement is unchanged).
    Returns the fresh recombined candidate for the base variant. Call with REVIEW_LOCK held."""
    from .adaptive_overlap import main as recombine
    boxes = preview_side_layout(pair_id, proposal)['candidate']['layout_boxes']
    layouts = json.loads(DEFAULT_LAYOUTS.read_text())
    item = next(row for row in layouts['items'] if row['reference_id'] == pair_id)
    original = {part['role']: part['layout'] for part in item['parts']}
    for part in item['parts']:
        part['layout'] = boxes[part['role']]
    overrides = (json.loads(PLACEMENT_OVERRIDES.read_text()) if PLACEMENT_OVERRIDES.exists()
                 else {'schema': 'pair-placement-overrides/v1', 'pairs': {}})
    overrides['pairs'][pair_id] = {'at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
                                   'from_layout': 'layout editor: ' + proposal.get('id', ''), 'layout': boxes,
                                   'original': overrides['pairs'].get(pair_id, {}).get('original', original)}
    DEFAULT_LAYOUTS.write_text(json.dumps(layouts, indent=2) + '\n')
    PLACEMENT_OVERRIDES.write_text(json.dumps(overrides, indent=1) + '\n')
    with tempfile.TemporaryDirectory(prefix='placement-recombine-') as directory:
        tmp = Path(directory)
        recombine(['--out', str(tmp), '--summary-only', '--ids', pair_id])
        fresh = next(row for row in json.loads((tmp / 'report.json').read_text())['rows'] if row['id'] == pair_id)
        from .mark_duplicate_variants import mark_row
        mark_row(fresh, tmp)          # region/group variants drawing the same picture as current stay hidden
        report = json.loads(SIDE_REPORT.read_text())
        report['rows'] = [fresh if row['id'] == pair_id else row for row in report['rows']]
        for candidate in fresh['candidates']:
            (SIDE_REPORT.parent / candidate['svg']).write_bytes((tmp / candidate['svg']).read_bytes())
        temporary = SIDE_REPORT.with_name(SIDE_REPORT.name + '.tmp')
        temporary.write_text(json.dumps(report, indent=2) + '\n')
        os.replace(temporary, SIDE_REPORT)
    has_layouts = bool(json.loads(LAYOUT_SPECS.read_text())['pairs'].get(pair_id))
    if has_layouts:
        render_layout_one(pair_id)
    layout_report_path = DEFAULT_LAYOUT_OUTPUT / 'report.json'
    layout_report = json.loads(layout_report_path.read_text())
    if not has_layouts:
        layout_report['pairs'].pop(pair_id, None)      # its last layout record was folded in
    digest = hashlib.sha256(DEFAULT_LAYOUTS.read_bytes()).hexdigest()
    for row in layout_report['pairs'].values():
        row['layout_sha256'] = digest
    temporary = layout_report_path.with_name(layout_report_path.name + '.tmp')
    temporary.write_text(json.dumps(layout_report, indent=2) + '\n')
    os.replace(temporary, layout_report_path)
    return next(c for c in fresh['candidates'] if c['variant'] == proposal['base_variant'])


def save_placement(pair_id, proposal, replaces=None):
    """Editor save that only repositions a normal variant: apply it to the pair's placement and keep
    the pick as that variant. The pair's other picks are kept, in order, with their new renders."""
    base = proposal['base_variant']
    previous = json.loads(SIDE_DECISIONS.read_text())['decisions'].get(pair_id) or {}
    earlier = ([previous['variant']] if previous.get('variant') else []) + list(previous.get('acceptable_candidate_sha256', {}))
    keep = [v for v in dict.fromkeys(earlier) if v not in (base, replaces)] if previous.get('status') == 'accepted' else []
    with REVIEW_LOCK:
        # The layout record the editor was opened from is now the pair's own placement: it goes, so the
        # pair keeps no second copy of the same picture (user rule: no layout records for a placement).
        if isinstance(replaces, str) and replaces.startswith('layout-'):
            specs = json.loads(LAYOUT_SPECS.read_text())
            kept = [s for s in specs['pairs'].get(pair_id, []) if 'layout-' + s['id'] != replaces]
            if kept:
                specs['pairs'][pair_id] = kept
            else:
                specs['pairs'].pop(pair_id, None)
            LAYOUT_SPECS.write_text(json.dumps(specs, indent=2) + '\n')
        candidate = apply_placement(pair_id, proposal)
    # Select the kept picks last-first, then the base, so the base leads and the order stays.
    order = [base, *keep]
    selection = None
    for index, variant in enumerate(reversed(order)):
        try:
            selection = select_side_variant(pair_id, variant, refresh=False, keep_earlier=index > 0,
                                            reason=proposal.get('reason') if variant == base else None)
        except ValueError:
            if variant == base:
                raise
    REFRESH.schedule()
    from .build_gallery import url, VARIANT_OUTPUT
    tile = {'variant': base, 'kind': 'normal', 'combined': url(VARIANT_OUTPUT / candidate['svg']),
            'safe': candidate['safe'], 'status': candidate['semantic_status'], 'main_style': 'normal',
            'sub_style': 'normal', 'sha256': candidate['candidate_sha256'],
            'validation_overlap': candidate['added_fill_inside_validation_px2'],
            'render_gap': candidate.get('render_gap_px'), 'graph_status': candidate['graph_status'],
            'graph_issues': candidate['graph_issues'], 'ai_acceptable': True, 'ai_rejected': False}
    return {'id': pair_id, 'variant': base, 'tile': tile, 'dropped': [replaces] if replaces and replaces != base else [],
            'proposals': selection['proposals'], 'reason': selection['reason'], 'applied_to_placement': True}


def save_side_layout(pair_id, proposal, replaces=None):
    """Save a pair-local layout and make it the pair's first proposal at once.

    A layout that only moves or resizes a normal variant's parts is applied to the pair's own
    placement instead (save_placement): no layout record is created. Otherwise saving again under the
    same name overwrites that layout's render. The variant the editor was opened from (`replaces`) is
    dropped from the pair's proposals; any other proposals stay. The response carries the gallery tile
    so the page updates in place; the gallery file is rebuilt in the background.
    """
    if isinstance(proposal, dict) and isinstance(pair_id, str) and placement_only(pair_id, proposal):
        return save_placement(pair_id, proposal, replaces)
    with REVIEW_LOCK:
        preview_side_layout(pair_id, proposal)
        specs = json.loads(LAYOUT_SPECS.read_text())
        if specs.get('schema') != 'side-ai-layout-proposals/v1':
            raise ValueError('Unexpected layout proposal schema')
        current = specs['pairs'].get(pair_id, [])
        specs['pairs'][pair_id] = [item for item in current if item['id'] != proposal['id']] + [proposal]
        old = LAYOUT_SPECS.read_text()
        LAYOUT_SPECS.write_text(json.dumps(specs, indent=2) + '\n')
        try:
            rendered = render_layout_one(pair_id)
        except Exception:
            LAYOUT_SPECS.write_text(old)
            raise
    variant = 'layout-' + proposal['id']
    candidate = next(c for c in rendered['candidates'] if c['variant'] == variant)
    drop = [replaces] if isinstance(replaces, str) and replaces != variant else []
    selection = select_side_variant(pair_id, variant, refresh=False, drop_variants=drop,
                                    reason=proposal.get('reason'))
    REFRESH.schedule()
    stress = DEFAULT_LAYOUT_OUTPUT / candidate['stress_svg'] if candidate.get('stress_svg') else None
    tile = layout_gallery_entry(candidate, candidate.get('keyshape_validation', {}), stress)
    tile.update(ai_acceptable=True, ai_rejected=False)
    return {'id': pair_id, 'variant': variant, 'tile': tile, 'dropped': drop,
            'proposals': selection['proposals'], 'reason': selection['reason']}


def reject_main_variant(name, variant, *, policy_path=MAIN_VARIANT_POLICY,
                        inventory_path=DEFAULT_OUT / "inventory.json", rebuild=True):
    """Persist a user rejection of one visible generated main variant."""
    if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name):
        raise ValueError("Invalid main icon name")
    if not isinstance(variant, str) or not VARIANT_PATTERN.fullmatch(variant):
        raise ValueError("Invalid variant name")
    with REVIEW_LOCK:
        gallery = json.loads(inventory_path.read_text())
        row = next((row for row in gallery["rows"] if row["name"] == name), None)
        if row is None:
            raise ValueError("Main icon is not in this gallery")
        choices = row["regions"] + row["extra_variants"]
        choice = next((choice for choice in choices if choice["variant"] == variant), None)
        if choice is None or choice["status"] not in ("approved", "unreviewed"):
            raise ValueError("Variant is not a visible review candidate")
        policy = json.loads(policy_path.read_text())
        entry = policy["mains"].setdefault(name, {"approved": [], "rejected": [], "groups": {}})
        entry["approved"] = sorted(set(entry.get("approved", [])) - {variant})
        entry["rejected"] = sorted(set(entry.get("rejected", [])) | {variant})
        entry["gallery_rejections"] = sorted(set(entry.get("gallery_rejections", [])) | {variant})
        if entry.get("preferred_main_variant") == variant:
            entry.pop("preferred_main_variant")
        entry["last_gallery_rejection"] = variant
        temporary = policy_path.with_name(policy_path.name + ".tmp")
        temporary.write_text(json.dumps(policy, indent=2) + "\n")
        os.replace(temporary, policy_path)
        if not rebuild:
            return None
        counts = inventory(DEFAULT_LAYOUTS, DEFAULT_OUT)
        build_pair_gallery()
        return counts


def select_side_variant(pair_id, variant, *, report_path=None,
                        decisions_path=SIDE_DECISIONS, history_path=SIDE_HISTORY,
                        selected_dir=SIDE_SELECTED, layout_dir=DEFAULT_LAYOUT_OUTPUT, refresh=True,
                        keep_earlier=True, drop_variants=(), reason=None):
    """Pin the exact reviewed SVG and copy valid selections into local outputs.

    refresh=False saves the decision only; the caller applies and rebuilds the gallery once.
    keep_earlier=False replaces the earlier accepted variants instead of keeping them acceptable."""
    if not isinstance(pair_id, str) or not isinstance(variant, str):
        raise ValueError('Pair ID and variant are required')
    report_path = report_path or (WORK / 'recombined-all/report.json'
                                  if (WORK / 'recombined-all/report.json').exists()
                                  else WORK / 'adaptive-8px-all/report.json')
    with REVIEW_LOCK:
        report = json.loads(report_path.read_text())
        row = next((row for row in report['rows'] if row['id'] == pair_id), None)
        if row is None:
            raise ValueError('Pair is not in the recombined gallery')
        source_entry = candidate_sources(row, report_path.parent, layout_dir).get(variant)
        if source_entry is None:
            raise ValueError('Variant is not available for this pair')
        candidate, svg = source_entry
        if not candidate_has_genuine_fill(pair_id, variant, candidate):
            raise ValueError('A fill side combination needs at least one genuinely filled icon')
        if candidate.get('main_style', 'normal') != 'normal' or candidate.get('sub_style', 'normal') != 'normal':
            raise ValueError('This review accepts Normal main and sub variants only')
        if not svg.is_file():
            raise ValueError('Candidate SVG is missing')
        digest = hashlib.sha256(svg.read_bytes()).hexdigest()
        if candidate.get('candidate_sha256') and digest != candidate['candidate_sha256']:
            raise ValueError('Candidate SVG changed since the gallery was built')
        stress_digest = None
        if variant.startswith('layout-') and candidate.get('base_variant') != 'outline':
            stress_relative = candidate.get('stress_svg')
            if not stress_relative:
                raise ValueError('Filled layout candidate has no 8px stress rendering')
            stress_file = layout_dir / stress_relative
            if not stress_file.is_file():
                raise ValueError('8px stress rendering is missing')
            stress_digest = hashlib.sha256(stress_file.read_bytes()).hexdigest()
            if stress_digest != candidate.get('stress_sha256'):
                raise ValueError('8px stress rendering changed since review')
        decisions = json.loads(decisions_path.read_text())
        if decisions.get('schema') != 'side-ai-variant-decisions/v1':
            raise ValueError('Unexpected side decision schema')
        previous = decisions['decisions'].get(pair_id)
        acceptable = {}
        stress_acceptable = {}
        rejected = dict(previous.get('rejected_candidate_sha256', {})) if previous else {}
        if keep_earlier and previous and previous.get('status') == 'accepted':
            earlier = dict(previous.get('acceptable_candidate_sha256', {}))
            if previous.get('variant') and previous.get('candidate_sha256'):
                earlier[previous['variant']] = previous['candidate_sha256']
            for earlier_variant, earlier_digest in earlier.items():
                entry = candidate_sources(row, report_path.parent, layout_dir).get(earlier_variant)
                if (earlier_variant != variant and entry and entry[1].is_file()
                        and hashlib.sha256(entry[1].read_bytes()).hexdigest() == earlier_digest):
                    acceptable[earlier_variant] = earlier_digest
                    prior_stress = previous.get('stress_candidate_sha256', {}).get(earlier_variant)
                    if prior_stress:
                        stress_acceptable[earlier_variant] = prior_stress
        rejected.pop(variant, None)
        for dropped in drop_variants:
            acceptable.pop(dropped, None)
            stress_acceptable.pop(dropped, None)
        record = {'status': 'accepted', 'variant': variant, 'candidate_sha256': digest,
                  'reviewer': 'user via local gallery',
                  'review_protocol': REVIEW_PROTOCOL,
                  'reason': (reason or candidate.get('reason') or
                             'Added after visual review from the Normal side-combination gallery.'),
                  'acceptable_candidate_sha256': acceptable,
                  'stress_candidate_sha256': {**stress_acceptable,
                                              **({variant: stress_digest} if stress_digest else {})},
                  'rejected_candidate_sha256': rejected}
        history_path.parent.mkdir(parents=True, exist_ok=True)
        with history_path.open('a') as history:
            history.write(json.dumps({'at': datetime.now(timezone.utc).isoformat(), 'id': pair_id,
                                      'previous': previous, 'selected': record}) + '\n')
        decisions['decisions'][pair_id] = record
        temporary = decisions_path.with_name(decisions_path.name + '.tmp')
        temporary.write_text(json.dumps(decisions, indent=2) + '\n')
        os.replace(temporary, decisions_path)
        if not refresh:
            return {'id': pair_id, 'variant': variant, 'sha256': digest,
                    'proposals': [variant, *acceptable], 'reason': record['reason']}
        applied = apply_side_decisions(report_path.parent, decisions_path, selected_dir, layout_dir)
        build_pair_gallery()
        return {'id': pair_id, 'variant': variant, 'sha256': digest,
                'proposals': [variant, *acceptable],
                'reason': record['reason'],
                'applied': len(applied['applied']), 'stale_or_invalid': len(applied['errors'])}


def select_side_variants(choices, replace=False):
    """Save many reviewed selections, then apply them and rebuild the gallery once."""
    if not isinstance(choices, list) or not 1 <= len(choices) <= 200:
        raise ValueError('Send 1 to 200 choices')
    saved, errors = [], {}
    for choice in choices:
        pair_id = choice.get('id') if isinstance(choice, dict) else None
        try:
            saved.append(select_side_variant(pair_id, choice.get('variant'), refresh=False,
                                             keep_earlier=not replace))
        except (ValueError, KeyError) as error:
            errors[str(pair_id)] = str(error)
    REFRESH.schedule()
    return {'saved': saved, 'errors': errors, 'applied': len(saved), 'refresh': 'scheduled'}


class BackgroundRefresh:
    """Apply selections and rebuild the gallery once, shortly after the last save.

    Both steps take ~14s together; running them per click made Select/Deselect wait for them.
    Saves return at once and the page updates the card itself; a burst of clicks rebuilds once.
    """

    def __init__(self, delay=1.5):
        self.delay, self.timer, self.lock, self.building = delay, None, Lock(), Lock()
        self.state = {'pending': False, 'running': False, 'finished_at': None, 'error': None}

    def schedule(self):
        with self.lock:
            if self.timer:
                self.timer.cancel()
            self.state['pending'] = True
            self.timer = Timer(self.delay, self.run)
            self.timer.daemon = True
            self.timer.start()

    def run(self):
        with self.lock:
            self.timer = None
            self.state.update(pending=False, running=True)
        error = None
        try:
            # Not REVIEW_LOCK: saves replace the decision file atomically, so they never wait for this
            # ~14s rebuild; a save made meanwhile schedules the next one.
            with self.building:
                apply_side_decisions(SIDE_REPORT.parent, SIDE_DECISIONS, SIDE_SELECTED, DEFAULT_LAYOUT_OUTPUT)
                build_pair_gallery()
        except Exception as exc:  # report it; the next save schedules another attempt
            error = repr(exc)
        with self.lock:
            self.state.update(running=False, error=error,
                              finished_at=datetime.now(timezone.utc).isoformat())

    def status(self):
        with self.lock:
            return dict(self.state)


REFRESH = BackgroundRefresh()


MAIN_VARIANT_VERDICTS = WORK / 'main-variant-noise-review.json'


def save_main_variant_verdicts(verdicts):
    """Store the user's keep/noise verdicts for the reviewed main variants (no policy change)."""
    with REVIEW_LOCK:
        review = json.loads(MAIN_VARIANT_VERDICTS.read_text())
        rows = {(row['main'], row['variant']): row for row in review}
        if not isinstance(verdicts, list) or len(verdicts) != len(rows):
            raise ValueError('Send a verdict for every reviewed variant')
        for item in verdicts:
            row = rows.get((item.get('main'), item.get('variant'))) if isinstance(item, dict) else None
            if row is None or item.get('verdict') not in ('keep', 'noise'):
                raise ValueError('Unknown variant or verdict')
            if row['verdict'] != item['verdict']:
                row.update(verdict=item['verdict'], set_by='user')
        temporary = MAIN_VARIANT_VERDICTS.with_name(MAIN_VARIANT_VERDICTS.name + '.tmp')
        temporary.write_text(json.dumps(review, indent=1) + '\n')
        os.replace(temporary, MAIN_VARIANT_VERDICTS)
    return {'keep': sum(r['verdict'] == 'keep' for r in review),
            'noise': sum(r['verdict'] == 'noise' for r in review)}


def reject_side_candidate(pair_id, variant, undo=False):
    """Hide one candidate render on one pair (the grid page's Remove), or undo that.

    The exact render's hash goes into the decision's rejected_candidate_sha256; a pair without a
    decision gets a 'pending' record holding only the rejection, so it stays not reviewed. A selected
    proposal must be unselected first.
    """
    if not isinstance(pair_id, str) or not isinstance(variant, str):
        raise ValueError('Pair ID and variant are required')
    with REVIEW_LOCK:
        report = json.loads(SIDE_REPORT.read_text())
        row = next((row for row in report['rows'] if row['id'] == pair_id), None)
        if row is None:
            raise ValueError('Pair is not in the recombined gallery')
        entry = candidate_sources(row, SIDE_REPORT.parent, DEFAULT_LAYOUT_OUTPUT).get(variant)
        if entry is None or not entry[1].is_file():
            raise ValueError('Variant is not available for this pair')
        digest = hashlib.sha256(entry[1].read_bytes()).hexdigest()
        decisions = json.loads(SIDE_DECISIONS.read_text())
        previous = decisions['decisions'].get(pair_id)
        record = json.loads(json.dumps(previous)) if previous else {'status': 'pending'}
        if record.get('status') == 'accepted' and (record.get('variant') == variant
                                                   or variant in record.get('acceptable_candidate_sha256', {})):
            raise ValueError('Unselect this proposal before removing it')
        rejected = record.setdefault('rejected_candidate_sha256', {})
        if undo:
            rejected.pop(variant, None)
        else:
            rejected[variant] = digest
        if record == {'status': 'pending', 'rejected_candidate_sha256': {}}:
            decisions['decisions'].pop(pair_id, None)
        else:
            decisions['decisions'][pair_id] = record
        with SIDE_HISTORY.open('a') as history:
            history.write(json.dumps({'at': datetime.now(timezone.utc).isoformat(), 'id': pair_id,
                                      'previous': previous, 'selected': record,
                                      'note': ('undo remove ' if undo else 'remove ') + variant}) + '\n')
        temporary = SIDE_DECISIONS.with_name(SIDE_DECISIONS.name + '.tmp')
        temporary.write_text(json.dumps(decisions, indent=2) + '\n')
        os.replace(temporary, SIDE_DECISIONS)
    REFRESH.schedule()
    return {'id': pair_id, 'variant': variant, 'removed': not undo}


def deselect_side_variant(pair_id, variant, *, report_path=SIDE_REPORT,
                          decisions_path=SIDE_DECISIONS, history_path=SIDE_HISTORY,
                          selected_dir=SIDE_SELECTED, layout_dir=DEFAULT_LAYOUT_OUTPUT, refresh=True,
                          when_empty='pending_human'):
    """Remove one reviewed proposal, promoting another if one remains.

    when_empty='unreviewed' (the grid page's undo) removes the decision when no proposal is left,
    so the pair returns to not reviewed instead of pending the user's review."""
    if not isinstance(pair_id, str) or not isinstance(variant, str):
        raise ValueError('Pair ID and variant are required')
    with REVIEW_LOCK:
        report = json.loads(report_path.read_text())
        if not any(row['id'] == pair_id for row in report['rows']):
            raise ValueError('Pair is not in the recombined gallery')
        decisions = json.loads(decisions_path.read_text())
        if decisions.get('schema') != 'side-ai-variant-decisions/v1':
            raise ValueError('Unexpected side decision schema')
        previous = decisions['decisions'].get(pair_id)
        if not previous or previous.get('status') != 'accepted':
            raise ValueError('Pair has no selected proposals')
        proposals = dict(previous.get('acceptable_candidate_sha256', {}))
        primary = previous.get('variant')
        if primary and previous.get('candidate_sha256'):
            proposals[primary] = previous['candidate_sha256']
        if variant not in proposals:
            raise ValueError('Variant is not a selected proposal')
        proposals.pop(variant)
        next_primary = primary if primary in proposals else next(iter(proposals), None)
        record = {**previous,
                  'status': 'accepted' if next_primary else 'pending_human',
                  'variant': next_primary,
                  'candidate_sha256': proposals.pop(next_primary) if next_primary else None,
                  'reviewer': 'user via local gallery',
                  'reason': (previous.get('reason') if next_primary else
                             'User removed all proposals from the Normal side-combination gallery.'),
                  'acceptable_candidate_sha256': proposals,
                  'stress_candidate_sha256': {
                      key: digest for key, digest in previous.get('stress_candidate_sha256', {}).items()
                      if key == next_primary or key in proposals},
                  'review_protocol': REVIEW_PROTOCOL}
        history_path.parent.mkdir(parents=True, exist_ok=True)
        with history_path.open('a') as history:
            history.write(json.dumps({'at': datetime.now(timezone.utc).isoformat(), 'id': pair_id,
                                      'previous': previous, 'selected': record}) + '\n')
        if not next_primary and when_empty == 'unreviewed':
            # Back to not reviewed; candidates removed on the grid page stay removed.
            kept = previous.get('rejected_candidate_sha256') or {}
            record = None
            if kept:
                decisions['decisions'][pair_id] = {'status': 'pending', 'rejected_candidate_sha256': kept}
            else:
                decisions['decisions'].pop(pair_id)
        else:
            decisions['decisions'][pair_id] = record
        temporary = decisions_path.with_name(decisions_path.name + '.tmp')
        temporary.write_text(json.dumps(decisions, indent=2) + '\n')
        os.replace(temporary, decisions_path)
        if record is None:
            return {'id': pair_id, 'selected_variant': None, 'proposals': [],
                    'selection_status': 'pending', 'reason': None}
        result = {'id': pair_id, 'selected_variant': next_primary,
                  'proposals': ([next_primary] if next_primary else []) + list(proposals),
                  'selection_status': record['status'], 'reason': record['reason']}
        if not refresh:
            return result
        applied = apply_side_decisions(report_path.parent, decisions_path, selected_dir, layout_dir)
        build_pair_gallery()
        return {'id': pair_id, 'selected_variant': next_primary,
                'proposals': ([next_primary] if next_primary else []) + list(proposals),
                'selection_status': record['status'], 'reason': record['reason'],
                'applied': len(applied['applied']), 'stale_or_invalid': len(applied['errors'])}


class GalleryHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WORKSPACE), **kwargs)

    def send_header(self, keyword, value):
        if keyword.lower() == 'cache-control':
            self.cache_control_sent = True
        super().send_header(keyword, value)

    def end_headers(self):
        # Gallery data and SVGs are rewritten in place; always revalidate them.
        if not getattr(self, 'cache_control_sent', False):
            self.send_header("Cache-Control", "no-cache")
        self.cache_control_sent = False
        super().end_headers()

    def send_json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/side_combinations/api/health":
            self.send_json(HTTPStatus.OK, {"ok": True, "refresh": REFRESH.status()})
            return
        super().do_GET()

    def do_POST(self):
        if self.path not in ("/side_combinations/api/reject-main-variant",
                             "/side_combinations/api/select-side-variant",
                             "/side_combinations/api/select-side-variants",
                             "/side_combinations/api/main-variant-verdicts",
                             "/side_combinations/api/reject-side-candidate",
                             "/side_combinations/api/deselect-side-variant",
                             "/side_combinations/api/preview-layout",
                             "/side_combinations/api/layout-elements",
                             "/side_combinations/api/save-layout"):
            self.send_json(HTTPStatus.NOT_FOUND, {"error": "Unknown endpoint"})
            return
        origin = self.headers.get("Origin")
        allowed_origins = {f"http://127.0.0.1:{self.server.server_port}",
                           f"http://localhost:{self.server.server_port}"}
        if origin and origin not in allowed_origins:
            self.send_json(HTTPStatus.FORBIDDEN, {"error": "Local gallery only"})
            return
        if self.headers.get("Content-Type", "").split(";", 1)[0] != "application/json":
            self.send_json(HTTPStatus.UNSUPPORTED_MEDIA_TYPE, {"error": "Expected JSON"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 1 <= length <= (65536 if self.path.endswith(('/select-side-variants', '/main-variant-verdicts')) else 4096):
                raise ValueError("Invalid request size")
            request = json.loads(self.rfile.read(length))
            if not isinstance(request, dict):
                raise ValueError("Expected an object")
            if self.path.endswith('/reject-main-variant'):
                result = reject_main_variant(request.get("name"), request.get("variant"))
            elif self.path.endswith('/preview-layout'):
                result = preview_side_layout(request.get('id'), request.get('proposal'))
            elif self.path.endswith('/layout-elements'):
                result = layout_editor_parts(request.get('id'))
            elif self.path.endswith('/save-layout'):
                result = save_side_layout(request.get('id'), request.get('proposal'), request.get('replaces'))
            elif self.path.endswith('/reject-side-candidate'):
                result = reject_side_candidate(request.get('id'), request.get('variant'), request.get('undo') is True)
            elif self.path.endswith('/main-variant-verdicts'):
                result = save_main_variant_verdicts(request.get('verdicts'))
            elif self.path.endswith('/select-side-variants'):
                result = select_side_variants(request.get('choices'), request.get('replace') is True)
            elif self.path.endswith('/deselect-side-variant'):
                result = deselect_side_variant(request.get('id'), request.get('variant'), refresh=False,
                                               when_empty=('unreviewed' if request.get('when_empty') == 'unreviewed'
                                                           else 'pending_human'))
                REFRESH.schedule()
            else:
                result = select_side_variant(request.get("id"), request.get("variant"), refresh=False)
                REFRESH.schedule()
        except (ValueError, KeyError, json.JSONDecodeError) as error:
            self.log_message('refused %s: %s', self.path.rsplit('/', 1)[-1], error)
            self.send_json(HTTPStatus.BAD_REQUEST, {"error": str(error)})
            return
        except Exception as error:
            self.log_message('failed %s: %r', self.path.rsplit('/', 1)[-1], error)
            self.send_json(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": str(error)})
            return
        key = 'counts' if self.path.endswith('/reject-main-variant') else 'result'
        self.send_json(HTTPStatus.OK, {"ok": True, key: result})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8769)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), GalleryHandler)
    print(f"Side combination gallery: http://127.0.0.1:{args.port}/side_combinations/", flush=True)
    try:
        server.serve_forever()
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
