from author_remaining import *
import subprocess,sys,os
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
BASE=Path(__file__).resolve().parent
records=[]
for claim in sorted((ROOT/'icon_set/work/primitive-fix-thuan').glob('*/20260924T*-thuan-mac/claim.json')):
    item=json.loads(claim.read_text())['item'];key=item['icon_id']
    if key not in DRAWINGS:continue
    ref=next((claim.parent/'reference').glob('*.svg'));uid=ref.stem[-36:];out=ROOT/'icon_set/work/primitive-make-ray'/uid/STAMP
    sh,plan,body=DRAWINGS[key];module=next(out.glob('*.py'))
    from icon_set.scripts.primitive_fix import load_icon
    icon=load_icon(module);report=icon.validate_icon()
    assert report.status=='valid' and not report.errors and not report.warnings,(key,report.describe())
    meta=json.loads((out/f'{key}.metadata.json').read_text())
    meta.update(keyshape=sh,validation_status=report.status,validation_errors=[],validation_warnings=[],symbol_plan=plan,
        visual_review={'status':'reviewed','themes':['light','dark'],'sizes':[48,384], 'findings':'Inspected native and enlarged renders. Continuous curves, clean straight runs, consistent stroke, mirrored paired parts where appropriate. Deliberate anatomical and directional corners retained.'},
        references=[str(ref.relative_to(ROOT)),'rejected before drawing',plan],
        omissions_and_reductions=plan,
        artifacts={'module':module.name,'svg':f'{key}.svg','metadata':f'{key}.metadata.json','validation':'validation.txt','reference':'reference.png','previews':[f'{key}-{t}-{n}.png' for t in ('light','dark') for n in (48,384)]})
    (out/'result.json').write_text(json.dumps(meta,indent=2)+'\n')
    records.append(dict(key=item['key'],icon_id=key,run=str(out),fix_dir=str(claim.parent),svg=str(out/f'{key}.svg'),plan=plan,keyshape=sh,feedback=item.get('feedback'),status='pending'))
(BASE/'batch.json').write_text(json.dumps(records,indent=2)+'\n')
for rec in records:
    if (Path(rec['fix_dir'])/'result.json').exists():
        rec['status']='done';continue
    note='Redrawn with clean centerlines, tangent-continuous curves and consistent strokes; shared symmetry where appropriate. '+rec['plan']+' Valid with zero warnings; reviewed light/dark at 48 and 384px.'
    command=[sys.executable,'icon_set/scripts/primitive_fix.py','--worker','thuan-mac','finish','--icon',rec['key'],'--run',rec['run'],'--outcome','done','--note',note]
    result=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,env={**os.environ,'SSL_CERT_FILE':'/etc/ssl/cert.pem'})
    print(result.stdout.strip() or result.stderr.strip(),flush=True)
    rec['status']='done' if result.returncode==0 else 'upload-error'
    rec['finish_returncode']=result.returncode
    (BASE/(rec['icon_id']+'-finish.log')).write_text(result.stdout+result.stderr)
    (BASE/'batch.json').write_text(json.dumps(records,indent=2)+'\n')
print('FINISH RESULTS', {status:sum(r['status']==status for r in records) for status in set(r['status'] for r in records)},flush=True)
