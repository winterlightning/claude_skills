"""SQL that fills the fill side pairs tables (migration 0023) from this workspace's build, the way
cloud/migrate/backfill_combinations.py fills the combination tables: run deliberately with wrangler d1 execute.

    python3 -m icon_set side-fill d1-import                 # writes the two files below
    (cd cloud/worker && npx wrangler d1 execute pictographic-review-next --remote --file ../../icon_set/state/side-fill/side-fill-import.sql)
    python3 cloud/migrate/upload_fill_parts.py --base-url … --send       # the fill variant icons
    (cd cloud/worker && npx wrangler d1 execute pictographic-review-next --remote --file ../../icon_set/state/side-fill/side-fill-picks.sql)

side-fill-import.sql   fill_pairs, fill_parts and fill_counts, upserted: a pair edited on the site keeps its state, a
                       part filled on the site stays filled, and the totals are counted from the rows written
side-fill-picks.sql    reference_part_fills: each pair's picks in order, rank 1 its output. Each pick names its fill
                       variant icon by key (fill_icons.fill_key) and is written only when that icon exists, so it runs
                       after the upload; a pick whose variant was not uploaded is skipped. Upserted: a pick keeps its
                       output (combined) and, when its choice is unchanged, its built drawing (built_sha). The picks
                       of a pair edited on the site (fill_pairs.edited_at) are never touched, and only imported rows
                       the build no longer has are removed.
                       An outline pick uses the solo / sub icon itself.
Every statement is a write keyed by primary key or a lookup on an index: nothing here scans a table.
"""
import argparse
import json
from datetime import datetime, timezone

from .fill_icons import fill_key
from .paths import DATA, WORK

IMPORT = WORK / 'side-fill-import.sql'
PICKS = WORK / 'side-fill-picks.sql'


def q(value):
    if value is None:
        return 'NULL'
    if isinstance(value, (int, float)):
        return str(int(value)) if float(value).is_integer() else str(value)
    return "'" + str(value).replace("'", "''") + "'"


def sort_key(text, ref):
    return f'{(text or "").lower()} {ref}'


NO_FILL_NOTE = 'Neither the main nor the sub has a fill: this pair has no fill version.'   # core side_fill::NO_FILL_NOTE
READY_NOTE = 'Has a fill: combined in its pairs.'
NOT_EDITED = "NOT EXISTS (SELECT 1 FROM fill_pairs e WHERE e.reference_id = {ref} AND e.edited_at IS NOT NULL)"


def pick_statement(ref, role, rank, icon, layout, options, now, exists=False):
    """One imported pick row: written unless the pair was edited on the site, as an upsert that keeps its output and
    (with the same icon, layout and options) its built drawing. `exists`: only when the icon is there (a variant)."""
    where = NOT_EDITED.format(ref=q(ref)) + (f" AND EXISTS (SELECT 1 FROM icons WHERE key = {q(icon)})" if exists else '')
    return (f"INSERT INTO reference_part_fills(reference_id, role, rank, icon, layout, options, updated_at, updated_by) "
            f"SELECT {q(ref)}, {q(role)}, {rank}, {q(icon)}, {q(layout)}, {q(options)}, {q(now)}, 'side-fill import' WHERE {where} "
            f"ON CONFLICT(reference_id, role, rank) DO UPDATE SET "
            f"built_sha = CASE WHEN reference_part_fills.icon IS excluded.icon AND reference_part_fills.layout IS excluded.layout "
            f"AND reference_part_fills.options IS excluded.options THEN reference_part_fills.built_sha END, "
            f"icon = excluded.icon, layout = excluded.layout, options = excluded.options, updated_at = excluded.updated_at "
            f"WHERE reference_part_fills.updated_by = 'side-fill import';")


def picks_head(keys):
    """Removes the imported picks this build no longer has (`keys`: 'ref role rank'), of pairs not edited on the site."""
    return ("DELETE FROM reference_part_fills WHERE updated_by = 'side-fill import' AND " + NOT_EDITED.format(ref='reference_part_fills.reference_id')
            + f" AND (reference_id || ' ' || role || ' ' || rank) NOT IN (SELECT value FROM json_each({q(json.dumps(sorted(keys)))}));")


def pair_statement(ref, sort, state, main, sub, layouts, note, now):
    """One fill_pairs row, upserted: a pair edited on the site keeps its state and note, and one a site fill made
    pickable (FIRST_FILL) is not put back to waiting for a fill."""
    return (f"INSERT INTO fill_pairs(reference_id, sort_key, state, main_source, sub_source, main_layout, sub_layout, note, updated_at) "
            f"VALUES ({q(ref)}, {q(sort)}, {q(state)}, {q(main)}, {q(sub)}, {layouts[0]}, {layouts[1]}, {q(note)}, {q(now)}) "
            f"ON CONFLICT(reference_id) DO UPDATE SET sort_key = excluded.sort_key, main_source = excluded.main_source, "
            f"sub_source = excluded.sub_source, main_layout = excluded.main_layout, sub_layout = excluded.sub_layout, "
            f"state = CASE WHEN fill_pairs.edited_at IS NOT NULL THEN fill_pairs.state "
            f"WHEN fill_pairs.state = 'unpicked' AND excluded.state = 'uncombined' AND excluded.note = {q(NO_FILL_NOTE)} THEN 'unpicked' "
            f"ELSE excluded.state END, "
            f"note = CASE WHEN fill_pairs.edited_at IS NOT NULL OR (fill_pairs.state = 'unpicked' AND excluded.note = {q(NO_FILL_NOTE)}) "
            f"THEN fill_pairs.note ELSE excluded.note END, updated_at = excluded.updated_at;")


def part_statement(key, role, sort, status, note, text, pair_count, now):
    """One fill_parts row, upserted: a part filled on the site (FIRST_FILL) stays filled."""
    return (f"INSERT INTO fill_parts(key, role, sort_key, status, note, text, pair_count, updated_at) VALUES "
            f"({q(key)}, {q(role)}, {q(sort)}, {q(status)}, {q(note)}, {q(text)}, {pair_count}, {q(now)}) "
            f"ON CONFLICT(key) DO UPDATE SET role = excluded.role, sort_key = excluded.sort_key, text = excluded.text, "
            f"pair_count = excluded.pair_count, updated_at = excluded.updated_at, "
            f"status = CASE WHEN fill_parts.status = 'ready' AND excluded.status IN ('no-fill', 'outline') THEN 'ready' ELSE excluded.status END, "
            f"note = CASE WHEN fill_parts.status = 'ready' AND excluded.status IN ('no-fill', 'outline') THEN fill_parts.note ELSE excluded.note END;")


# The totals, counted from the rows written (one pass over each table, at import only).
COUNTS = ["DELETE FROM fill_counts;",
          "UPDATE fill_pairs SET state = 'picked', note = NULL WHERE state != 'picked' "
          "AND EXISTS (SELECT 1 FROM reference_part_fills p WHERE p.reference_id = fill_pairs.reference_id);",
          "INSERT INTO fill_counts(scope, status, n) SELECT 'pairs', state, COUNT(*) FROM fill_pairs GROUP BY state;",
          "INSERT INTO fill_counts(scope, status, n) SELECT 'pairs', 'all', COUNT(*) FROM fill_pairs;",
          "INSERT INTO fill_counts(scope, status, n) SELECT role, status, COUNT(*) FROM fill_parts GROUP BY role, status;",
          "INSERT INTO fill_counts(scope, status, n) SELECT role, 'all', COUNT(*) FROM fill_parts GROUP BY role;"]


def keyshape_fits():
    """{pair: {rank: {main, sub, keyshape}}}: picks laid out again to fill the 64px keyshape, by rank."""
    path = DATA / 'data/keyshape-fit-layouts.json'
    return json.loads(path.read_text())['pairs'] if path.is_file() else {}


def gallery_rows():
    text = (WORK / 'gallery-data.js').read_text()
    return {row['id']: row for row in json.loads(text[text.index('{'):text.rindex('}') + 1])['rows']}


def uncombined_note(parts, error):
    """Why the combine could not draw a pair."""
    if parts.get('sub') and not parts['sub'].get('icon'):
        return 'Text sub: the fill combine does not place text subs yet.'
    if parts.get('main') and not parts['main'].get('icon'):
        return 'No main drawn yet.'
    if error and 'differs from its layout hash' in error:
        return f'The {error.split()[0]} was redrawn since the pair was laid out.'
    return f'Not combined: {error}' if error else 'Not combined.'


def uploaded_variants():
    """{(source_key, variant)} of the fill variant icons exported for upload (side-fill icons)."""
    path = WORK / 'fill-icons/manifest.json'
    return {(m['source_key'], m['variant']) for m in json.loads(path.read_text())} if path.is_file() else set()


def resolve(source, label, available):
    """The label a pick can use: itself when uploaded; else the same picture under another name (a region / group
    hidden as a duplicate of current → current; an outline-only part's current / fill, which is its outline → the
    outline, i.e. the solo / sub icon). None when nothing fits."""
    if label == 'outline' or (source, label) in available:
        return label
    if label.startswith(('region-', 'group-')) and (source, 'current') in available:
        return 'current'
    return 'outline'


def rejected_variants():
    """Whether (main key, label) is a main region / group variant rejected in review (the variants index, or the
    main's variant policy and the user's main48 marks): never uploaded, never picked."""
    from .adaptive_overlap import main_variant_policy, variant_rejected
    index = json.loads((WORK / 'main-variants/index.json').read_text())
    listed = {(f'solo/{name}', v['variant']) for name, entry in index.items() for v in entry.get('variants', [])
              if v.get('status') == 'rejected'}
    policies = {}

    def rejected(key, label):
        if not key or not label or not label.startswith(('region-', 'group-')):
            return False
        if (key, label) in listed:
            return True
        name = key.split('/', 1)[1]
        if name not in policies:
            policies[name] = main_variant_policy(name)
        return variant_rejected(policies[name], label)
    return rejected


def pick_specs(rows=None, available=None, fallbacks=None, dropped=None):
    """Every pair's picks in order, as reference_part_fills holds them:
    [{reference_id, rank, variant, options, roles: {main|sub: {source, label, layout}}}]. `label` is the fill variant
    (resolve()); 'outline' means the solo / sub icon itself. `options` (main row): omit (main element numbers left
    out) and overlap 'join' of a layout proposal."""
    rows = gallery_rows() if rows is None else rows
    available = uploaded_variants() if available is None else available
    items = json.loads((DATA / 'data/production-layouts.json').read_text())['items']
    layout_renders = json.loads((WORK / 'ai-layout-proposals/report.json').read_text())['pairs']
    specs = json.loads((DATA / 'data/ai-layout-proposals.json').read_text())['pairs']
    rejected = rejected_variants()
    out = []
    for item in items:
        ref = item['reference_id']
        parts = {p['role']: p for p in item['parts']}
        row = rows.get(ref)
        proposals = (row or {}).get('proposed_variants') or [] if row and row.get('selection_status') == 'selected' else []
        combos = {c['variant']: c for c in (row or {}).get('variant_combinations', [])}
        rank = 0
        for variant in proposals:
            c = combos.get(variant, {})
            base = c.get('base_variant') if c.get('kind') == 'layout' else variant
            if rejected(parts.get('main', {}).get('icon'), base):
                # A pick of a rejected variant is dropped; the later picks move up.
                if dropped is not None:
                    dropped.append({'reference_id': ref, 'variant': variant})
                continue
            rank += 1
            options = {}
            if c.get('kind') == 'layout':
                base, sub_variant = c.get('base_variant'), c.get('sub_variant') or 'fill'
                render = next((r for r in layout_renders.get(ref, {}).get('candidates', []) if r['variant'] == variant), {})
                boxes = render.get('layout_boxes') or {}
                spec = next((p for p in specs.get(ref, []) if f'layout-{p["id"]}' == variant), {})
                if spec.get('omit_main_elements'):
                    options['omit'] = sorted(spec['omit_main_elements'])
                if spec.get('overlap_mode') == 'join':
                    options['overlap'] = 'join'
                if sub_variant == 'fill' and spec.get('sub', {}).get('size', 99) < 20:
                    options['sub_scaled'] = True
            else:
                base, sub_variant = variant, 'fill'
                boxes = {role: parts[role].get('layout') for role in ('main', 'sub') if role in parts}
            roles = {}
            for role, label in (('main', base), ('sub', sub_variant)):
                source = parts.get(role, {}).get('icon')
                if not source:
                    continue
                resolved = resolve(source, label, available)
                if resolved != label and fallbacks is not None:
                    fallbacks[f'{label} → {resolved}'] = fallbacks.get(f'{label} → {resolved}', 0) + 1
                roles[role] = {'source': source, 'label': resolved, 'layout': boxes.get(role)}
            out.append({'reference_id': ref, 'rank': rank, 'variant': variant, 'options': options, 'roles': roles})
    return out


def build():
    from .parts import parts_listing
    available = uploaded_variants()
    fallbacks = {}
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    rows = gallery_rows()
    items = json.loads((DATA / 'data/production-layouts.json').read_text())['items']
    errors = {e['id']: e['error'] for e in json.loads((WORK / 'recombined-all/report.json').read_text()).get('errors', [])}
    pairs, picks, counts, dropped = [], [], {}, []
    specs = pick_specs(rows, available, fallbacks, dropped)
    picked = {spec['reference_id'] for spec in specs}
    filled = {source for source, _label in available}          # parts with a fill variant icon
    for item in items:
        ref = item['reference_id']
        parts = {p['role']: p for p in item['parts']}
        row = rows.get(ref)
        state = 'uncombined' if row is None else 'picked' if ref in picked else 'unpicked'
        note = uncombined_note(parts, errors.get(ref)) if row is None else None
        if state == 'unpicked' and not any(p.get('icon') in filled for p in parts.values()):
            # A fill side pair needs a filled main or sub: with both outline only there is nothing to pick.
            state, note = 'uncombined', NO_FILL_NOTE
        counts[('pairs', state)] = counts.get(('pairs', state), 0) + 1
        layouts = [q(json.dumps(parts[r]['layout']) if parts.get(r, {}).get('layout') else None) for r in ('main', 'sub')]
        pairs.append(pair_statement(ref, sort_key(item['concept'], ref), state, parts.get('main', {}).get('icon'),
                                    parts.get('sub', {}).get('icon'), layouts, note, now))
    listed = [item['reference_id'] for item in items]
    pairs.append(f"DELETE FROM fill_pairs WHERE reference_id NOT IN (SELECT value FROM json_each({q(json.dumps(listed))}));")
    fitted = keyshape_fits()
    keys = set()
    for spec in specs:
        ref, rank = spec['reference_id'], spec['rank']
        fit = fitted.get(ref, {}).get(str(rank))
        for role, part in spec['roles'].items():
            # A pick laid out again to fill the 64px keyshape (cloud/migrate/fit_fill_keyshapes.mjs) uses those boxes.
            boxes = fit[role] if fit else part['layout']
            layout = json.dumps(boxes) if boxes else None
            options = json.dumps(spec['options'], sort_keys=True) if role == 'main' and spec['options'] else None
            keys.add(f'{ref} {role} {rank}')
            if part['label'] == 'outline':      # the outline is the solo / sub icon itself
                picks.append(pick_statement(ref, role, rank, part['source'], layout, options, now))
            else:
                picks.append(pick_statement(ref, role, rank, fill_key(part['source'], part['label']), layout, options, now, exists=True))
    mains, subs = parts_listing(set(rows))
    from .fill_icons import site_fill
    from .parts import STATUS_NOTE
    parts_sql = []
    for role, listing in (('main', mains), ('sub', subs)):
        for entry, art in listing:
            if entry['status'] == 'redrawn' and site_fill(role, entry):
                # Its fill is of the site's current drawing (side-fill sources): its pairs are picked on that drawing
                # (pick_new_pairs.mjs), so it is a filled part like any other.
                entry = {**entry, 'status': 'ready', 'note': STATUS_NOTE['ready']}
            counts[(role, entry['status'])] = counts.get((role, entry['status']), 0) + 1
            parts_sql.append(part_statement(entry['key'], role, sort_key(entry['name'], entry['key']), entry['status'],
                                            entry['note'], art.get('text'), len(entry['pairs']), now))
    listed_parts = [entry['key'] for listing in (mains, subs) for entry, _ in listing]
    parts_sql.append(f"DELETE FROM fill_parts WHERE key NOT IN (SELECT value FROM json_each({q(json.dumps(listed_parts))}));")
    IMPORT.write_text('\n'.join(pairs + parts_sql + COUNTS) + '\n')
    # Picks made or changed on the site are kept; open pair pages of the pairs whose picks this may change reload.
    PICKS.write_text('\n'.join([picks_head(keys)] + picks + COUNTS
                               + ["UPDATE fill_pairs SET version = version + 1 WHERE edited_at IS NULL;"]) + '\n')
    return {'pairs': len(items), 'parts': len(listed_parts), 'pick_rows': len(picks), 'pick_fallbacks': fallbacks, 'dropped_rejected_picks': len(dropped),
            'counts': {f'{s}:{st}': n for (s, st), n in counts.items()}, 'import_sql': str(IMPORT), 'picks_sql': str(PICKS)}


def main(argv=None):
    argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter).parse_args(argv)
    print(json.dumps(build(), indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
