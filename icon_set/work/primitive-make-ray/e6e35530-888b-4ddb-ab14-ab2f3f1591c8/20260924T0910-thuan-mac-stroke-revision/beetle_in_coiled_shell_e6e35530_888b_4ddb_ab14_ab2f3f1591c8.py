"""insect earth. Revision of reviewer feedback: Bad stroke drawn.
Plan: Coiled shell surrounds a reduced insect. Exact shell join30,40; centered head/body, one leg pair. x6..42,y6..42.
Construction reference: Lucide bug: round head and elongated abdomen; supplied source controls shell topology.
Omissions: Antennae and extra legs removed in second fit attempt; fidelity requires visual review.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e6e35530-888b-4ddb-ab14-ab2f3f1591c8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__beetle-in-coiled-shell/20260924T090615Z-thuan-mac/reference/insect earth_e6e35530-888b-4ddb-ab14-ab2f3f1591c8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'beetle-in-coiled-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference-revision'
    aliases = ()
    keywords = ('insect', 'earth')
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

        line('lip-top',(6,6),(12,6))
        line('lip-neck',(12,6),(12,16))
        bez('left',(12,16),((12,22),(6,24),(6,30)),((6,38),(14,42),(22,42)))
        bez('coil-base',(22,42),((25,42),(28,41),(30,40)))
        bez('coil-bottom',(30,40),((34,36),(34,34),(34,30)))
        line('coil-side',(34,30),(34,26))
        bez('coil-turn',(34,26),((34,21),(34,18),(32,16)))
        contour('spiral','lip-top','lip-neck','left','coil-base','coil-bottom','coil-side','coil-turn')
        bez('outer-top',(18,9),((20,8),(24,6),(28,6)),((36,6),(42,14),(42,24)))
        bez('outer-bottom',(42,24),((42,32),(36,37),(30,40)))
        contour('outer','outer-top','outer-bottom')
        oval('head',22,19,2)
        oval('body',22,27,3,6)
        line('left-leg',(19,27),(16,27))
        line('right-leg',(25,27),(26,27))

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
