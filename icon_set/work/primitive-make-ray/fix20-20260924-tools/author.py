"""Standalone authoring support; each output records its own source identity."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
ITEMS = json.loads((Path(__file__).parent/'batch.json').read_text())
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = tuple(x['uuid'] for x in ITEMS)
SOURCE_PATH = tuple(x['reference'] for x in ITEMS)

HELPERS = '''
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        bez = self.add_bezier
        def arc(n,a,b,r,ry=None,sweep=True,large=False):
            self.add_arc(n,a,b,radius_x=r,radius_y=r if ry is None else ry,sweep=sweep,large_arc=large)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def oval(n,x,y,rx,ry=None):
            ry = rx if ry is None else ry
            pts=[(x,y-ry),(x+rx,y),(x,y+ry),(x-rx,y)]
            for j in range(4): arc(n+str(j),pts[j],pts[(j+1)%4],rx,ry)
            contour(n,*(n+str(j) for j in range(4)),closed=True)
        def box(n,l,t,r,b,rad=4):
            pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
            members=[]
            for j in range(8):
                a,bp=pts[j],pts[(j+1)%8]
                if a==bp: continue
                name=n+str(j);members.append(name)
                if j%2: arc(name,a,bp,rad)
                else: line(name,a,bp)
            contour(n,*members,closed=True)
'''

# Split actual straight attachments and declare only coincident endpoints.
CONTACTS = '''
        from icon_set.model.primitives import Line
        from dataclasses import replace
        ends={q for p in self.primitives for q in (p.start,p.end)}
        rebuilt=[]; replacements={}
        for p in self.primitives:
            if isinstance(p,Line) and p.start!=p.end:
                a,b=p.start,p.end;dx,dy=b.x-a.x,b.y-a.y
                cuts=[q for q in ends if q not in (a,b) and (q.x-a.x)*dy==(q.y-a.y)*dx and 0<(q.x-a.x)*dx+(q.y-a.y)*dy<dx*dx+dy*dy]
                if cuts:
                    nodes=[a]+sorted(cuts,key=lambda q:(q.x-a.x)*dx+(q.y-a.y)*dy)+[b]
                    ids=[]
                    for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                        n=p.element_id+'-joint-'+str(j);rebuilt.append(Line(n,u,v));ids.append(n)
                    replacements[p.element_id]=ids
                    continue
            rebuilt.append(p)
        self.primitives[:]=rebuilt
        self.contours[:]=[replace(c,members=tuple(k for m in c.members for k in replacements.get(m,[m]))) for c in self.contours]
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
'''

def author(i,keyshape,plan,body,reference='No useful exact Lucide match; geometric contours reconstructed from supplied reference.',omissions='None'):
    x=ITEMS[i]; out=Path(x['run']); name=x['id'].replace('-','_')+'_'+x['uuid'].replace('-','_')+'.py'
    source=f'''"""{x['concept']}. Revision of reviewer feedback: Bad stroke drawn.
Plan: {plan}
Construction reference: {reference}
Omissions: {omissions}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {x['uuid']!r}
SOURCE_PATH = {x['reference']!r}
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = {x['id']!r}
    keyshape = Keyshape.{keyshape}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference-revision'
    aliases = ()
    keywords = {tuple(x['concept'].split())!r}
    def build(self):
'''+HELPERS+body+CONTACTS
    (out/name).write_text(source)
    (out/'design.json').write_text(json.dumps(dict(keyshape=keyshape,plan=plan,construction_reference=reference,omissions=omissions),indent=2))

def check(indices):
    from icon_set.scripts.primitive_fix import load_icon,run_module,render_previews
    for i in indices:
        x=ITEMS[i];out=Path(x['run'])
        icon=load_icon(run_module(out));r=icon.validate_icon();s=icon.to_svg()
        (out/(x['id']+'.svg')).write_text(s)
        (out/'validation.txt').write_text(r.describe())
        render_previews(s,x['id'],48,out)
        print(i,x['id'],r.describe(),flush=True)

if __name__=='__main__': check([int(i) for i in sys.argv[1:]])
