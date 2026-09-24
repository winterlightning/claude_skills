"""tools ar kit. Revision of reviewer feedback: Bad stroke drawn.
Plan: Broken isometric cube with central Y and outward corner directions; extremes 8,4,40,44. Symmetry about x24.
Construction reference: No useful exact Lucide match; geometric contours reconstructed from supplied reference.
Omissions: None; retains the six separated corner junctions and central Y.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e879424e-4424-5a55-9724-37f5338a9a78'
SOURCE_PATH = 'pictographic-primitives/technology/tools ar kit_e879424e-4424-5a55-9724-37f5338a9a78.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'ar-cube-axis-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('tools', 'ar', 'kit')
    def build(self):

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

        poly('top',(20,7),(24,4),(28,7))
        line('top-stem',(24,4),(24,12))
        poly('bottom',(20,41),(24,44),(28,41))
        line('bottom-stem',(24,36),(24,44))
        poly('center',(18,20),(24,24),(30,20))
        line('center-stem',(24,24),(24,28))
        for side in ['left','right']:
            def p(x,y):return (48-x,y) if side=='right' else (x,y)
            poly(side+'upper',p(12,14),p(8,16),p(8,20))
            line(side+'upper-in',p(8,16),p(10,18))
            poly(side+'lower',p(8,28),p(8,34),p(12,36))
            line(side+'lower-in',p(8,34),p(10,32))

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
