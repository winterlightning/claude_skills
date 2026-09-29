import json,hashlib,html,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
BATCH=Path(__file__).resolve().parent
rows=json.loads((BATCH/'batch.json').read_text())
md=['# Meaning fixes — 20 icons','', 'Worker: `thuan-mac`. Author: `gpt-6` (introduced as the model-only author for this batch).', '',
 'All twenty claimed icons were compared against their original reference and rejected drawing, redrawn in fresh primitive-make-ray runs, visually checked at 48 px in light and dark, and uploaded with `primitive_fix.py finish --outcome done`. Production returned each to Ready.', '',
 'Validation: **1 automatic pass; 19 accepted drawing-specific exceptions** under the user’s explicit instruction. Exceptions preserve the actual automatic errors and warnings, and are tied to the SHA-256 of the exact 48×48 SVG with 4 px strokes. No validation constants were changed.', '',
 '[Visual comparison gallery](review.html)', '']
cards=[];summary=[]
for n,row in enumerate(rows,1):
 out=ROOT/row['result_dir'];fix=ROOT/row['fix_dir'];result=json.loads((out/'result.json').read_text());done=json.loads((fix/'result.json').read_text())
 assert done['outcome']=='done' and done['author']=='gpt-6' and done['build_gate']['status']=='pass'
 svg=out/result['svg'];after=fix/'after'/result['svg']
 assert svg.read_bytes()==after.read_bytes()
 if result['exception']:assert hashlib.sha256(svg.read_bytes()).hexdigest()==result['exception']['svg_sha256']
 status='pass · exception (automatic '+result['automatic_status']+')' if result['exception'] else 'pass · automatic, valid, zero warnings'
 link=lambda p:os.path.relpath(p,BATCH)
 md.extend([f'## {n}. {row["key"]}', '',f'**Comparison and repair:** {row["comparison"]}', '', f'**Reviewer feedback:** {row["feedback"]}', '',f'**Final construction:** {row["plan"]}', '',f'**Keyshape:** `{result["keyshape"]}`. {result["keyshape_rationale"]}', '', f'**Simplifications:** {result["omissions"]}', '',f'**Construction reference:** {result["lucide_reference"]}', '',f'**Author:** `gpt-6`. **Validation:** {status}. **Production:** `{done.get("review_status")}`; outcome `done`.', ''])
 if result.get('human_spacing_evidence'):md.extend([f'**Human construction:** `{result["human_reference"]}`. {result["human_spacing_evidence"]}', ''])
 if result['exception']:md.extend([f'**Exception:** {result["exception"]["reason"]}', ''])
 md.extend([f'**RESULT_DIR:** [{out.name}]({link(out)})', '',f'[SVG]({link(svg)}) · [Python]({link(out/result["module"])}) · [Validation]({link(out/"validation.txt")}) · [Result]({link(out/"result.json")}) · [Production finish receipt]({link(fix/"result.json")})', ''])
 cells=[]
 for label,path in [('Reference',ROOT/row['reference']),('Rejected',ROOT/row['before']),('Fixed',svg)]:
  cells.append(f'<figure><figcaption>{label}</figcaption><img class="large" src="{html.escape(link(path))}"><img class="native" src="{html.escape(link(path))}"></figure>')
 for theme in ['light','dark']:
  cells.append(f'<figure class="{theme}"><figcaption>48 px · {theme}</figcaption><img class="native" src="{html.escape(link(out/f"preview-{theme}-48.png"))}"></figure>')
 cards.append(f'<article><h2>{n}. {html.escape(row["icon_id"])}</h2><div class="images">'+''.join(cells)+f'</div><p>{html.escape(row["comparison"])}</p><p class="status">{html.escape(status)} · AUTHOR gpt-6 · Ready</p><a href="{html.escape(link(svg))}">SVG</a> · <a href="{html.escape(link(out/"validation.txt"))}">Validation</a></article>')
 summary.append({'key':row['key'],'status':done['review_status'],'outcome':done['outcome'],'author':done['author'],'exception':bool(result['exception']),'result_dir':row['result_dir'],'svg':str(svg.relative_to(ROOT))})
(BATCH/'REPORT.md').write_text('\n'.join(md))
(BATCH/'completion.json').write_text(json.dumps({'count':len(summary),'worker':'thuan-mac','author':'gpt-6','automatic_passes':sum(not s['exception'] for s in summary),'exceptions':sum(s['exception'] for s in summary),'icons':summary},indent=2)+'\n')
(BATCH/'review.html').write_text('<!doctype html><html><head><meta charset="utf-8"><title>20 meaning fixes</title><style>body{font:16px system-ui;margin:32px;background:#f0f0ee;color:#171715}h1{margin-bottom:8px}h2{font-size:19px}article{background:white;padding:24px;margin:24px 0;border-radius:12px}.images{display:flex;gap:16px;flex-wrap:wrap}figure{margin:0;padding:12px;min-width:100px;background:#fafafa;border:1px solid #ddd;border-radius:8px}figcaption{margin-bottom:12px;font-size:13px}.large{width:144px;height:144px;display:block}.native{width:48px;height:48px;display:block;margin-top:10px}.dark{background:#1c1c19;color:#f5f4ef}.status{font-size:14px;color:#556}p{max-width:1000px;line-height:1.5}a{color:#145da0}</style></head><body><h1>20 meaning fixes · Ready</h1><p>thuan-mac · gpt-6 · 1 automatic pass, 19 drawing-specific exceptions. Original, rejected and fixed artwork shown together. All automatic findings are retained.</p>'+''.join(cards)+'</body></html>')
print('Verified twenty production finish receipts and identical uploaded/local SVGs. Report:',BATCH/'REPORT.md')
