"""chick. Revision of reviewer feedback: Bad stroke drawn.
Plan: Chick facing left, crest, beak, rounded body, raised tail, wing and two feet. Square 6,6,42,42. Natural directional asymmetry.
Construction reference: No useful exact Lucide match; geometric contours reconstructed from supplied reference.
Omissions: None in initial attempt; preserve complete chick features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3f1a2fcc-b8bd-5d0d-8a3f-ff4bd2741fbf'
SOURCE_PATH = 'pictographic-primitives/animals/chick_3f1a2fcc-b8bd-5d0d-8a3f-ff4bd2741fbf.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'baby-chick'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('chick',)
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

        bez('head-left',(12,20),((12,15),(15,11),(19,10)))
        line('crest-1',(19,10),(23,6))
        line('crest-2',(23,6),(26,10))
        bez('head-right',(26,10),((31,11),(32,17),(33,21)))
        bez('back',(33,21),((35,27),(39,24),(42,21)))
        bez('body',(42,21),((42,31),(36,36),(30,36)),((26,36),(22,36),(18,36)),((12,34),(10,27),(12,20)))
        contour('bird','head-left','crest-1','crest-2','head-right','back','body',closed=True)
        poly('beak',(12,20),(6,22),(12,26))
        dot('eye',(21,18))
        bez('wing',(20,26),((20,28),(24,28),(26,26)))
        poly('left-foot',(18,36),(16,42),(12,42))
        line('left-toe',(16,42),(20,42))
        poly('right-foot',(30,36),(32,42),(36,42))
        line('right-toe',(32,42),(28,42))

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
