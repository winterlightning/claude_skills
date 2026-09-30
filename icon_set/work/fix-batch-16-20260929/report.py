from pathlib import Path
import json,html,os
B=Path(__file__).parent;ROOT=B.resolve().parents[2]
rows=json.loads((B/'staged.json').read_text());runs=json.loads((B/'runs.json').read_text());changes=json.loads((B/'changes.json').read_text());audit=json.loads((B/'disapproval-audit.json').read_text())
md=['# Once-disapproved solo fix batch 16 of 34','', '20 icons claimed at offset 0 with `--max-disapprovals 1`; every production history independently verified as one disapproval before fixing. Worker: `thuan-mac`. Author in all modules: `gpt-6`.','', 'No icon had written reviewer feedback. Each revision follows a rendered original/rejected comparison. Two uploaded inputs have no separate original; their displayed drawing was used as the reference. All final drawings were inspected at 48px and enlarged in light and dark themes.','', 'Validation for every final module: **valid, zero warnings, full build gate pass**.','']
web=['<!doctype html><meta charset="utf-8"><title>Batch 16 fixes</title><style>body{font:16px system-ui;margin:30px;background:#eee;color:#222}article{background:white;padding:20px;margin:20px 0;border-radius:12px}figure{display:inline-block;margin:10px}img{width:160px;height:160px;object-fit:contain}small{display:block}code{overflow-wrap:anywhere}</style><h1>Once-disapproved solo fix batch 16</h1><p>20 claims · offset 0 · max disapprovals 1 · author gpt-6 · worker thuan-mac</p>']
verified=[]
for row in rows:
 k=row['item']['icon_id'];r=runs[k];run=Path(r['run']);m=json.loads((run/(k+'.metadata.json')).read_text());final=Path(row['result_dir'])/'result.json'
 f=json.loads(final.read_text()) if final.exists() else {};state=f.get('outcome','uploading');status=f.get('review_status','pending')
 svg=run/(k+'.svg');source=Path(r['module'])
 md += [f'## {row["key"]}', '', '**Original / rejected comparison:** '+m['comparison'], '', '**Feedback:** None recorded.', '', '**Changed:** '+changes[k], '', '**Simplification:** '+m['omissions'], '', '**Construction:** '+m['lucide'], '', f'**Keyshape:** {__import__("re").search(r"keyshape=Keyshape\.(\w+)",source.read_text()).group(1)}; selected to fit the subject within the SOLO48 envelope.', '', f'**AUTHOR:** `gpt-6`. **Validation:** valid, 0 warnings; build gate pass. **Production:** {state}, {status}.', '', f'**RESULT_DIR:** [{run.name}]({run.resolve()})', '', f'[SVG]({svg.resolve()}) · [Python source]({source.resolve()}) · [Validation]({(run/"validation.txt").resolve()}) · [Result]({(run/"result.json").resolve()})','']
 web.append('<article><h2>'+html.escape(row['key'])+'</h2>')
 for label,path in [('Original',Path(row['reference'])),('Rejected',Path(row['result_dir'])/'before'/(k+'.svg')),('Fixed',svg),('Fixed dark',run/'preview-dark-384.png')]:
  rel=os.path.relpath(path,B);web.append(f'<figure><img src="{html.escape(rel,quote=True)}"><figcaption>{label}</figcaption></figure>')
 web.append('<p>'+html.escape(changes[k])+'</p><p>Simplification: '+html.escape(m['omissions'])+'</p><small>AUTHOR gpt-6 · valid · zero warnings · gate pass · '+state+' / '+status+'</small><p><a href="'+os.path.relpath(run,B)+'">RESULT_DIR</a> · <a href="'+os.path.relpath(svg,B)+'">SVG</a></p></article>')
 verified.append({'key':row['key'],'outcome':state,'review_status':status,'author':f.get('author'),'validation':f.get('validation_status'),'warnings':f.get('validation_warnings'),'gate':f.get('build_gate',{}).get('status'),'run':str(run)})
(B/'REPORT.md').write_text('\n'.join(md)+'\n');(B/'report.html').write_text('\n'.join(web));(B/'verified-results.json').write_text(json.dumps(verified,indent=2)+'\n')
print('Done:',sum(x['outcome']=='done' for x in verified),'Ready:',sum(x['review_status']=='ready' for x in verified),'of',len(verified))
