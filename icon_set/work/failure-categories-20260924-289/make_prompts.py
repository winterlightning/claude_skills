"""Categorize the "Drawn, unpublished" primitives (build_failed, not skipped) and write primitive-make-ray repair prompts.

    /opt/homebrew/bin/python3 icon_set/work/failure-categories-20260924-289/make_prompts.py [status.json]
status.json is /api/primitives/status (skip decisions); without it no row is treated as skipped.
"""
import collections, csv, glob, json, os, re, sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BATCH = 15
ORDER = ['bounds', 'symmetry', 'spacing', 'parallel', 'clearance', 'pinches', 'holes', 'other']
LABEL = {'bounds': 'keyshape bounds', 'symmetry': 'near-miss symmetry', 'spacing': 'part spacing under 8',
         'parallel': 'parallel straight edges under 8', 'clearance': 'internal ink clearance under 4',
         'pinches': 'pinches', 'holes': 'undersized holes', 'other': 'other build failures'}
TYPE = {
 'bounds': "Keyshape bounds: the visible ink does not exactly match the chosen keyshape envelope (rectangles fit with tolerance 0; CIRCLE is radial). Choose the keyshape first, get its extremes from Keyshape.<TOKEN>.bounds_for(Profile.SOLO48), and design backwards so the outermost strokes sit exactly on the centerline box. Put arc centres on integer points with the apex at the endpoint so nothing overshoots or falls short.",
 'symmetry': "Near-miss symmetry: the ink is about 98% mirrored but the centerlines are off by under 1 unit. Either make the subject exactly symmetric (shared axis, mirrored coordinates, equal radii) or make any asymmetry deliberate and clearly larger.",
 'spacing': "Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.",
 'parallel': "Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.",
 'clearance': "Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.",
 'pinches': "Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.",
 'holes': "Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.",
 'other': "Other build failure: read the listed error, repair the named element, and pass every check below.",
}
COMMON = [
 "Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as \"Drawn, unpublished\" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.",
 None,  # failure type line
 "validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported \"valid\" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.",
 "Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set \"build_gate\": \"pass\" or \"fail\" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.",
]

def kinds(errors):
    found = set()
    for e in errors:
        if 'bounds' in e: found.add('bounds')
        elif e.startswith('symmetry'): found.add('symmetry')
        elif 'parallel straight' in e: found.add('parallel')
        elif 'apart on centerlines' in e: found.add('spacing')
        elif 'internal-spacing' in e or 'ink clearance' in e: found.add('clearance')
        elif 'holes/pinches' in e:
            m = re.search(r'(\d+) undersized holes; (\d+) pinches', e)
            if not m or int(m[1]): found.add('holes')
            if not m or int(m[2]): found.add('pinches')
        else: found.add('other')
    return found

def short(e):
    e = re.sub(r'SOLO48 requires at least 8 \(ink clearance 4\).*', '(needs 8)', e.strip())
    return re.sub(r'(\d+\.\d{3})\d+', r'\1', e)[:230]

def main():
    statuses = {}
    if len(sys.argv) > 1:
        statuses = json.load(open(sys.argv[1])); statuses = statuses.get('statuses', statuses)
    rows = json.load(open(REPO / 'published/gallery/primitives.json'))['rows']
    fail = {}
    for mf in glob.glob(str(REPO / 'published/failed/*/manifest.json')):
        folder = Path(mf).parent
        for it in json.load(open(mf))['icons']:
            fail[it['icon_id']] = {**it, '_svg': str((folder / it['svg']).relative_to(REPO))}
    promoted = {}
    for p in glob.glob(str(REPO / 'icon_set/work/*/*/*/promoted.json')):
        promoted[os.path.basename(json.load(open(p))['module'])] = Path(p).parts[-4]
    items = []
    for r in rows:
        if r['state'] == 'generated' or statuses.get(r['uuid']):
            continue
        if not (r.get('models') or r['state'] in ('model_only', 'build_failed', 'work_only')):
            continue
        records = [fail[m] for m in r.get('models', []) if m in fail]
        errors = [e for rec in records for e in rec.get('errors', [])]
        found = kinds(errors) or {'other'}
        primary = next(k for k in ORDER if k in found)
        ref = f"pictographic-primitives/{r['path']}"
        runs_dir = REPO / 'icon_set/work/primitive-make-ray' / r['uuid']
        runs = sorted(p.name for p in runs_dir.iterdir() if (p / 'result.json').is_file()) if runs_dir.is_dir() else []
        module = os.path.basename(records[0].get('source_path') or '') if records else ''
        items.append(dict(uuid=r['uuid'], category=r['category'], concept=r.get('concept', ''),
                          icon_id=';'.join(x['icon_id'] for x in records), reference=ref,
                          reference_exists=(REPO / ref).is_file(), primary=primary,
                          all=' '.join(k for k in ORDER if k in found),
                          origin=promoted.get(module, 'model tree'), previous_runs=len(runs),
                          newest_run=runs[-1] if runs else '', current=';'.join(x['_svg'] for x in records),
                          errors=errors))
    with open(OUT / 'failures.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['uuid', 'category', 'concept', 'icon_id', 'reference', 'primary', 'all_categories', 'origin',
                    'previous_runs', 'newest_run', 'current_drawing', 'error_count', 'first_errors'])
        for i in items:
            w.writerow([i['uuid'], i['category'], i['concept'], i['icon_id'], i['reference'], i['primary'], i['all'],
                        i['origin'], i['previous_runs'], i['newest_run'], i['current'], len(i['errors']),
                        ' | '.join(short(e) for e in i['errors'][:3])])
    by = collections.defaultdict(list)
    for i in items: by[i['primary']].append(i)
    # One batch holds any mix of failures; each file lists every rule it breaks with that rule's errors.
    ordered = sorted(items, key=lambda i: i['reference'].lower())
    total = (len(ordered) + BATCH - 1) // BATCH
    prompts = []
    for b in range(total):
        chunk = ordered[b * BATCH:(b + 1) * BATCH]
        rules = [k for k in ORDER if any(k in i['all'].split() for i in chunk)]
        lines = [f"Run $primitive-make-ray to repair failed icons, batch {b + 1} of {total}. "
                 f"Redraw each of these {len(chunk)} reference files in order."]
        lines += ['  ' + x for x in COMMON if x]
        lines.append('  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. '
                     'Fix all of the listed rules for that file, not just the first; a file passes only when none remain.')
        lines.append('  How to fix each rule that appears in this batch:')
        lines += [f'    - {TYPE[k]}' for k in rules]
        lines.append('  Files:')
        for n, i in enumerate(chunk, 1):
            violated = i['all'].split()
            lines.append(f"  {n}. {i['reference']}")
            lines.append(f"     icon_id: {i['icon_id']}")
            if i['current']: lines.append(f"     current drawing: {i['current'].split(';')[0]}")
            lines.append(f"     violates {len(violated)} rule{'s' if len(violated) > 1 else ''}: " + ', '.join(LABEL[k] for k in violated))
            for k in violated:
                errs = [e for e in i['errors'] if k in kinds([e])]
                more = f" (+{len(errs) - 3} more)" if len(errs) > 3 else ''
                lines.append(f"       - {LABEL[k]}: " + ' | '.join(short(e) for e in errs[:3]) + more)
        prompts.append((f"batch-{b + 1:02d}", '\n'.join(lines)))
    pdir = OUT / 'prompts'; pdir.mkdir(exist_ok=True)
    for old in pdir.glob('*.txt'): old.unlink()
    for name, text in prompts: (pdir / f'{name}.txt').write_text(text + '\n')
    (OUT / 'prompts.md').write_text('\n\n'.join(f'### {name}\n\n```\n{text}\n```' for name, text in prompts) + '\n')
    summary = {'total': len(items),
               'primary': {k: len(by[k]) for k in ORDER if by.get(k)},
               'any': {k: sum(k in i['all'].split() for i in items) for k in ORDER},
               'origin': dict(collections.Counter(i['origin'] for i in items)),
               'no_previous_run': sum(not i['previous_runs'] for i in items),
               'missing_reference': [i['reference'] for i in items if not i['reference_exists']],
               'batches': len(prompts)}
    (OUT / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))

main()
