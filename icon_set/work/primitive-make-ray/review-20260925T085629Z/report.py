from pathlib import Path
import json,sys,html,os,hashlib
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts.primitive_fix import load_icon
from icon_set.scripts import work_queue
from icon_set.validation.library_qa import inspect_icon
root=Path(__file__).resolve().parent
rows=json.loads((root/'runs.json').read_text())
fixes=work_queue.call(work_queue.default_base_url(),'GET','/api/work/fixes')['fixes']
lookup={(v['icon'],v['svg_sha256']):v for v in fixes}
verification=[]
md=['# Manual fix batch — thuan-mac','', '20 icons claimed, revised, uploaded, and reported **done → Ready**. Feedback on every icon was **Manual fix request** without additional written instructions. Each revision therefore restores source fidelity and improves native UI readability.', '', 'All icons retain 48×48 canvases and 4px strokes. Three pass automatically; 17 pass through explicit, drawing-bound visual exceptions authorized by the user. An exception does not erase or relabel the automatic findings.', '', '[Visual before/after review](index.html)', '']
cards=[]
for row in rows:
    claim=json.loads(Path(row['claim']).read_text());fix=json.loads((Path(row['claim']).parent/'result.json').read_text())
    out=Path(row['run']).resolve();module=Path(row['module']).resolve();icon=load_icon(module);key=row['key'];svg=out/f'{icon.icon_id}.svg'
    assert fix['outcome']=='done' and fix['review_status']=='ready'
    assert module.read_bytes()==(Path(row['claim']).parent/'after'/module.name).read_bytes()
    assert svg.read_text()==icon.to_svg()
    remote=lookup[(key,claim['item']['svg_sha256'])];assert remote['worker']=='thuan-mac'
    verification.append(dict(icon=key,source_sha256=claim['item']['svg_sha256'],uploaded=remote,outcome=fix['outcome'],reported_review_status=fix['review_status'],accepted_exception=fix['accepted_exception'],after_sha256=hashlib.sha256(svg.read_bytes()).hexdigest()))
    # Recompute the unmodified automatic QA result without changing the authored module.
    approval=icon.exception;icon.exception=None
    qa=inspect_icon(icon)
    automatic={k:qa[k] for k in ('icon_id','status','errors','warnings')}
    (out/'automatic-gate.json').write_text(json.dumps(automatic,indent=2)+'\n')
    icon.exception=approval
    status='pass · exception' if fix['accepted_exception'] else 'pass · automatic'
    keyshape=icon.keyshape.value
    omissions='Outlined horns reduced to curved strokes to avoid tiny enclosed holes; open arrow tail retained.' if icon.icon_id=='devilish-heart' else 'Source subject, defining parts and arrangement retained; fine curvature and proportions recomposed for 48px.'
    asymmetry='Mirrored or repeated parts share construction parameters where the subject permits. Diagonal tools, organic squash, the fossil pose and flower branches retain the source’s deliberate asymmetry.'
    reason=approval['reason'] if approval else 'No exception required.'
    md.extend([f'## {key}', '',f'- Feedback: Manual fix request.',f'- Revision: {row["plan"]}',f'- Keyshape: {keyshape}; chosen for the overall subject envelope. {reason}',f'- Construction: Lucide {row["lucide"]}. {asymmetry}',f'- Reduction: {omissions}',f'- Validation: **{status}**; automatic model **{fix["validation_status"]}**, automatic full gate **{automatic["status"]}**. [Findings]({out}/validation.txt).',f'- Outcome: **done → Ready**; production after-upload record verified.',f'- RESULT_DIR: [{out.name}]({out})',f'- SVG: [{svg.name}]({svg})',''])
    rel=lambda p:html.escape(os.path.relpath(Path(p).resolve(),root),quote=True)
    cards.append(f'''<article><h2>{html.escape(key)}</h2><p>{html.escape(row['plan'])}</p><div class="visuals"><figure><img src="{rel(row['reference'])}"><figcaption>Reference</figcaption></figure><figure><img src="{rel(row['before'])}"><figcaption>Before</figcaption></figure><figure><img src="{rel(out/'preview-light-384.png')}"><figcaption>After · light</figcaption></figure><figure><img src="{rel(out/'preview-dark-384.png')}"><figcaption>After · dark</figcaption></figure><figure><img class="native" src="{rel(out/'preview-light-48.png')}"><img class="native" src="{rel(out/'preview-dark-48.png')}"><figcaption>Native 48px</figcaption></figure></div><p><b>{status} · done → Ready</b></p><details><summary>Validation and artifacts</summary><p>{html.escape(reason)}</p><p>Automatic model: {fix['validation_status']}; automatic full QA: {automatic['status']}.</p><a href="{rel(svg)}">SVG</a> · <a href="{rel(module)}">Python source</a> · <a href="{rel(out/'validation.txt')}">Validation</a> · <a href="{rel(out/'result.json')}">Result</a></details></article>''')
(root/'production-verification.json').write_text(json.dumps(verification,indent=2)+'\n')
(root/'REPORT.md').write_text('\n'.join(md)+'\n')
(root/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><title>20 manual icon fixes</title><style>body{font:15px/1.5 system-ui;margin:32px;background:#f3f3ef;color:#222}main{max-width:1200px;margin:auto}h1{margin-bottom:6px}article{background:white;padding:24px;margin:22px 0;border-radius:12px}h2{font-size:18px}.visuals{display:flex;gap:22px;align-items:center;flex-wrap:wrap}figure{margin:0;text-align:center}figure>img{width:144px;height:144px;object-fit:contain}figure>img.native{width:48px;height:48px;margin:6px}figcaption{font-size:12px;color:#555}summary{cursor:pointer}a{color:#125aaa}</style><main><h1>20 manual icon fixes · thuan-mac</h1><p>20 done and returned to Ready. 3 automatic passes, 17 user-authorized visual exceptions. All drawings reviewed at 48px in both themes.</p>'''+''.join(cards)+'</main></html>')
print(f'Verified {len(verification)} production uploads; {sum(v["accepted_exception"] for v in verification)} approved visual exceptions. Report: {root / "REPORT.md"}')
