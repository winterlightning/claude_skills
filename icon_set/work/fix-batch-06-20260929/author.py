import json,sys,textwrap
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
ROOT=Path(__file__).parent
HELPERS='''
        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                members.append(member);here=end
            self.add_contour(name,*members,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*pts): self.add_polyline(name,*pts)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r): path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
'''
def author(index,body,note,keyshape='SQUARE',lucide='No useful direct match'):
    rows=json.loads((ROOT/'claims.json').read_text());row=rows[index]
    ref=Path(row['reference']);uuid=ref.stem[-36:];concept=ref.stem[:-37]
    run=Path('icon_set/work/primitive-make-ray')/uuid/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'-batch06')
    run.mkdir(parents=True);icon_id=row['key'].split('/')[1]
    meta=dict(concept=concept,source_uuid=uuid,reference_path=str(ref),icon_id=icon_id,author='gpt-6',comparison=note,feedback='No written feedback',lucide=lucide)
    (run/f'{icon_id}.metadata.json').write_text(json.dumps(meta,indent=2))
    module=run/(icon_id.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
    module.write_text(f'"""{note}\nPlan: {lucide}. Keyshape {keyshape}; shared contour nodes and dimensions.\n"""\nfrom icon_set.model.icons.solo._base import Solo48\nfrom icon_set.model.keyshapes import Keyshape\nSOURCE_ICON_ID={uuid!r}\nSOURCE_PATH={str(ref)!r}\nAUTHOR="gpt-6"\nclass Drawing(Solo48):\n    icon_id={icon_id!r}\n    keyshape=Keyshape.{keyshape}\n    semantic_role="MAIN"\n    semantic_kind="noun"\n    category="primitives-generate"\n    def build(self):\n'+HELPERS+textwrap.indent(textwrap.dedent(body),'        '))
    icon=load_icon(module);report=icon.validate_icon();g=gate(module)
    (run/'validation.txt').write_text(report.describe()+'\n'+json.dumps(g,indent=2));(run/f'{icon_id}.svg').write_text(icon.to_svg())
    render_previews(icon.to_svg(),icon_id,48,run)
    row.update(run=str(run),module=str(module),note=note,status=report.status,gate=g)
    rows[index]=row;(ROOT/'claims.json').write_text(json.dumps(rows,indent=2))
    print(index,icon_id,report.describe(),g,run,flush=True)
    return row
if __name__=='__main__':
    exec((ROOT/'drawings.py').read_text())
