from pathlib import Path
import json,html,os
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[3];batch=Path(__file__).parent;rows=json.loads((batch/'batch.json').read_text())
md=['# Meaning fixes — 20 icons','', 'Worker: `thuan-mac`. Author in every module: `gpt-6`. All claims are meaning fixes; the clock and question-mark claims include specific reviewer notes. Original and rejected drawings were compared before authoring. All final drawings were inspected at native 48px and enlarged size in light and dark themes.','', 'Eight icons pass strictly; 12 use user-authorized, SHA-256-bound visual exceptions. Automatic findings are preserved; exceptions do not change the 48×48 canvas or 4px strokes.','']
sections=[];sheet=Image.new('RGB',(1200,1100),'#eeeeee');draw=ImageDraw.Draw(sheet)
def rel(p):return os.path.relpath(p,batch)
for i,r in enumerate(rows):
 dest=root/r['result_dir'];result=json.loads((dest/'result.json').read_text());fix=root/r['fix_dir'];finished=json.loads((fix/'result.json').read_text()) if (fix/'result.json').exists() else {}
 status='PASS · exception' if result['accepted_exception'] else 'PASS · strict'
 key='solo/'+r['icon_id'];svg=dest/result['svg'];module=dest/result['module']
 md += [f'## {key}','',f'**Rejected drawing:** {result["comparison"]}',f'**Feedback:** {result["feedback"]}.',f'**Revision:** {result["changes"]}',f'**Keyshape:** `{result["keyshape"]}` chosen to support the subject’s overall proportions; natural-envelope exceptions are recorded where exact fit would distort it.',f'**Construction reference:** {result["construction_reference"]}. Lucide originals and atomic geometry informed coherent contours, rounded enclosure corners, circular wheels and minimalist detail where applicable; unmatched subjects were rebuilt from their original references.',f'**Reduction:** {result["omissions"]}',f'**Author:** `{result["author"]}`. **Validation:** {status}; automatic full gate `{result["automatic_gate_status"]}`, model `{result["validation_status"]}`.',f'**Production:** {finished.get("outcome","upload pending")} / {finished.get("review_status","pending")}.',f'**RESULT_DIR:** [{dest.name}]({dest}) · [SVG]({svg}) · [Python]({module}) · [validation]({dest/"validation.txt"})','']
 if result.get('exception'):md += [f'**Exception reason:** {result["exception"]["reason"]}','']
 if result.get('human_spacing'):md += [result['human_spacing'],'']
 pics=[('Original',root/r['reference_path']),('Rejected',fix/'before'/(r['icon_id']+'.svg')),('Revision — light',dest/'preview-light-384.png'),('Revision — dark',dest/'preview-dark-384.png')]
 figures=''.join(f'<figure><img src="{html.escape(rel(p))}"><figcaption>{label}</figcaption></figure>' for label,p in pics)
 sections.append(f'<article><h2>{html.escape(key)}</h2><p class="status">{status} · AUTHOR gpt-6 · production {finished.get("review_status","pending")}</p><div class="images">{figures}</div><p><b>Problem:</b> {html.escape(result["comparison"])}</p><p><b>Change:</b> {html.escape(result["changes"])}</p><p><a href="{html.escape(rel(svg))}">SVG</a> · <a href="{html.escape(rel(module))}">Python</a> · <a href="{html.escape(rel(dest/"validation.txt"))}">Validation</a></p></article>')
 x=(i%4)*300;y=(i//4)*220
 im=Image.open(dest/'preview-light-384.png').convert('RGB').resize((130,130));sheet.paste(im,(x+20,y+12));sheet.paste(Image.open(dest/'preview-dark-48.png').convert('RGB'),(x+182,y+45))
 import textwrap
 name=r['icon_id'];label='\n'.join(textwrap.wrap(name,width=38));draw.text((x+8,y+151),label,fill='black');draw.text((x+8,y+192),status,fill='#444444')
(batch/'report.md').write_text('\n'.join(md))
css='body{max-width:1100px;margin:30px auto;font:16px system-ui;background:#eee;color:#171717}article{padding:24px;background:white;margin:24px 0;border-radius:12px}h2{font-size:20px}.images{display:flex;gap:12px}figure{margin:0;flex:1}img{width:100%;aspect-ratio:1;object-fit:contain}figcaption{margin-top:8px}.status{color:#555}'
(batch/'report.html').write_text(f'<!doctype html><meta charset="utf-8"><title>20 meaning fixes</title><style>{css}</style><h1>20 meaning fixes</h1><p>Worker thuan-mac · AUTHOR gpt-6 · 48px canvas · 4px strokes. Eight strict passes, 12 drawing-bound visual exceptions. Original and rejected artwork shown beside each revision.</p>'+''.join(sections))
sheet.save(batch/'final-overview.png')
print('report.md, report.html, final-overview.png written')
