from pathlib import Path
import json,html,os
BATCH=Path(__file__).resolve().parent
ROOT=Path.cwd()
entries=json.loads((BATCH/'final.json').read_text());items=json.loads((BATCH/'items.json').read_text())
rows=[];cards=[]
for n,(e,item) in enumerate(zip(entries,items),1):
 result_path=ROOT/item['fix_dir']/'result.json';result=json.loads(result_path.read_text()) if result_path.exists() else {}
 status='done · Ready' if result.get('outcome')=='done' and result.get('review_status')=='ready' else str(result.get('review_status','upload pending'))
 run=(ROOT/e['run']).resolve();svg=(ROOT/e['svg']).resolve()
 rows.append(f'''### {n}. {item['key']}

- **Status:** {status}; AUTHOR = `gpt-6`; build gate **pass · exception**; automatic model **{e['validation_status']}**, automatic full gate **{e['build_gate']['automatic_status']}**.
- **Original versus rejected:** {e['comparison']}
- **Reviewer feedback:** {e['feedback'].strip()}
- **Changed:** {e['change']}
- **Keyshape:** {e['keyshape']}, selected for the complete subject; approved optical-envelope departures are recorded in validation.
- **Omitted:** {e['omissions']}
- **Exception:** {e['exception_reason']}
- **Visual review:** Original and rejected drawing compared before authoring; final inspected at native 48px and enlarged in light and dark. {e['construction_reference_note']} {e['human_review']} Intentional asymmetry follows the source pose or object angle; repeated parts share dimensions.
- **Artifacts:** [RESULT_DIR]({run}) · [SVG]({svg}) · [Python source]({(ROOT/e['module']).resolve()}) · [validation]({run/'validation.txt'}) · [production finish]({result_path})
''')
 rel=lambda p:html.escape(os.path.relpath(ROOT/p,BATCH),quote=True)
 esc=html.escape
 cards.append(f'''<article><h2>{n}. {esc(item['key'])}</h2><div class="images"><figure><img src="{rel(item['reference'])}"><figcaption>Original</figcaption></figure><figure><img src="{rel(item['before'])}"><figcaption>Rejected</figcaption></figure><figure><img src="{rel(e['run']+'/preview-light-384.png')}"><figcaption>Revised · light</figcaption></figure><figure class="dark"><img src="{rel(e['run']+'/preview-dark-384.png')}"><figcaption>Revised · dark</figcaption></figure><figure class="native"><img src="{rel(e['run']+'/preview-light-48.png')}"><img src="{rel(e['run']+'/preview-dark-48.png')}"><figcaption>48px</figcaption></figure></div><p><b>{esc(status)} · gpt-6 · pass with exception</b></p><p>{esc(e['comparison'])}</p><p>{esc(e['change'])}</p><p class="detail">Exception: {esc(e['exception_reason'])} Automatic model: {esc(e['validation_status'])}; full gate: {esc(e['build_gate']['automatic_status'])}.</p><p><a href="{rel(e['svg'])}">SVG</a> · <a href="{rel(e['module'])}">Python</a> · <a href="{rel(e['run']+'/validation.txt')}">Validation</a> · <a href="{rel(e['run']+'/result.json')}">Run record</a></p></article>''')
header='''# Meaning-disapproved icons — 20 revisions

Worker: `thuan-mac`. Requested: 20, offset 0, reason `meaning`. Author: `gpt-6`.

All revisions retain 48×48 canvases and uniform 4px strokes. All 20 use drawing-bound visual exceptions authorized by the user. These are **not strict automatic passes**: the full automatic gate reports fail for all 20; model validation reports invalid for all 20. Original findings remain in each validation report. Production `finish` revalidated and accepted the exceptions before reporting done.

No registered icon modules, published assets, profile constants or validation thresholds were changed. Earlier attempts and before/after evidence are retained. The initial request timed out after 15 production claims. Those exact live claims were recovered and five additional icons were claimed, for exactly 20. An older completed batch was mistakenly inspected during recovery; its new alternative drafts were not uploaded and its production results were not replaced.

[Visual comparison gallery](index.html)

'''
(BATCH/'REPORT.md').write_text(header+'\n'.join(rows))
(BATCH/'index.html').write_text('''<!doctype html><meta charset="utf-8"><title>20 icon meaning fixes</title><style>body{font:15px system-ui;margin:32px;background:#eee;color:#202020;max-width:1200px}h1{font-size:25px}h2{font-size:18px}article{background:white;padding:22px;margin:22px 0;border-radius:12px}.images{display:flex;align-items:center;gap:20px;flex-wrap:wrap}figure{margin:0;padding:8px;background:#fff}figure img{width:144px;height:144px;object-fit:contain}figcaption{font-size:12px;color:#666;text-align:center}.dark{background:#1c1c19}.dark figcaption{color:#ddd}.native img{width:48px;height:48px;margin:8px}.detail{color:#555}a{color:#265ac5}</style><h1>20 icon meaning fixes</h1><p>Original → rejected → revised. Worker thuan-mac; author gpt-6. Reviewed at native 48px in light and dark. All revisions use user-authorized drawing-bound exceptions; automatic findings are retained.</p>'''+''.join(cards))
print(BATCH/'REPORT.md');print(BATCH/'index.html')
