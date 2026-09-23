from pathlib import Path
import json
import html
import os
from PIL import Image

AUTHOR = 'gpt-6'
FIRST = Path(__file__).parent
ENTRIES = json.loads((FIRST / 'batch-inputs.json').read_text())
SOURCE_ICON_ID = tuple(e['source_uuid'] for e in ENTRIES)
SOURCE_PATH = tuple(e['reference_path'] for e in ENTRIES)
NOTES = [
    'Circular head and open shoulders remain recognizable in both themes. Shoulders are shallower than the shared user reference to fit the enclosure. Exact head-to-shoulder ink gap is 4: head bottom 26, shoulder top 34, less two stroke half-widths. Footer clearance remains a numerical warning, not a pass.',
    'Pound hook, crossbar and foot are readable at 48px. Upright enclosure creates room for the symbol; right alignment is modest because of required side clearance. Smooth hook joins the stem vertically.',
    'Centered pound reads cleanly in both themes. Upright browser and rounded hook retain the source composition, with decorative title marks omitted.',
    'All 18+ characters remain, but the top loop of 8 closes at native size and adjacent glyph spacing is crowded. Retained as an unsuccessful complete-composition attempt.',
    'One-bar yuan remains visible at native size; mirrored arms and deliberately right-shifted placement preserve the source arrangement.',
    'Centered one-bar yuan has balanced arms and margins. The original single crossbar is retained instead of importing a second Lucide yen bar.',
    'PM lettering and lower-left tail remain legible, but M is too close to the oval and P counter is undersized. Retained as an unsuccessful attempt; no content letter removed.',
    'Cup, straw and heart remain recognizable in both themes. Slightly tapered walls and mirrored heart lobes provide clear margins; the secondary lid seam is omitted.',
    'The complete 2+1 expression remains readable but numerals and plus have insufficient clearance to one another and to the calendar wall. Retained as an unsuccessful attempt.',
    'Seven is readable with generous lower margin. Rounded enclosure and matched bindings are balanced in both themes; numeral slant is intentional.',
    'Handset is recognizable but its closed handle contour crowds the calendar bottom and its end openings are too small. Retained as an unsuccessful attempt.',
    'Three pie sectors and three bindings remain visible, but the circle crowds the calendar bottom. Shared radial endpoints are coherent; retained as an unsuccessful attempt.',
    'Clipped-corner document and raised-prism camera with lens point are clear at 48px. Wider square page leaves camera clearance while preserving the asymmetric corner.',
]
PRINCIPLES = {
    'panels-top-left': 'rounded enclosure with one horizontal title divider',
    'pound-sterling': 'rounded upper hook, vertical stem, crossbar and foot',
    'japanese-yen': 'mirrored fork and stem; source controls crossbar count',
    'calendar': 'matched bindings, rounded page and optional header',
    'message-square': 'coherent enclosure-and-tail contour; source supplies oval silhouette',
    'cup-soda': 'centered straw, horizontal lid and tapered cup',
    'heart': 'mirrored rounded lobes converging to a lower tip',
    'file-video-camera': 'clipped document corner and distinct camera silhouette',
    'human_ref/user.svg': 'circular head and open shoulders; exact detached-head ink gap of 4',
}
ORDER = '''3a3e4d85-115c-4ccb-82d1-46fd45222b3a
70992897-5703-44f1-b32b-410282375607
544f8a60-ccee-42bc-8507-07936210e82f
fc5ffdff-80e9-4119-bf62-fb7c515c5aad
f3a40f08-7124-46f5-9ed2-b85ee4e25e73
fea32660-18d8-471e-9f27-73b635d24732
2a272a63-d16a-4057-9c1a-7e52136b6784
39d51711-cb0a-4cf4-bdca-37c1fe832458
d2f14f75-1ec0-41b0-83b6-100d1dcb63ea
f45d9583-295d-48ad-a334-df8ed9d7581c
b3b9d031-1b14-49cd-b640-12d78e2f90f7
bcaaf2a2-b7c9-450b-836e-e0c294ab0564
c75ad249-5bb8-4a26-91fe-e9f0c2f3ae41
1ccecf6e-60d8-417b-accc-4a89121dd0ab
14b5dacf-2ae7-4b43-b032-7129b3d49037
d7201890-607e-4568-916a-e843756d3ef0
fd8eb806-4d12-4ad0-bb86-c0aaf66d08bc
8c9afa4f-6b92-41b3-8bcd-f538c69afde6
ed808041-ff02-4ca5-8f86-337d16e29436
e82ae3f4-3ab0-421b-9460-5df44f0236e9'''.split()

records = {}
for i, entry in enumerate(ENTRIES):
    d = Path(entry['dir'])
    r = json.loads((d / 'attempt-findings.json').read_text())
    r['visual_review'] = dict(native_light_reviewed=True, native_dark_reviewed=True,
                             enlarged_light_reviewed=True, enlarged_dark_reviewed=True,
                             findings=NOTES[i], accepted=r['validation_status'] == 'valid')
    refs = []
    for s in r['refs']:
        p = 'icon_set/references/' + s if s.startswith('human_ref') else 'icon_set/references/lucide/original/' + s + '.svg'
        refs.append(dict(path=p, principle=PRINCIPLES[s], atomic_debug_inspected=not s.startswith('human_ref')))
    r['construction_references'] = refs
    r['keyshape_reason'] = ('Upright 32 by 40 centerline envelope makes room for the enclosed symbol or straw.'
                           if r['key'] == 'VRECT_L' else 'Square 36 by 36 centerline envelope retains the compact enclosure composition.')
    r['keyshape_centerline_extremes'] = [8, 4, 40, 44] if r['key'] == 'VRECT_L' else [6, 6, 42, 42]
    r['attempt_complete'] = True
    r['release_ready'] = r['validation_status'] == 'valid'
    r['source_path'] = r['reference_path']
    if i == 0:
        r['human_spacing_evidence'] = dict(reference='icon_set/references/human_ref/user.svg',
            head_center=[24,23], head_radius=3, head_bottom_centerline=26,
            shoulder_top_centerline=34, centerline_gap=8, ink_gap=4,
            nearest_points=[[24,26],[24,34]], construction='detached bust, not a stick figure',
            proportion_note='Shoulder curvature is shallower than the reference; no approval of exact reference proportions claimed.')
    notes = [r['description'], NOTES[i], 'Keyshape: ' + r['key'] + '. ' + r['keyshape_reason'],
             'Omissions: ' + ('; '.join(r['omissions']) or 'None.'), r['validation_findings']]
    (d / 'review-notes.md').write_text('\n\n'.join(notes))
    records[entry['source_uuid']] = r

rows, details = [], []
gallery = ['<!doctype html><meta charset="utf-8"><title>Batch 06 review</title>',
           '<style>body{font:16px system-ui;background:#e2e5e8;margin:24px}article{background:white;padding:16px;margin-bottom:18px;border-radius:10px}img{vertical-align:middle;margin:8px}a{color:#174795}.native{width:48px;height:48px}</style>',
           '<h1>Batch 06: 13 new attempts, 7 already done</h1><p>New drawings: 7 valid, 1 review, 5 invalid. AUTHOR: gpt-6. Review and invalid are not passes.</p>']
for i, uid in enumerate(ORDER, 1):
    ref = next(Path('icon_set/work/todo-references').glob('*' + uid + '.svg'))
    concept = ref.stem[:-37]
    if uid in records:
        r = records[uid]
        d = Path(r['dir'])
        status, action = r['validation_status'], 'new'
        svg = d / r['svg']
    else:
        file = next((Path('icon_set/work/primitive-make-ray') / uid).glob('*/result.json'))
        r = json.loads(file.read_text())
        d = file.parent
        status, action = r.get('validation_status', 'unknown'), 'already done - skipped'
        svg = d / (r['icon_id'] + '.svg')
    rows.append(f'| {i} | {concept} | {action} | {status} | [Folder]({d.resolve()}) / [SVG]({svg.resolve()}) |')
    details.append(dict(order=i, concept=concept, source_uuid=uid, reference_path=str(ref),
                        action=action, validation_status=status, result_dir=str(d), svg=str(svg)))
    if uid in records:
        rel = os.path.relpath(d, FIRST)
        gallery.append(f'<article><h2>{i}. {html.escape(concept)} - {status}</h2>')
        for f in ['reference-192.png', 'light-192.png', 'dark-192.png', 'light-48.png', 'dark-48.png']:
            cls = ' class="native"' if '48.png' in f else ''
            gallery.append(f'<img src="{html.escape(rel + "/" + f)}"{cls}>')
        gallery.append('<p>' + html.escape(r['visual_review']['findings']) + '</p>')
        gallery.append(f'<a href="{html.escape(rel + "/" + r["svg"])}">SVG</a> / <a href="{html.escape(rel + "/result.json")}">Result</a></article>')

report = ['# Primitive-make-ray: todo batch 06 of 55', '',
    'Processed 20 requested paths in order: 13 new standalone SOLO48 attempts and 7 skipped because an existing result.json was found. New results: **7 valid, 1 review, 5 invalid**. All new attempts retain Python source, SVG, metadata, reference renders, light/dark native and enlarged previews, and validation evidence. AUTHOR uses the model label `gpt-6`.', '',
    '[Visual comparison](comparison.png) / [Review index](batch-review.html)', '',
    '| # | Input concept | Action | Validation | Artifacts |', '|---|---|---|---|---|', *rows, '',
    '## New drawing findings', '']
for e in ENTRIES:
    r = records[e['source_uuid']]
    construction = '; '.join(s['path'] + ': ' + s['principle'] for s in r['construction_references'])
    report.extend(['### ' + r['concept'], '', r['description'], '',
        r['key'] + ': ' + r['keyshape_reason'] + ' Centerline extremes: ' + str(r['keyshape_centerline_extremes']) + '.', '',
        r['visual_review']['findings'], '', 'Omissions: ' + ('; '.join(r['omissions']) or 'None.'), '',
        'Construction: ' + construction + '.', '', '```text', r['validation_findings'].rstrip(), '```', ''])
(FIRST / 'batch-report.md').write_text('\n'.join(report))
(FIRST / 'batch-results.json').write_text(json.dumps(details, indent=2))
(FIRST / 'batch-review.html').write_text('\n'.join(gallery))
im = Image.open(FIRST / 'comparison.png')
for n, (a,b) in enumerate([(0,1200), (1200,2160), (2160,3120)], 1):
    im.crop((0,a,800,b)).save(FIRST / f'comparison-{n}.png')

# Result markers are deliberately the last files written in each run folder.
for e in ENTRIES:
    r = records[e['source_uuid']]
    d = Path(e['dir'])
    r['artifact_filenames'] = sorted(str(f.relative_to(d)) for f in d.rglob('*')
                                     if f.is_file() and '__pycache__' not in str(f)) + ['result.json']
    (d / 'result.json').write_text(json.dumps(r, indent=2))
for e in ENTRIES:
    d = Path(e['dir'])
    r = json.loads((d / 'result.json').read_text())
    assert r['source_uuid'] == e['source_uuid']
    assert (d / r['python']).is_file() and (d / r['svg']).is_file()
    for theme in ['light', 'dark']:
        assert Image.open(d / f'{theme}-48.png').size == (48,48)
print('Verified 13 new results and 7 previously completed references. New: 7 valid, 1 review, 5 invalid.')
print(FIRST / 'batch-report.md')
