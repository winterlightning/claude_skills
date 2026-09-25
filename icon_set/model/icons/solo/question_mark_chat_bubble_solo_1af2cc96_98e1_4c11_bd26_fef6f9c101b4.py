"""question mark in chat bubble. Revision of reviewer feedback: Bad stroke drawn.
Plan: Round speech bubble with a lower-left tail and enlarged clear question mark. Square6..42. Symmetric round main balloon; directional tail.
Construction reference: Lucide message-circle-question-mark: round balloon with a clear hook and detached dot.
Omissions: None
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1af2cc96-98e1-4c11-bd26-fef6f9c101b4'
SOURCE_PATH='pictographic-primitives/symbol/question mark in chat bubble_1af2cc96-98e1-4c11-bd26-fef6f9c101b4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'question-mark-chat-bubble-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('question', 'mark', 'in', 'chat', 'bubble')
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

        bez('upper-left',(6,24),((6,14),(14,6),(24,6)))
        bez('upper-right',(24,6),((34,6),(42,14),(42,24)))
        bez('lower-right',(42,24),((42,34),(34,42),(24,42)),((22,42),(20,42),(18,41)))
        line('tail-bottom',(18,41),(6,42))
        line('tail-left',(6,42),(10,34))
        bez('lower-left',(10,34),((7,31),(6,28),(6,24)))
        contour('bubble','upper-left','upper-right','lower-right','tail-bottom','tail-left','lower-left',closed=True)
        arc('question-top',(19,20),(29,20),5)
        bez('question-hook',(29,20),((29,23),(24,21),(24,23)))
        contour('question','question-top','question-hook')
        dot('question-dot',(24,32))

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
