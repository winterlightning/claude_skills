"""Saved reference briefs, independent of a primitive's remake status."""
from datetime import datetime, timezone

FAMILIES = ('sub', 'solo', 'container', 'avatar')
MAX_BRIEF = 20000


def init_primitive_briefs(connection):
    connection.execute('''CREATE TABLE IF NOT EXISTS primitive_briefs (
        uuid TEXT PRIMARY KEY, family TEXT NOT NULL, brief TEXT NOT NULL,
        updated_by TEXT NOT NULL, updated_at TEXT NOT NULL)''')


def load_primitive_briefs(connection):
    return {uid: dict(family=family, brief=brief, updated_by=user, updated_at=at)
            for uid, family, brief, user, at in connection.execute(
                'SELECT uuid, family, brief, updated_by, updated_at FROM primitive_briefs')}


def save_primitive_brief(connection, uid, family, brief, *, known, user, record, authority='unspecified'):
    if not isinstance(uid, str) or uid not in known:
        raise ValueError('Choose a known primitive.')
    if family not in FAMILIES:
        raise ValueError('Choose an icon family: sub, solo, container or avatar.')
    if not isinstance(brief, str) or not brief.strip() or len(brief) > MAX_BRIEF:
        raise ValueError(f'Enter a brief of 1–{MAX_BRIEF:,} characters.')
    brief = brief.strip()
    previous = connection.execute('SELECT family, brief FROM primitive_briefs WHERE uuid=?', (uid,)).fetchone()
    if previous != (family, brief):
        now = datetime.now(timezone.utc).isoformat()
        connection.execute('INSERT INTO primitive_briefs VALUES (?,?,?,?,?) ON CONFLICT(uuid) DO UPDATE SET '
                           'family=excluded.family, brief=excluded.brief, updated_by=excluded.updated_by, '
                           'updated_at=excluded.updated_at', (uid, family, brief, user, now))
        record(connection, user, 'primitive_brief', 'primitive:' + uid, family=family, brief=brief,
               previous_family=previous[0] if previous else None, authority=authority)
    return load_primitive_briefs(connection)[uid]


def generation_queue(catalog, statuses, briefs, query, classification_history=None):
    """Read-only, deterministic authoring handoff; never calls a model or saves briefs."""
    import re
    from urllib.parse import quote
    try:
        from .primitive_status import merge, filter_rows
    except ImportError:
        from primitive_status import merge, filter_rows

    one = lambda key, default='': query.get(key, [default])[0]
    family = one('family', 'solo')
    if family not in FAMILIES:
        raise ValueError('Choose family: solo, sub, container or avatar.')
    brief_filter = one('brief')
    if brief_filter not in ('', 'ready', 'missing'):
        raise ValueError('Choose brief: ready or missing, or omit it for all TODO icons.')
    try:
        limit, offset = int(one('limit', '50')), int(one('offset', '0'))
    except ValueError:
        raise ValueError('limit and offset must be integers.') from None
    if not 1 <= limit <= 500 or offset < 0:
        raise ValueError('limit must be 1–500 and offset must be nonnegative.')
    rows = []
    term = one('q').casefold()
    for row in filter_rows(merge(catalog['rows'], statuses), one('category'), 'todo', one('batch')):
        saved = briefs.get(row['uuid'])
        ready = bool(saved and saved.get('family') in FAMILIES and saved.get('brief', '').strip())
        if brief_filter and ready != (brief_filter == 'ready'):
            continue
        if term and term not in ' '.join(str(row.get(k, '')) for k in ('concept', 'old_concept', 'path', 'uuid')).casefold():
            continue
        rows.append((row, saved if ready else None))
    rows.sort(key=lambda pair: (pair[0]['path'], pair[0]['uuid']))
    items = []
    for row, saved in rows[offset:offset + limit]:
        name = row.get('concept') or row.get('old_concept') or 'Unnamed icon'
        icon_id = row.get('proposed_icon_id') or re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
        if not re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', icon_id):
            icon_id = 'icon-' + (icon_id or row['uuid'])
        source = catalog.get('root_label', 'pictographic-primitives').rstrip('/') + '/' + row['path']
        reference_url = '/primitives/' + quote(row['path'], safe='/')
        chosen = saved['family'] if saved else family
        skill = 'icon-solo-distilled' if chosen == 'solo' else f'icon-{chosen}'
        design_root = 'icon_set/skills/icon-design' + ('-distilled' if chosen == 'solo' else '')
        size = 32 if chosen == 'sub' else 64 if chosen == 'container' else 48
        tags = row.get('tags') or [word for word in re.split(r'\W+', name.lower()) if word]
        if isinstance(tags, str):
            tags = [tags]
        template = f"""# {name}

- source: `{source}`
- reference: `{reference_url}` (render and look at this first)
- native size: {size}px (render the source before authoring)
- tags: {', '.join(tags)}
- family: {chosen} — author with `${skill}`
- proposed icon_id: `{icon_id}`
- source UUID: `{row['uuid']}`

## To author

Run `${skill}` and follow its shared guidance in `{design_root}/`, including
the reference-backed intake. Look at the render before choosing anything: name the subject in
one sentence, keep only what survives at native size, choose the keyshape,
and design backwards from its four extreme coordinates.

The reference sets the subject, not the grid, the stroke or the
proportions. Fit the result to the requested profile.

You can try modifying a copy of the SVG reference to fit the icon design rules,
or generate a new icon that matches the icon name. Either approach must follow
the requested family's design rules and preserve the named subject's identity.
Keep the original reference unchanged and produce the family skill's required deliverables.

## Fit the icon design rules

Adapt or regenerate the reference to fit: fewer parts, the profile's stroke
weight, larger gaps, geometry rebuilt on the grid. Keep the meaning intact —
the recognizable silhouette and the parts that distinguish the subject.
Simplify the drawing, never the meaning.

## Reference triage

This template is prepared from catalog metadata without visual review. Confirm
the requested family before drawing. Follow `{design_root}/reference-triage.md`; route combined
subjects to `$icon-making` for component briefs, and text/numbers to `{design_root}/typeface.md`.
"""
        exported_brief = saved['brief'] if saved else template
        if saved and chosen == 'solo':
            # Adapt only the exported handoff; retain the stored editorial brief.
            exported_brief = re.sub(r'\$icon-solo(?![-\w])', '$icon-solo-distilled', exported_brief)
            exported_brief = exported_brief.replace('icon_set/skills/icon-design/', design_root + '/')
        from icon_set.scripts.primitive_decision_history import handoff_decision
        history = (classification_history or {}).get(row['uuid'], [])
        decision = handoff_decision(history, chosen, saved)
        if decision['authoritative']:
            # Remove the generic invitation to reclassify from generated templates.
            if not saved:
                exported_brief = exported_brief.split('## Reference triage')[0].rstrip()
            exported_brief = '## User classification — takes priority\n\n' + decision['instruction'] + '\n\n' + exported_brief
        items.append(dict(uuid=row['uuid'], concept=name, category=row['category'],
                          batch=row.get('batch'), reference_path=source, reference_url=reference_url,
                          family=chosen, skill=skill, proposed_icon_id=icon_id, tags=tags,
                          brief_source='saved' if saved else 'template',
                          classification_history=history, classification_decision=decision,
                          brief=exported_brief))
    return dict(total=len(rows), offset=offset, limit=limit,
                next_offset=offset + limit if offset + limit < len(rows) else None,
                instruction='Recheck TODO status before drawing. Follow authoritative user classification decisions; do not reclassify or split those references. Inspect geometry and follow the family drawing rules.',
                briefs=items)
