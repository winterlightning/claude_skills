"""insect. Revision of reviewer feedback: Bad stroke drawn.
Plan: Beetle with rounded thorax, abdomen seam, paired antennae and three pairs of legs. Shared exact leg nodes on abdomen; x8..40,y4..44.
Construction reference: Lucide bug: paired antennae, three legs per side and one central seam.
Omissions: None
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '82fb3003-56b5-5594-a35c-f4552fbc42d8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__beetle/20260924T090615Z-thuan-mac/reference/insect_82fb3003-56b5-5594-a35c-f4552fbc42d8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'beetle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference-revision'
    aliases = ()
    keywords = ('insect',)
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

        box('thorax',16,12,32,22,4)
        for n,mirror in [('left',False),('right',True)]:
            def p(x,y):return (48-x,y) if mirror else (x,y)
            bez(n+'shoulder',p(20,22),(p(17,22),p(14,22),p(14,24)))
            line(n+'side',p(14,24),p(14,34))
            arc(n+'lower',p(14,34),p(18,42),10,sweep=mirror)
            arc(n+'base',p(18,42),p(24,44),10,sweep=mirror)
            contour(n+'body',n+'shoulder',n+'side',n+'lower',n+'base')
            bez(n+'antenna',p(20,12),(p(17,10),p(17,4),p(20,4)))
            line(n+'leg-top',p(14,24),p(8,24))
            line(n+'leg-middle',p(14,34),p(8,34))
            line(n+'leg-bottom',p(18,42),p(8,44))
        line('seam',(24,22),(24,44))

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
