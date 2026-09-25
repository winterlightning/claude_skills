"""bulb. Revision of reviewer feedback: Bad stroke drawn.
Plan: Lightbulb with symmetric dome, tapered base and five rays. Square6..42. Continuous bulb silhouette; curved shoulder-to-base transitions.
Construction reference: Lucide lightbulb: circular dome with smooth narrowing shoulders and a clear base.
Omissions: None
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9c7b548b-f26b-4b87-8dac-75d503bfd7a8'
SOURCE_PATH = 'pictographic-primitives/work/bulb_9c7b548b-f26b-4b87-8dac-75d503bfd7a8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'bulb'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('bulb',)
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

        arc('dome',(15,26),(33,26),9)
        bez('right-shoulder',(33,26),((33,30),(30,30),(30,34)))
        line('right-base',(30,34),(30,38))
        arc('base-right',(30,38),(26,42),4)
        line('base',(26,42),(22,42))
        arc('base-left',(22,42),(18,38),4)
        line('left-base',(18,38),(18,34))
        bez('left-shoulder',(18,34),((18,30),(15,30),(15,26)))
        contour('bulb','dome','right-shoulder','right-base','base-right','base','base-left','left-base','left-shoulder',closed=True)
        line('divider',(18,34),(30,34))
        line('top-ray',(24,6),(24,8))
        line('left-ray',(6,26),(7,26))
        line('right-ray',(41,26),(42,26))
        line('upper-left-ray',(8,12),(10,14))
        line('upper-right-ray',(40,12),(38,14))

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
