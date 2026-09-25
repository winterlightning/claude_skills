"""Save reviewed run manifests, then finish only the twenty claims in this batch."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts import primitive_fix,work_queue
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
BATCH=Path(__file__).parent
items=json.loads((BATCH/'items.json').read_text())
omissions={2:['Reduced the reference tick series to three evenly spaced ticks per row for 4px ink clearance.'],
           5:['Reduced two motion strokes to one; kept both falling snowballs and mountain snow contour.']}
for item in items:
    run=Path(item['run']);checks=json.loads((run/'checks.json').read_text())
    assert checks['gate']['status']=='pass',item['key']
    assert not checks['warnings'],item['key']
    if checks['validation']!='valid':assert item.get('exception'),item['key']
for i,item in enumerate(items):
    run=Path(item['run']);checks=json.loads((run/'checks.json').read_text())
    metadata=json.loads((run/(item['id']+'.metadata.json')).read_text())
    result=dict(metadata,icon_id=item['id'],author=AUTHOR,keyshape=item['keyshape'],
        validation_status=checks['validation'],build_gate_status=checks['gate']['status'],
        automatic_status=checks['gate'].get('automatic_status',checks['gate']['status']),
        exception=item.get('exception'),visual_review='Reviewed enlarged and at native 48px in light and dark. Contours are coherent, openings visible, and reference-defining features retained.',
        findings=item['plan'],omissions=omissions.get(i,[]),
        references=[item['reference']]+[
            ('icon_set/references/'+name.strip() if name.strip().startswith('human_ref/') else
             'icon_set/references/lucide/original/'+name.strip()+'.svg')
            for name in item['lucide'].split(';')],
        artifacts=[p.name for p in run.iterdir() if p.is_file() and p.name!='result.json'])
    (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    if '--save-only' in sys.argv:
        continue
    if (Path(item['fix'])/'superseded.json').exists():
        continue
    status = work_queue.call(work_queue.default_base_url(),'GET','/api/work',query={'icon':item['key']})
    claim = json.loads((Path(item['fix'])/'claim.json').read_text())
    if status['svg_sha256'] != claim['item']['svg_sha256']:
        note = 'Superseded during redraw: production now has a different, '+status['status']+' revision. Local revision retained; newer artwork untouched.'
        try:
            code = primitive_fix.finish(work_queue.default_base_url(),'thuan-mac',item['key'],'cannot-fix',note)
            print('Closed superseded claim:',item['key'],code,flush=True)
        except work_queue.ApiError as error:
            (Path(item['fix'])/'superseded.json').write_text(json.dumps({'current':status,'note':note,'finish_attempt':'cannot-fix','error':str(error),'http_status':error.status},indent=2))
            print('Superseded; finish rejected:',item['key'],str(error),flush=True)
        continue
    fix=Path(item['fix'])
    if (fix/'result.json').exists():
        print('Already finished:',item['key'],flush=True);continue
    latest=primitive_fix.latest_run(item['key'])
    assert latest.resolve()==fix.resolve(),f'Unexpected newer claim for {item["key"]}'
    note=item['plan']
    if item.get('exception'):note+=' User-authorized visual exception; automatic findings retained. '+item['exception']['reason']
    try:
        code=primitive_fix.finish(work_queue.default_base_url(),'thuan-mac',item['key'],'done',note,ray_run=run)
    except work_queue.ApiError as error:
        if error.status != 409:
            raise
        status = work_queue.call(work_queue.default_base_url(),'GET','/api/work',query={'icon':item['key']})
        if status['svg_sha256'] == claim['item']['svg_sha256']:
            raise
        note='Superseded during upload: production changed to a newer '+status['status']+' drawing; local revision preserved.'
        try:
            primitive_fix.finish(work_queue.default_base_url(),'thuan-mac',item['key'],'cannot-fix',note)
        except work_queue.ApiError as close_error:
            (fix/'superseded.json').write_text(json.dumps({'current':status,'note':note,'finish_attempt':'done and cannot-fix','error':str(close_error),'http_status':close_error.status},indent=2))
        print(note,item['key'],flush=True)
        continue
    assert code==0,(item['key'],code)
    print('Uploaded',i+1,'of',len(items),flush=True)
