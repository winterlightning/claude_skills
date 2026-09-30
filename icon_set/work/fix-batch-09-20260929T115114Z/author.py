from pathlib import Path
import sys,json,textwrap,datetime
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
sys.path.insert(0,str(REPO))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
ROWS=json.loads((ROOT/'batch.json').read_text())
HELPERS='''
        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
'''
def make(num,keyshape,notes,body,reference='No useful exact Lucide match; original reference and geometric curves.',extra=''):
 if len(sys.argv)>1 and str(num) not in sys.argv[1:]: return
 r=ROWS[num-1]; parent=REPO/'icon_set/work/primitive-make-ray'/r['uuid']; stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
 out=parent/f'{stamp}-batch09';out.mkdir(parents=True)
 meta={**r,'reference_path':r['reference'],'source_uuid':r['uuid'],'author':'gpt-6','keyshape':keyshape,'comparison':notes,'feedback':'No written feedback recorded.','construction_reference':reference,'result_dir':str(out.relative_to(REPO))}
 (out/f"{r['icon_id']}.metadata.json").write_text(json.dumps(meta,indent=2))
 module=out/(r['icon_id'].replace('-','_')+'_'+r['uuid'].replace('-','_')+'.py')
 source=f'''"""{notes}
Symbol plan: {reference}
Keyshape {keyshape}: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {r['uuid']!r}
SOURCE_PATH = {r['reference']!r}
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = {r['icon_id']!r}
    keyshape = Keyshape.{keyshape}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = {tuple(r['icon_id'].split('-'))!r}
{extra}
    def build(self):
'''+HELPERS+textwrap.indent(textwrap.dedent(body),'        ')
 module.write_text(source)
 icon=load_icon(module);report=icon.validate_icon(); g=gate(module)
 svg=icon.to_svg();(out/(r['icon_id']+'.svg')).write_text(svg)
 render_previews(svg,r['icon_id'],48,out)
 (out/'validation.txt').write_text(report.describe()+'\n'+json.dumps(g,indent=2))
 meta.update(module=module.name,svg=r['icon_id']+'.svg',validation_status=report.status,build_gate=g,errors=report.errors,warnings=report.warnings)
 (out/'candidate.json').write_text(json.dumps(meta,indent=2))
 (ROOT/f'latest-{num}.json').write_text(json.dumps(meta,indent=2))
 print(num,r['icon_id'],report.status,g['status'],str(out.relative_to(REPO)),flush=True)
 for e in list(report.errors)+list(report.warnings)+g['errors']+g['warnings']:print('  ',e,flush=True)
 return out
