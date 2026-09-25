from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts import primitive_fix,work_queue
root=Path(__file__).resolve().parent
for row in json.loads((root/'runs.json').read_text()):
    claim=Path(row['claim']);run=claim.parent
    if (run/'result.json').exists():continue
    data=json.loads(claim.read_text());item=data['item']
    if (run/'before-upload-error.txt').exists():
        before=run/'before'
        try:
            work_queue.upload_result(work_queue.default_base_url(),'thuan-mac',row['key'],item['svg_sha256'],'before',next(before.glob('*.svg')),next(before.glob('*.py')),note='Original rejected drawing; retry successful before upload')
            (run/'before-upload-retried.txt').write_text('Uploaded successfully.\n')
        except Exception as e:print('Before retry failed',row['key'],str(e),flush=True)
    try:
        code=primitive_fix.finish(work_queue.default_base_url(),'thuan-mac',row['key'],'done',row['plan'],ray_run=row['run'])
        print('FINISH',row['key'],code,flush=True)
    except Exception as e:
        print('UPLOAD ERROR',row['key'],str(e),flush=True)
