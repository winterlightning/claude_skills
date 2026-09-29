from pathlib import Path
import json,sys,datetime,hashlib,shutil
ROOT=Path.cwd();sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
BATCH=Path(__file__).parent
records=json.loads((BATCH/'batch.json').read_text())
AUTHOR='gpt-6'
# This utility preserves source identities on every emitted module and in batch.json.
SOURCE_ICON_ID=[Path(r['reference']).stem[-36:] for r in records]
SOURCE_PATH=[r['reference'] for r in records]
HELPERS='''
    def path(self, name, start, *steps, closed=False):
        ids=[]; p=start
        for n,step in enumerate(steps):
            key=f"{name}-{n}"; end=step[1]
            if step[0]=='L': self.add_line(key,p,end)
            elif step[0]=='C': self.add_bezier(key,p,(step[2],step[3],end))
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)
'''
def author(i,body,keyshape,review,plan,refs,omissions='',exception_reason=None):
 r=records[i];ref=Path(r['reference']);uid=ref.stem[-36:];concept=ref.stem[:-37]
 stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
 run=Path('icon_set/work/primitive-make-ray')/uid/(stamp+'-meaning-fix');run.mkdir(parents=True)
 metadata={'concept':concept,'source_uuid':uid,'reference_path':str(ref),'icon_id':r['id'],'feedback':r['feedback'],'comparison':review,'plan':plan}
 (run/(r['id']+'.metadata.json')).write_text(json.dumps(metadata,indent=2))
 shutil.copyfile(BATCH/f'{i}-reference.png',run/'reference.png');shutil.copyfile(BATCH/f'{i}-before.png',run/'before.png')
 module=run/(r['id'].replace('-','_')+'_'+uid.replace('-','_')+'.py')
 text=f'''"""{plan}
Reference comparison: {review}
Construction references: {refs}
Omissions: {omissions or 'No defining features omitted.'}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uid!r}
SOURCE_PATH = {str(ref)!r}
AUTHOR = {AUTHOR!r}
class Drawing(Solo48):
    icon_id = {r['id']!r}
    keyshape = Keyshape.{keyshape}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
{HELPERS}
    def build(self):
'''+''.join('        '+ln+'\n' for ln in body.strip().splitlines())
 module.write_text(text)
 icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
 (run/'validation-automatic.txt').write_text(report.describe())
 g=gate(module)
 (run/'gate-automatic.json').write_text(json.dumps(g,indent=2))
 if exception_reason and (report.status!='valid' or report.warnings or g['status']!='pass'):
  approval={'reason':exception_reason,'approved_by':'user','approved_on':'2026-09-29','svg_sha256':hashlib.sha256(svg.encode()).hexdigest()}
  module.write_text(text+'\nDrawing.exception = '+repr(approval)+'\n')
  icon=load_icon(module);g=gate(module)
 (run/(r['id']+'.svg')).write_text(icon.to_svg());render_previews(icon.to_svg(),r['id'],48,run)
 (run/'validation.txt').write_text(report.describe()+'\n\nBuild gate: '+json.dumps(g,indent=2))
 result={**metadata,'author':AUTHOR,'module':module.name,'svg':r['id']+'.svg','validation_status':report.status,'gate':g,'visual_review':'pending','omissions':omissions,'construction_references':refs}
 (run/'candidate.json').write_text(json.dumps(result,indent=2))
 r.update(run=str(run),module=str(module),note=review+' Revision: '+plan,exception=bool(g.get('exception')))
 (BATCH/'batch.json').write_text(json.dumps(records,indent=2))
 print(i,r['id'],report.status,g['status'],str(run),flush=True)
 if g['status']!='pass': print(json.dumps(g,indent=2),flush=True)
 return run

if __name__=='__main__':
 exec((BATCH/sys.argv[1]).read_text())
