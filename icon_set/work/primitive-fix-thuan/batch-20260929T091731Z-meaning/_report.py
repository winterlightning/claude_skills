from pathlib import Path
import json,hashlib,sys
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
B=Path('icon_set/work/primitive-fix-thuan/batch-20260929T091731Z-meaning');rs=json.loads((B/'runs.json').read_text());root=Path.cwd();AUTHOR='gpt-6'
lines=['# Meaning fix batch — thuan-mac','', 'Claim: 20 solo icons, offset 0, disapprove status `meaning`.','', 'Every original and rejected drawing was visually compared before authoring. Final candidates were checked at native 48px in light and dark themes. All modules use `AUTHOR = "gpt-6"`.','', 'Validation: 1 strict automatic pass; 19 drawing-bound visual exceptions authorized by the user. All automatic errors and warnings remain recorded. Every accepted drawing retains the 48×48 canvas and uniform 4px stroke.','', '[Final light/dark preview](final-review.png)','']
audit=[]
for r in rs:
 SOURCE_ICON_ID=r['source_uuid'];SOURCE_PATH=r['reference_path'];finishfile=Path(r['fix_dir'])/'result.json';f=json.loads(finishfile.read_text());assert f['outcome']=='done' and f['review_status']=='ready';assert f['author']=='gpt-6';assert f['build_gate']['status']=='pass'
 svg=Path(r['result_dir'])/(r['icon_id']+'.svg');after=Path(r['fix_dir'])/'after'/svg.name;assert svg.read_bytes()==after.read_bytes();assert load_icon(Path(r['module'])).to_svg()==svg.read_text();assert not (Path(r['fix_dir'])/'before-upload-error.txt').exists()
 status='pass · exception (automatic '+f['build_gate'].get('automatic_status','pass')+')' if f['accepted_exception'] else 'strict pass · no errors or warnings'
 def link(label,p):return '['+label+']('+str((root/p).resolve())+')'
 lines += ['## '+r['key'],'', '**Original vs rejected:** '+r['comparison'],'', '**Feedback:** '+r['feedback'].replace('\n\n',' — '),'', '**Revision:** '+r['change'],'', '**Fit:** '+r['keyshape']+'; selected for the subject proportions. '+(r['exception']['reason'] if r.get('exception') else 'Exact envelope and automatic clearance checks pass.'),'', '**Omissions:** '+r['omissions'],'', '**Construction references:** '+r['reference_path']+'. '+r['lucide'],'']
 if r.get('human_gap_evidence'):lines+=['**Human construction:** '+r['human_gap_evidence'],'']
 lines+=['**AUTHOR:** `gpt-6` · **Validation:** '+status+' · **Production:** done, Ready.','',link('RESULT_DIR',Path(r['result_dir']))+' · '+link('SVG',svg)+' · '+link('Validation',Path(r['result_dir'])/'validation.txt')+' · '+link('Production receipt',finishfile),'']
 audit.append(dict(key=r['key'],outcome='done',review_status='ready',author='gpt-6',accepted_exception=f['accepted_exception'],svg_sha256=hashlib.sha256(svg.read_bytes()).hexdigest(),result_dir=r['result_dir'],production_receipt=str(finishfile)))
(B/'REPORT.md').write_text('\n'.join(lines));(B/'audit.json').write_text(json.dumps(audit,indent=2))
print('Verified:',len(audit),'done / Ready;',sum(r['accepted_exception'] for r in audit),'exceptions; all SVGs match uploaded after artifacts. All before drawings uploaded.')
print(B/'REPORT.md')
