"""Standalone primitive-make-ray authoring runs for the batch's claimed references."""
import json
import sys
import re
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from icon_set.scripts.primitive_fix import load_icon, render_previews
from icon_set.scripts.build_gate import gate

AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None  # Each individual source ID is written to its own module.
SOURCE_PATH = None
BATCH = Path(__file__).parent

HELPERS = '''
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def path(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def contour(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
'''

def author(key, keyshape, body, findings, plan, references='Lucide hand and hand-fist: rounded fingertips, coherent palm contours. Shared human references inspected; detached-head spacing does not apply to hands.', attributes=''):
    item = next(i for i in json.loads((BATCH/'items.json').read_text()) if i['key']==key)
    ref = Path(item['reference'])
    match = re.search(r'([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$',ref.stem)
    uid = match.group(1)
    concept = ref.stem[:match.start()].rstrip('_')
    icon_id = key.split('/',1)[1]
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ-batch03')
    run = ROOT/'icon_set/work/primitive-make-ray'/uid/stamp
    run.mkdir(parents=True)
    meta = dict(concept=concept,source_uuid=uid,reference_path=str(ref),icon_id=icon_id,author=AUTHOR)
    (run/(icon_id+'.metadata.json')).write_text(json.dumps(meta,indent=2))
    (run/'review-before.txt').write_text(findings+'\nFeedback: no written reason or feedback was supplied. Repair follows the original reference.\n'+references+'\n')
    import cairosvg
    cairosvg.svg2png(url=str(ROOT/ref),write_to=str(run/'reference.png'),output_width=384,output_height=384,background_color='white')
    module = run/(icon_id.replace('-','_')+'_'+uid.replace('-','_')+'.py')
    module.write_text(f'''"""{concept}.\nSymbol plan: {plan}\n{references}\nDeliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uid!r}
SOURCE_PATH = {str(ref)!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {icon_id!r}
    keyshape = Keyshape.{keyshape}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = {tuple(icon_id.split('-'))!r}
    {attributes}
    def build(self):
'''+HELPERS+'\n'+body+'\n')
    icon=load_icon(module); report=icon.validate_icon()
    (run/'validation.txt').write_text(report.describe())
    (run/(icon_id+'.svg')).write_text(icon.to_svg())
    render_previews(icon.to_svg(),icon_id,48,run)
    result=gate(module)
    (run/'gate.json').write_text(json.dumps(result,indent=2))
    print(key, str(run.relative_to(ROOT)), report.describe(), json.dumps(result),flush=True)
    meta.update(result_dir=str(run.relative_to(ROOT)),module=module.name,svg=icon_id+'.svg',validation_status=report.status,validation_errors=report.errors,validation_warnings=report.warnings,build_gate=result,findings=findings,plan=plan,references=references)
    (run/'pending-result.json').write_text(json.dumps(meta,indent=2))
    return str(run.relative_to(ROOT))

if __name__=='__main__':
    configs=json.loads((BATCH/sys.argv[1]).read_text())
    results={}
    for c in configs:
        results[c['key']]=author(**c)
    (BATCH/(sys.argv[1]+'.runs.json')).write_text(json.dumps(results,indent=2))
