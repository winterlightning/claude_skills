from pathlib import Path
import json,re,textwrap,sys,datetime
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts import build_gate
B=Path(__file__).parent
# Input identity is assigned per reference; every emitted module retains exact source identity.
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
HELPERS='''
        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
'''
D={}
def add(key,shape,issue,ref,code,omissions='None'):
 D[key]=dict(shape=shape,issue=issue,lucide=ref,code=textwrap.dedent(code),omissions=omissions)

def generate(keys=None):
 rows=json.loads((B/'claims.json').read_text());index=json.loads((B/'runs.json').read_text()) if (B/'runs.json').exists() else {}
 for row in rows:
  key=row['key'].split('/')[-1]
  if key not in D or keys and key not in keys:continue
  d=D[key];ref=Path(row['reference']);uuid=re.search(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}$',ref.stem).group()
  run=Path('icon_set/work/primitive-make-ray')/uuid/('20260929-batch12-'+datetime.datetime.now().strftime('%H%M%S%f'));run.mkdir(parents=True)
  meta={'concept':ref.stem[:-37],'source_uuid':uuid,'reference_path':str(ref),'author':AUTHOR,'icon_id':key,'comparison':d['issue'],'feedback':row['feedback'] or 'No written feedback; correct fidelity against original.','lucide':d['lucide'],'omissions':d['omissions']}
  (run/(key+'.metadata.json')).write_text(json.dumps(meta,indent=2))
  (run/'review-before.txt').write_text(d['issue']+'\n'+meta['feedback'])
  mod=run/(key.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
  code=f'"""{d["issue"]}\nPlan: {d["shape"]} exact SOLO48 bounds; coherent contours and shared repeats.\nConstruction reference: {d["lucide"]}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={uuid!r}\nSOURCE_PATH={str(ref)!r}\nAUTHOR={AUTHOR!r}\nclass Drawing(Solo48):\n    icon_id={key!r}\n    keyshape=Keyshape.{d["shape"]}\n    semantic_role="MAIN"\n    semantic_kind="noun"\n    category="primitives-generate"\n    aliases=()\n    keywords={tuple(key.split("-"))!r}\n    def build(self):\n'+HELPERS+textwrap.indent(d['code'],'        ')
  mod.write_text(code);icon=load_icon(mod);r=icon.validate_icon();(run/'validation.txt').write_text(r.describe());(run/(key+'.svg')).write_text(icon.to_svg());render_previews(icon.to_svg(),key,48,run)
  g=build_gate.gate(mod);(run/'gate.json').write_text(json.dumps(g,indent=2));print(key,r.status,g['status'],r.errors,r.warnings,g['errors'],g['warnings'],flush=True)
  index[key]={'run':str(run),'module':str(mod),'metadata':meta,'valid':r.status=='valid' and not r.warnings and g['status']=='pass'}
  (B/'runs.json').write_text(json.dumps(index,indent=2))
if __name__=='__main__':generate(sys.argv[1:])
