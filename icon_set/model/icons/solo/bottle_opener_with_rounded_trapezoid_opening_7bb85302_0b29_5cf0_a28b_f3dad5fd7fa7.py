"""Bottle opener with a rounded trapezoid aperture and a distinct rounded grip. Shared axis and paired radii; bounds (10,4)-(38,44).
Keyshape VRECT_M; fresh revision for feedback: Bad stroke drawn.
Construction reference: No useful local Lucide bottle opener; one paired arc system owns the head and grip.
Omissions: Handle shortened relative to source for aperture spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7bb85302-0b29-5cf0-a28b-f3dad5fd7fa7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/beer opener_7bb85302-0b29-5cf0-a28b-f3dad5fd7fa7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bottle-opener-with-rounded-trapezoid-opening'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('beer', 'opener')

    def build(self):
        self.path('outline',(10,18),('A',(38,18),14,14,True),('A',(30,30),8,12,True),('A',(28,34),2,4,False),('L',(28,40)),('A',(20,40),4,4,True),('L',(20,34)),('A',(18,30),2,4,False),('A',(10,18),8,12,True),closed=True)

        self.path('opening',(21,14),('L',(27,14)),('A',(29,16),2,2,True),('L',(28,20)),('A',(26,22),2,2,True),('L',(22,22)),('A',(20,20),2,2,True),('L',(19,16)),('A',(21,14),2,2,True),closed=True)
        self.add_line('grip-seam',(20,34),(28,34))
        self.contacts()

    def path(self, name, start, *commands, closed=False):
        members=[]
        here=start
        for j,command in enumerate(commands):
            kind,end,*args=command
            ident=f'{name}-{j}'
            if kind=='L': self.add_line(ident,here,end)
            else:
                rx,ry,sweep=args
                self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
            here=end;members.append(ident)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def contacts(self):
        # Split receiving straight runs at true attachment nodes. Declare only
        # actual endpoint contact; never connect separated shapes.
        from icon_set.model.primitives import Line
        from dataclasses import replace
        endpoints={p.start for p in self.primitives}|{p.end for p in self.primitives}
        replacement={};rebuilt=[]
        for p in self.primitives:
            if isinstance(p,Line) and p.start!=p.end:
                a,b=p.start,p.end;dx,dy=b.x-a.x,b.y-a.y
                cuts=[q for q in endpoints if q not in (a,b) and (q.x-a.x)*dy==(q.y-a.y)*dx and 0<(q.x-a.x)*dx+(q.y-a.y)*dy<dx*dx+dy*dy]
                if cuts:
                    nodes=[a]+sorted(cuts,key=lambda q:(q.x-a.x)*dx+(q.y-a.y)*dy)+[b]
                    ids=[]
                    for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                        ident=f'{p.element_id}-join-{j}';rebuilt.append(Line(ident,u,v));ids.append(ident)
                    replacement[p.element_id]=ids
                    continue
            rebuilt.append(p)
        self.primitives[:]=rebuilt
        self.contours[:]=[replace(c,members=tuple(k for m in c.members for k in replacement.get(m,[m]))) for c in self.contours]
        for j,a in enumerate(self.primitives):
            for b in self.primitives[j+1:]:
                if {a.start,a.end}&{b.start,b.end}:self.relate('connect',a.element_id,b.element_id)
