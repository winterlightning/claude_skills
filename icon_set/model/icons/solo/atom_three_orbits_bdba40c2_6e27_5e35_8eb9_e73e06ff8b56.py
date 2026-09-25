"""molecule. Revision of reviewer feedback: Bad stroke drawn.
Plan: Three tangent-continuous orbital loops with explicit shared intersection nodes; x8..40,y4..44. Mirrored tilted orbits and central nucleus.
Construction reference: Lucide atom: coherent smooth loops; third vertical orbit is retained from the supplied source.
Omissions: The molecule nucleus ring is reduced to a dot for clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bdba40c2-6e27-5e35-8eb9-e73e06ff8b56'
SOURCE_PATH = 'pictographic-primitives/science/molecule_bdba40c2-6e27-5e35-8eb9-e73e06ff8b56.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'atom-three-orbits'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('molecule',)
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

        bez('vertical-top',(15,19),((15,11),(18,4),(24,4)),((30,4),(33,11),(33,19)))
        line('vertical-right',(33,19),(33,29))
        bez('vertical-bottom',(33,29),((33,37),(30,44),(24,44)),((18,44),(15,37),(15,29)))
        line('vertical-left',(15,29),(15,19))
        contour('vertical','vertical-top','vertical-right','vertical-bottom','vertical-left',closed=True)
        for name,mirror in [('rising',False),('falling',True)]:
            def p(x,y):return (48-x,y) if mirror else (x,y)
            bez(name+'a',p(15,19),(p(18,17),p(21,15),p(24,14)))
            bez(name+'b',p(24,14),(p(33,11),p(40,8),p(40,16)))
            bez(name+'c',p(40,16),(p(40,20),p(36,27),p(33,29)))
            bez(name+'d',p(33,29),(p(30,31),p(27,33),p(24,34)))
            bez(name+'e',p(24,34),(p(15,37),p(8,40),p(8,32)))
            bez(name+'f',p(8,32),(p(8,28),p(12,21),p(15,19)))
            contour(name,*(name+k for k in 'abcdef'),closed=True)
        dot('nucleus',(24,24))

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
