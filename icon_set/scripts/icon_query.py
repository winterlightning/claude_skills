"""Icon review's list for deploy.py (GET /api/icons, /api/icons/facets, /api/icon): the page of cards, counts and
filter choices the Worker answers from D1 (cloud/worker/core/src/icon_query.rs), here over deploy.py's in-memory
catalog. Both follow gallery.html's list functions and are checked against the same answers
(cloud/worker/core/tests/fixtures/icon-query-expected.json, icon_set/tests/test_icon_query.py).
"""
from __future__ import annotations

from datetime import datetime
import json
import re

STATES = ('ready', 'failed', 'pending', 'approve', 'rejected')
SORTS = ('name', 'newest', 'oldest', 'modified-newest', 'modified-oldest', 'strokes-asc', 'strokes-desc', 'segments-asc', 'segments-desc')
PAGE_SIZES = (24, 48, 96, 192)
CHOICES = {'symmetry': ('symmetric', 'vertical', 'horizontal', 'both', 'asymmetric', 'unknown'),
           'strokes': ('1-3', '4-6', '7-10', '11+', 'unknown'), 'revision': ('original', 'variant'), 'reference': ('with', 'without'),
           'artwork': ('original', 'modified', 'edited', 'uploaded', 'work_fix'),
           'reason': ('bad-stroke', 'manual-fix-request', 'meaning', 'other', 'missing', 'cannot-fix'),
           'pending_feedback': ('with', 'without'), 'status': STATES, 'sort': SORTS}
COMBINED = ('side_combination64', 'container_combination64')
CARD_FIELDS = ('key', 'icon_id', 'name', 'family', 'category', 'profile', 'canvas_size', 'canvas_width', 'canvas_height', 'sizing_mode',
               'keyshape', 'keyshape_bounds', 'preview_url', 'svg_sha256', 'uploaded_icon', 'author', 'build_failed', 'errors', 'status',
               'variant_of', 'variant_root', 'variant_label', 'reference_fidelity', 'side_role', 'artwork_source')


def params(query: dict) -> dict:
    """The page's URL filters from a parse_qs dict; unknown values are ignored like the page's selects ignore them."""
    get = lambda name: (query.get(name) or [None])[0]  # noqa: E731
    text = lambda name: (get(name) or '').strip()  # noqa: E731
    p = {name: (get(name) if get(name) in allowed else '') for name, allowed in CHOICES.items()}
    p.update(family=text('family'), category=get('category') or None, q=text('q').lower(), reviewer=text('reviewer'),
             icon_feedback_by=text('icon_feedback_by'), keyshape=text('keyshape'), author=text('author'),
             versions=get('view') == 'versions')
    p['sort'] = p['sort'] or 'name'
    try:
        p['offset'] = max(0, int(get('offset') or 0))
    except ValueError:
        p['offset'] = 0
    try:
        p['limit'] = int(get('limit') or 48) if int(get('limit') or 48) in PAGE_SIZES else 48
    except ValueError:
        p['limit'] = 48
    if p['reason']:
        p['status'] = 'pending'
    if p['status'] != 'pending':
        p['pending_feedback'] = ''
    return p


def _model(record) -> bool:
    return not record.get('uploaded_icon') and (record.get('artwork_source') or 'use_org') == 'use_org' and isinstance(record.get('primitives'), list)


def stroke_count(record):
    """`strokeCount`: one per contour, plus each primitive no contour claims."""
    if not _model(record):
        return None
    contours = record.get('contours') or []
    claimed = {member for c in contours for member in (c.get('members') or [])}
    return len(contours) + sum(1 for p in record['primitives'] if p.get('element_id') not in claimed)


def segment_count(record):
    if not _model(record):
        return None
    return sum(max(1, len(p.get('segments') or [])) if p.get('kind') == 'bezier' else 1 for p in record['primitives'])


def version_group(record) -> str:
    return f"{record.get('family')}/{record.get('variant_root') or record.get('variant_of') or record.get('icon_id')}"


def version(record) -> int:
    if not record.get('variant_of'):
        return 1
    match = re.search(r'-v(\d+)$', record.get('icon_id') or '')
    return int(match.group(1)) if match else 2


def search_text(record) -> str:
    words = [record.get(f) for f in ('name', 'icon_id', 'variant_label', 'variant_root', 'category')]
    words += list(record.get('keywords') or []) + list(record.get('aliases') or [])
    return ' '.join('' if w is None else str(w) for w in words).lower()


def millis(value):
    try:
        return datetime.fromisoformat(value).timestamp() * 1000 if value else None
    except (TypeError, ValueError):
        return None


def card(record) -> dict:
    out = {f: record[f] for f in CARD_FIELDS if record.get(f) is not None}
    if record.get('original_sources'):
        out['original_sources'] = [{'url': record['original_sources'][0].get('url')}]
    if isinstance(record.get('validation'), dict):
        out['validation'] = {k: record['validation'][k] for k in ('status', 'automatic_status', 'exception') if k in record['validation']}
    return out


class Catalog:
    """The list's view of one moment: records with picks applied, review decisions, feedback, work and facets."""

    def __init__(self, records, statuses, approved_by, disapproved_by, rejected_by, feedback, work, facets):
        self.records = records
        self.statuses = statuses
        self.actors = {'approve': approved_by, 'pending': disapproved_by, 'rejected': rejected_by}
        self.facets = facets or {}
        self.work = work or {}
        self.feedback_by, self.with_feedback, self.reasons = {}, set(), {}
        current = {r['key']: r.get('svg_sha256') for r in records}
        latest = {}
        for row in feedback:
            self.with_feedback.add(row['icon'])
            if row.get('author') and row['icon'] in current and row['author'] not in self.feedback_by.setdefault(row['icon'], []):
                self.feedback_by[row['icon']].append(row['author'])
            if current.get(row['icon']) == row['svg_sha256'] and (row['icon'] not in latest or int(row['id']) > int(latest[row['icon']]['id'])):
                latest[row['icon']] = row
        self.reasons = {k: 'bad-stroke' if r.get('reason') == 'bad-draw' else r.get('reason') or 'other' for k, r in latest.items()}

    # ---- gallery.html list functions
    def state(self, icon) -> str:
        raw = self.statuses.get(icon['key']) or 'ready'
        if icon.get('family') in COMBINED and icon.get('build_failed') and raw not in ('rejected', 'pending'):
            return 'failed'
        current = 'ready' if raw == 're-generated' else 'pending' if raw in ('disapprove', 'claimed') else raw
        return 'failed' if current == 'ready' and icon.get('build_failed') else current

    def axes(self, icon):
        facet = self.facets.get(icon['key'])
        return facet.get('axes') if facet and facet.get('svg_sha256') == icon.get('svg_sha256') else None

    @staticmethod
    def artwork(icon) -> str:
        source = icon.get('artwork_source') or 'use_org'
        return ('edited' if source == 'use_edited' else 'uploaded' if source == 'use_upload' or (icon.get('uploaded_icon') and source == 'use_org')
                else 'work_fix' if source == 'work_fix' else 'original')

    def facets_match(self, icon, p) -> bool:
        symmetry, axes = p['symmetry'], self.axes(icon)
        if symmetry:
            if symmetry == 'unknown':
                if axes is not None:
                    return False
            elif axes is None or (not axes if symmetry == 'symmetric' else bool(axes) if symmetry == 'asymmetric'
                                  else not ('vertical' in axes and 'horizontal' in axes) if symmetry == 'both' else symmetry not in axes):
                return False
        count = stroke_count(icon)
        if p['strokes']:
            if p['strokes'] == 'unknown':
                if count is not None:
                    return False
            else:
                low, high = (11, float('inf')) if p['strokes'] == '11+' else map(int, p['strokes'].split('-'))
                if count is None or not low <= count <= high:
                    return False
        if p['keyshape'] and icon.get('keyshape') != p['keyshape']:
            return False
        if p['author'] and (icon.get('author') or 'unknown') != p['author']:
            return False
        if p['revision'] and bool(icon.get('variant_of')) != (p['revision'] == 'variant'):
            return False
        if p['reference'] and bool(icon.get('original_sources')) != (p['reference'] == 'with'):
            return False
        kind = self.artwork(icon)
        if p['artwork'] and (kind == 'original' if p['artwork'] == 'modified' else kind != p['artwork']):
            return False
        if p['reason'] == 'cannot-fix':
            claim = self.work.get(icon['key'])
            if self.state(icon) != 'pending' or not (claim and claim.get('svg_sha256') == icon.get('svg_sha256') and claim.get('state') == 'cannot-fix'):
                return False
        elif p['reason'] and (self.state(icon) != 'pending' or self.reasons.get(icon['key'], 'missing') != p['reason']):
            return False
        return True

    def search_match(self, icon, p, category=True) -> bool:
        family = p['family']
        if family in ('side_main', 'side_sub'):
            if icon.get('side_role') != family[5:]:
                return False
        elif family and icon.get('family') != family:
            return False
        if p['reviewer']:
            status = self.state(icon)
            if status not in ('approve', 'pending', 'rejected') or self.actors[status].get(icon['key']) != p['reviewer']:
                return False
        if p['icon_feedback_by'] and p['icon_feedback_by'] not in self.feedback_by.get(icon['key'], []):
            return False
        if not self.facets_match(icon, p) or p['q'] not in search_text(icon):
            return False
        return not category or not p['category'] or icon.get('category') == p['category']

    def in_section(self, icon, p) -> bool:
        if p['status']:
            return self.state(icon) == p['status']
        return bool(p['reviewer']) or self.state(icon) != 'rejected'

    def pending_match(self, icon, p) -> bool:
        if not p['pending_feedback']:
            return True
        has = icon['key'] in self.with_feedback
        return self.state(icon) == 'pending' and (has if p['pending_feedback'] == 'with' else not has)

    @staticmethod
    def sort_key(p):
        order = p['sort']
        name = lambda i: ((i.get('name') or i.get('icon_id') or '').lower(), i['key'].lower())  # noqa: E731
        measure = {'strokes': stroke_count, 'segments': segment_count}.get(order.split('-')[0])
        field = {'newest': 'created_at', 'oldest': 'created_at', 'modified-newest': 'modified_at', 'modified-oldest': 'modified_at'}.get(order)
        desc = order.endswith('-desc') or order.endswith('newest')
        def key(icon):
            value = measure(icon) if measure else millis(icon.get(field)) if field else None
            if not measure and not field:
                return (0, 0, name(icon))
            return (value is None, (-value if desc else value) if value is not None else 0, name(icon))
        return key

    def grouped(self, p) -> bool:
        narrowed = any(p[f] for f in ('symmetry', 'strokes', 'reason', 'keyshape', 'revision', 'reference', 'artwork', 'author',
                                      'reviewer', 'icon_feedback_by'))
        return p['versions'] and not narrowed and p['status'] != 'rejected' and not (p['status'] == 'pending' and p['pending_feedback'])

    def item(self, icon) -> dict:
        out = card(icon)
        key = icon['key']
        state = self.state(icon)
        actor = (self.actors.get(state) or {}).get(key)
        out.update(build_failed=bool(icon.get('build_failed')), stroke_count=stroke_count(icon), segment_count=segment_count(icon),
                   symmetry_axes=self.axes(icon), review={'state': state, 'status': self.statuses.get(key, 'ready'), 'by': actor},
                   work=self.work.get(key) if (self.work.get(key) or {}).get('svg_sha256') == icon.get('svg_sha256') else None)
        return out

    def list(self, p) -> dict:
        matching = [i for i in self.records if self.search_match(i, p)]
        rows = [i for i in matching if self.in_section(i, p) and self.pending_match(i, p)]
        if self.grouped(p):
            groups = {version_group(i) for i in rows}
            rows = [i for i in self.records if version_group(i) in groups and self.state(i) != 'rejected']
        rows.sort(key=self.sort_key(p))
        if p['versions']:
            units, index = [], {}
            for icon in rows:
                g = version_group(icon)
                if g not in index:
                    index[g] = len(units)
                    units.append([])
                units[index[g]].append(icon)
            for group in units:
                group.sort(key=lambda i: (version(i), i.get('icon_id') or ''))
        else:
            units = rows
        limit, offset = p['limit'], p['offset']
        if offset >= len(units) and units:
            offset = (len(units) - 1) // limit * limit
        visible = units[offset:offset + limit]
        page = [i for g in visible for i in g] if p['versions'] else visible
        states, categories = {}, {}
        for icon in matching:
            states[self.state(icon)] = states.get(self.state(icon), 0) + 1
        for icon in self.records:
            if self.search_match(icon, p, category=False) and self.in_section(icon, p) and self.pending_match(icon, p):
                categories[icon.get('category') or ''] = categories.get(icon.get('category') or '', 0) + 1
        return {'items': [self.item(i) for i in page], 'total': len(units), 'versions': len(rows), 'offset': offset, 'limit': limit,
                'states': states, 'categories': categories}

    def by_keys(self, keys) -> dict:
        wanted = set(keys)
        return {'items': [self.item(i) for i in self.records if i['key'] in wanted]}

    def facet_choices(self) -> dict:
        out = {'authors': {}, 'keyshapes': {}, 'categories': {}, 'families': {}, 'total': 0}
        for icon in self.records:
            out['authors'][icon.get('author') or 'unknown'] = out['authors'].get(icon.get('author') or 'unknown', 0) + 1
            out['families'][icon.get('family')] = out['families'].get(icon.get('family'), 0) + 1
            if icon.get('build_failed'):
                continue
            out['total'] += 1
            if icon.get('keyshape'):
                out['keyshapes'][icon['keyshape']] = out['keyshapes'].get(icon['keyshape'], 0) + 1
            if icon.get('category'):
                out['categories'][icon['category']] = out['categories'].get(icon['category'], 0) + 1
        return out

    def detail(self, key):
        icon = next((i for i in self.records if i['key'] == key), None)
        if icon is None:
            return None
        record = {k: v for k, v in icon.items() if k != 'uploaded_svg'}
        item = self.item(icon)
        record.update({k: item[k] for k in ('review', 'work', 'stroke_count', 'segment_count', 'symmetry_axes', 'build_failed')})
        return record


def work_claims(rows):
    """Work state of each current review row with a worker, as /api/work reports it (claims here have no lease left
    to check: a lapsed claim shows as no state, like the Worker's work_state)."""
    from datetime import timedelta, timezone
    out = {}
    now = datetime.now(timezone.utc)
    for icon, sha, status, worker, claimed_at, note, updated_at in rows:
        if not worker:
            continue
        state = None
        if status == 'claimed':
            try:
                started = datetime.fromisoformat((claimed_at or '').replace('Z', '+00:00'))
                state = 'working' if now < started + timedelta(hours=6) else None
            except ValueError:
                state = None
        elif status == 'ready':
            state = 'done'
        elif status == 'pending':
            state = 'cannot-fix'
        if state:
            out[icon] = {'state': state, 'worker': worker, 'note': note or '', 'claimed_at': claimed_at, 'updated_at': updated_at,
                         'svg_sha256': sha}
    return out


def dumps(value) -> bytes:
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
