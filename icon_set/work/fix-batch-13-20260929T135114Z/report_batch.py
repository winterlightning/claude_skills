from pathlib import Path
import html
import json
import os
import sys

B = Path(__file__).resolve().parent
ROOT = B.parents[2]
sys.path.insert(0, str(ROOT))
from icon_set.scripts import primitive_fix as f, work_queue as q

rows = json.loads((B / 'claims.json').read_text())
runs = json.loads((B / 'runs.json').read_text())
audit = []
sections = []
cards = []

def link(label, path):
    return f'[{label}](<{Path(path).resolve()}>)'

def image_tag(path, size):
    src = html.escape(os.path.relpath(path, B), quote=True)
    return f'<img src="{src}" width="{size}" height="{size}" alt="Icon comparison">'

for row in rows:
    key = row['key']
    k = key.split('/')[-1]
    v = runs[k]
    run = ROOT / v['run']
    fix = ROOT / row['fix_dir']
    m = v['metadata']
    result_path = fix / 'result.json'
    if not result_path.exists():
        history = json.loads((fix / 'finish-reconciliation.json').read_text())
        current = history['current']
        assert current['status'] == 'ready' and current['work']['state'] == 'done'
        icon = f.load_icon(ROOT / v['module'])
        validation = icon.validate_icon()
        gate = json.loads((run / 'gate.json').read_text())
        claim = json.loads((fix / 'claim.json').read_text())
        reconciled = dict(source_key=key, icon_id=k, svg_sha256=claim['item']['svg_sha256'],
                          worker='thuan-mac', outcome='done', make_ray_run=v['run'],
                          module=v['module'], author=m['author'], author_ok=True,
                          validation_status=validation.status, validation_errors=list(validation.errors),
                          validation_warnings=list(validation.warnings), build_gate=gate,
                          reported=current['work'], review_status=current['status'],
                          reconciliation='Finish response timed out. Production history confirms done and Ready; evidence in finish-reconciliation.json.')
        result_path.write_text(json.dumps(reconciled, indent=2) + '\n')
    result = json.loads(result_path.read_text())
    count = q.disapproval_count(json.loads((B / 'history' / f'{k}.json').read_text()))
    assert count == 1
    assert result['outcome'] == 'done' and result['review_status'] == 'ready'
    assert result['validation_status'] == 'valid'
    assert not result['validation_errors'] and not result['validation_warnings']
    assert result['build_gate']['status'] == 'pass'
    assert not result['build_gate']['errors'] and not result['build_gate']['warnings']
    assert result['author'] == 'gpt-6' and result['author_ok']
    assert (run / f'{k}.svg').read_bytes() == (fix / 'after' / f'{k}.svg').read_bytes()
    audit.append(dict(key=key, disapprovals_before_fix=count, outcome='done', review_status='ready',
                      validation='valid', warnings=0, build_gate='pass', author='gpt-6',
                      result_dir=v['run'], finish_result=str(result_path.relative_to(ROOT))))
    sections.append(f"## {key}\n\n{m['comparison']}\n\n"
                    f"**Feedback:** {m['feedback']} **Author:** `gpt-6`. "
                    "**Validation:** valid, zero warnings; build gate pass. **Production:** done; Ready.\n\n"
                    f"**Construction:** {m['lucide']}. **Reduction:** {m['omissions']}\n\n" +
                    ' · '.join([link('RESULT_DIR', run), link('SVG', run / f'{k}.svg'),
                                link('Reference', ROOT / row['reference']), link('Rejected SVG', ROOT / row['before'])]))
    images = []
    for label, stem in [('Original', 'reference'), ('Rejected', 'before'), ('Fixed light', 'preview-light'), ('Fixed dark', 'preview-dark')]:
        images.append(f'<figure><figcaption>{label}</figcaption>{image_tag(run / (stem + "-384.png"), 192)}'
                      f'<div class="native">{image_tag(run / (stem + "-48.png"), 48)}</div></figure>')
    cards.append(f'<article><h2>{html.escape(key)}</h2><div class="comparison">' + ''.join(images) + '</div>' +
                 f'<p>{html.escape(m["comparison"])}</p><p>Reductions: {html.escape(m["omissions"])}</p>' +
                 '<p>AUTHOR: gpt-6 · valid · zero warnings · build gate pass · Ready</p></article>')

assert len(audit) == 20
(B / 'completion-audit.json').write_text(json.dumps(dict(batch=13, requested=20, completed=20, items=audit), indent=2) + '\n')
(B / 'report.md').write_text('# Once-disapproved solo fix batch 13\n\n'
    'Completed: all 20 revisions uploaded and returned to Ready through primitive_fix.finish.\n\n'
    'Claim: 20 solo icons, offset 0, maximum disapprovals 1; worker `thuan-mac`. '
    'All 20 production histories confirmed a count of 1 before any after uploads. '
    'No written reviewer feedback was present. Corrections follow the original references and comparison with the rejected drawings.\n\n'
    'All final modules use `AUTHOR = "gpt-6"`. Each validates as valid with zero errors and warnings and passes the upload build gate. '
    'Light and dark previews were inspected at 48px and enlarged size.\n\n' + '\n\n'.join(sections) + '\n')
(B / 'review.html').write_text('<!doctype html><html><head><meta charset="utf-8"><title>Batch 13 icon fixes</title>'
    '<style>body{font:15px system-ui;margin:32px;background:#eee;color:#222}article{background:white;padding:24px;margin:24px 0;border-radius:12px}'
    'h2{font-size:18px}.comparison{display:flex;gap:20px;flex-wrap:wrap}figure{margin:0}figcaption{margin-bottom:8px}.native{padding:12px 0}</style>'
    '</head><body><h1>Batch 13 · 20 fixes</h1><p>Original, rejected, and fixed drawings at enlarged and native 48px sizes.</p>' + ''.join(cards) + '</body></html>')
print('Verified and documented 20/20 done, Ready, valid, zero warnings, gate pass, AUTHOR gpt-6.')
