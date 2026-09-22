"""Read-only generation queue for unresolved side-combination components."""
from __future__ import annotations

import re


ROLES = ('main', 'sub')


def generation_queue(combinations, primitives, statuses, *, role='all', limit=10, offset=0, q=''):
    """Return distinct missing side components, deduplicated by canonical primitive UUID."""
    if role not in ('all', *ROLES):
        raise ValueError('role must be all, main or sub.')
    if not 1 <= limit <= 500 or offset < 0:
        raise ValueError('limit must be 1–500 and offset must be nonnegative.')
    refs = combinations['references']
    sources = {row['uuid']: row for row in primitives['rows']}
    groups = {}
    for row in combinations['rows']:
        if row['kind'] != 'side':
            continue
        completed = ((row.get('component_selection') != 'explicit' and refs[row['id']]['generated'])
                     or row.get('generated'))
        if completed:
            continue
        generated = {
            'main': refs[row['main_id']]['generated'],
            'sub': row['sub_generated'] if 'sub_generated' in row else refs[row['sub_id']]['generated'],
        }
        for component_role in ROLES:
            if generated[component_role] or role not in ('all', component_role):
                continue
            source_id = row[component_role + '_id']
            ref = refs[source_id]
            uid = ref.get('canonical_id', source_id)
            key = (component_role, uid)
            group = groups.setdefault(key, {
                'uuid': uid, 'role': component_role, 'concept': ref.get('concept') or uid,
                'reference_url': ref.get('reference_url'), 'source_ids': set(), 'uses': {},
            })
            group['source_ids'].add(source_id)
            group['uses'][row['id']] = {'combination_id': row['id'], 'concept': row['concept']}

    marked_text_by_role = {component_role: 0 for component_role in ROLES}
    items = []
    term = q.casefold()
    for (component_role, uid), group in sorted(
            groups.items(), key=lambda pair: (pair[0][0], pair[1]['concept'].casefold(), pair[0][1])):
        if statuses.get(uid, {}).get('reason') == 'text_number':
            marked_text_by_role[component_role] += 1
            continue
        source = sources.get(uid, {})
        aliases = sorted(source_id for source_id in group['source_ids'] if source_id != uid)
        searchable = ' '.join([group['concept'], uid, *aliases,
                               *(use['concept'] for use in group['uses'].values())]).casefold()
        if term and term not in searchable:
            continue
        family, skill, size = (('solo', 'icon-solo-distilled', 48)
                               if component_role == 'main' else ('sub', 'icon-sub', 32))
        proposed = re.sub(r'[^a-z0-9]+', '-', group['concept'].lower()).strip('-')
        if not proposed or not proposed[0].isalpha():
            proposed = 'icon-' + (proposed or uid)
        reference_url = '/gallery/' + group['reference_url'] if group['reference_url'] else None
        path = source.get('path')
        reference_path = (primitives.get('root_label', 'pictographic-primitives').rstrip('/') + '/' + path
                          if path else None)
        exclusions = ('Generate only the standalone main subject. Exclude every adjacent, floating or overlapping '
                      'sub-icon modifier from the side combinations.' if component_role == 'main' else
                      'Generate only the isolated modifier glyph. Exclude the main subject, and complete any outline '
                      'hidden by overlap so the sub icon stands alone.')
        alias_line = f"\n- primitive aliases: {', '.join(f'`{alias}`' for alias in aliases)}" if aliases else ''
        brief = f"""# {group['concept']}

- role: {component_role} component of side combinations
- source UUID: `{uid}`{alias_line}
- source: `{reference_path or 'catalog reference only'}`
- reference: `{reference_url or 'reference unavailable'}` (render and inspect this first)
- native size: {size}px
- family: {family} — author with `${skill}`
- proposed icon_id: `{proposed}`
- needed by: {len(group['uses'])} side combination{'s' if len(group['uses']) != 1 else ''}

## To author

Run `${skill}` and follow its shared guidance. {exclusions}
Preserve the recognizable identity of the isolated primitive, fit it to the {family} profile,
validate it, and keep the source UUID attribution above.
"""
        items.append({
            'uuid': uid, 'source_id': uid, 'source_ids': [uid, *aliases],
            'concept': group['concept'], 'category': source.get('category', ''),
            'batch': source.get('batch'), 'role': component_role, 'family': family,
            'skill': skill, 'canvas_size': size, 'proposed_icon_id': proposed,
            'reference_path': reference_path, 'reference_url': reference_url,
            'brief_source': 'template', 'brief': brief,
            'combination_count': len(group['uses']),
            'combinations': list(group['uses'].values()),
        })
    total = len(items)
    missing_by_role = {
        component_role: sum(item['role'] == component_role for item in items)
        for component_role in ROLES
    }
    return {
        'total': total, 'offset': offset, 'limit': limit,
        'next_offset': offset + limit if offset + limit < total else None,
        'role': role, 'requirements_total': len(groups),
        'missing_by_role': missing_by_role,
        'marked_text_requirements': sum(marked_text_by_role.values()),
        'marked_text_by_role': marked_text_by_role,
        'missing_requirements': total,
        'instruction': ('One item per canonical primitive and component role. Recheck the live page before authoring; '
                        'generated components and text/number classifications are excluded.'),
        'briefs': items[offset:offset + limit],
    }
