from pathlib import Path
import json,html
root=Path(__file__).parent.resolve();rows=json.loads((root/'batch.json').read_text())
records=[]
for m in rows:
    rd=Path(m['result_dir']).resolve();claim=Path(m['claim_dir']).resolve()
    result=json.loads((rd/'result.json').read_text());finish=json.loads((claim/'result.json').read_text())
    assert finish['outcome']=='done' and finish['review_status']=='ready'
    assert finish['author']=='gpt-6' and finish['build_gate']['status']=='pass'
    records.append((m,rd,claim,result,finish))
exceptions=sum(r[4]['accepted_exception'] for r in records)
lines=['# Primitive fix report — 20 icons', '',f'Worker: `thuan-mac`. All 20 claimed icons uploaded through `primitive_fix.py finish` and returned to **Ready**. Author: `gpt-6` on every module. {20-exceptions} strict automatic pass; {exceptions} accepted drawing-bound visual exceptions.', '', 'Exceptions preserve the automatic findings and are bound to the exact SVG SHA-256. They use the user’s explicit delegation: “If you think an icon needs to be exceptional, make it an exception, but make sure the icon quality is still good for UI/UX.” All icons retain SOLO48, uniform 4px strokes and fit inside the canvas. Every reference and rejected drawing was compared before authoring; each final drawing was inspected at native 48px in light and dark themes.', '', '[Native-size review sheet](native-final.png) · [Visual before/after report](review.html)', '', '| Icon key | Validation | Result directory | SVG |','|---|---|---|---|']
for m,rd,claim,r,f in records:
    label='Pass · exception' if f['accepted_exception'] else 'Strict pass'
    lines.append(f'| `{m["key"]}` | {label} | [Run](<{rd}>) | [SVG](<{rd / r["svg"]}>) |')
for m,rd,claim,r,f in records:
    g=f['build_gate'];lines.extend(['',f'## {m["key"]}','','**Reference/current comparison and repair:** '+m['comparison'],'','**Reviewer feedback:** '+m['feedback'].replace('\n',' '),'',f'**AUTHOR:** `gpt-6`. **Keyshape:** `{m["keyshape"]}`. **Construction:** local Lucide `{m["lucide"]}` original and atomic-debug; coherent contours, repeated dimensions and shared junctions. The source controls direction and intentional asymmetry.','', '**Omissions:** '+(' '.join(r['omissions']) or 'No identifying feature omitted.'),'',f'**Validation:** model `{r["validation_status"]}`; final gate `{g["status"]}`; '+('accepted exception; automatic gate `'+g['automatic_status']+'` retained.' if f['accepted_exception'] else 'zero errors and warnings.'),'',f'**Production:** `{f["outcome"]}` → `{f["review_status"]}`.', '',f'[Result directory](<{rd}>) · [SVG](<{rd / r["svg"]}>) · [Python](<{Path(m["module"]).resolve()}>) · [Validation](<{rd / "validation.txt"}>) · [Production receipt](<{claim / "result.json"}>)'])
    if f['accepted_exception']:lines.extend(['','**Exception reason:** '+g['exception']['reason']])
(root/'REPORT.md').write_text('\n'.join(lines)+'\n')
parts=['<!doctype html><html><meta charset="utf-8"><title>20 icon fixes</title><style>body{font:15px system-ui;margin:32px;background:#eee;color:#222}article{background:white;padding:24px;margin:20px 0;border-radius:12px}h2{font-size:18px}.images{display:flex;gap:24px;align-items:start}figure{margin:0;text-align:center}img{width:144px;height:144px}figcaption{margin:6px}.native img{width:48px;height:48px}p{max-width:1100px;line-height:1.5}a{color:#1460a0}.status{font-weight:bold}</style><h1>20 repaired icons · Ready</h1>',f'<p>Worker thuan-mac · AUTHOR gpt-6 · {20-exceptions} strict pass · {exceptions} drawing-specific exceptions. Automatic findings remain in each validation report.</p>']
for m,rd,claim,r,f in records:
    e=html.escape;parts.extend([f'<article><h2>{e(m["key"])}</h2><p>{e(m["comparison"])}</p><div class="images">'])
    for name,label in [('reference.png','Original reference'),('before.png','Rejected drawing'),('preview-light-384.png','Revision · light'),('preview-dark-384.png','Revision · dark')]:parts.append(f'<figure><img src="{rd/name}"><figcaption>{label}</figcaption></figure>')
    for theme in ('light','dark'):parts.append(f'<figure class="native"><img src="{rd / ("preview-"+theme+"-48.png")}"><figcaption>48 px</figcaption></figure>')
    parts.append('</div><p class="status">Ready · '+('Pass with exception' if f['accepted_exception'] else 'Strict pass')+'</p>')
    if f['accepted_exception']:parts.append('<p>'+e(f['build_gate']['exception']['reason'])+'</p>')
    parts.append(f'<p><a href="{rd / r["svg"]}">SVG</a> · <a href="{Path(m["module"]).resolve()}">Python</a> · <a href="{rd / "validation.txt"}">Validation</a> · <a href="{claim / "result.json"}">Production receipt</a></p></article>')
parts.append('</html>');(root/'review.html').write_text(''.join(parts))
print(f'Verified {len(records)} done/ready; {exceptions} accepted exceptions. Report: {root / "REPORT.md"}')
