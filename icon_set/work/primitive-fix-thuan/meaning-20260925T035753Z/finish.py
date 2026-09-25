from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts import primitive_fix as fix,work_queue

root=Path(__file__).parent
rows=json.loads((root/'batch.json').read_text())
details={
 'browser-dollar-sign-right':{
  'references_used':'Supplied browser-dollar reference and rejected drawing; Lucide dollar-sign original and atomic-debug inspected for two tangent semicircular bowls. Browser construction uses a square frame with a separate toolbar.',
  'omissions':'Dollar moved beside the browser on its right to fit an unmistakable curved S and top/bottom vertical ticks; tiny toolbar controls omitted. Retain both the browser and dollar concepts.',
  'note':'Replaced the zigzag with a curved dollar S and explicit vertical ticks; placed it on the right of a square browser window so both concepts remain clear at 48px.'},
 'cartoon-cat-face':{
  'references_used':'Supplied cat reference and rejected drawing; Lucide cat original and atomic-debug inspected for paired pointed ears, broad rounded jaw and restrained facial marks.',
  'omissions':'Oversized eye outlines, pupils and separate smile omitted to make room for two clearly separated eyes, a small nose and paired whiskers. Features mirror across x24.',
  'note':'Added paired cheek whiskers and a small feline nose beneath two eyes; retained pointed ears and a broad round jaw so the face reads as a cat.'},
 'capped-carpenter-beside-a-hand-saw':{
  'references_used':'Supplied avatar-carpenter reference and rejected drawing. Shared human_ref/user.svg and full_body_ref.png inspected earlier in this session: round head/jaw vocabulary retained. No useful local Lucide saw match was found.',
  'omissions':'Tiny facial details omitted. The source contains a head without a torso, so no detached head-to-body gap applies. Saw retained beside the capped head, with three coarse teeth and a large handle opening.',
  'note':'Redrew the hand saw with three coarse blade teeth and a distinct open grip below the blade, beside a capped carpenter head.'}
}
for r in rows:
 out=Path(r['run']);receipt=Path(r['claim']).parent/'result.json'
 if receipt.exists():
  print('Already reported',r['icon_id'],flush=True);continue
 checks=json.loads((out/'checks.json').read_text());design=json.loads((out/'design.json').read_text());extra=details[r['icon_id']]
 assert checks['model']=='valid' and not checks['warnings'] and checks['gate']['status']=='pass'
 result=dict(source_uuid=r['source_uuid'],reference_path=r['reference_path'],concept=r['concept'],icon_id=r['icon_id'],author='gpt-6',
   validation_status='valid',validation_warnings=[],build_gate_status='pass',
   visual_review='Inspected the emitted SVG renders at native 48px and enlarged size in light and dark themes. Defining subject features, clear negative space and smooth rounded contours remain legible.',
   keyshape=design['keyshape'],design=design['plan'],artifacts=sorted(p.name for p in out.iterdir() if p.is_file()),outcome='done',**extra)
 (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 code=fix.finish(work_queue.default_base_url(),'thuan-mac','solo/'+r['icon_id'],'done',note=extra['note'],ray_run=out)
 print('FINISH',r['icon_id'],code,flush=True)
