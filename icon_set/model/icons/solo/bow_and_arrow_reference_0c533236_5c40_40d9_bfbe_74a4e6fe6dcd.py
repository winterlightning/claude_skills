"""rama navami. Revision of reviewer feedback: Bad stroke drawn.
Plan: Diagonal recurved bow with a taut string and arrow. Shared arrow/string node24,24 and bow node30,18. Square6..42.
Construction reference: Lucide bow-arrow: diagonal string, arrow and a smoothly recurved bow.
Omissions: Closed feather vanes reduced to an open two-stroke fletching at 48px.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0c533236-5c40-40d9-bfbe-74a4e6fe6dcd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/rama navami_0c533236-5c40-40d9-bfbe-74a4e6fe6dcd.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'bow-and-arrow-reference'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('rama', 'navami')
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

        bez('bow-upper',(6,6),((14,12),(32,6),(30,18)))
        bez('bow-lower',(30,18),((28,30),(42,20),(42,42)))
        contour('bow','bow-upper','bow-lower')
        poly('string',(6,6),(24,24),(42,42))
        poly('shaft',(6,42),(24,24),(30,18),(42,6))
        poly('head',(30,6),(42,6),(42,18))
        poly('feather',(6,34),(6,42),(14,42))

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
