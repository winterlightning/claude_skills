"""Carousel horse under a triangular canopy, with a sloping horse neck and muzzle, curved rump and two extended legs. Shared canopy axis x=24; pole x=22. Bounds (8,4)-(40,44).
Keyshape VRECT_L; fresh revision for feedback: Bad stroke drawn.
Construction reference: No useful exact Lucide carousel match; source controls the horse posture.
Omissions: Eye, mane and extra leg outlines omitted to keep the small horse legible.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b951d0e4-79bf-546b-b5b2-2b4ef11ec445'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/amusement park merry go round toys_b951d0e4-79bf-546b-b5b2-2b4ef11ec445.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'carousel-horse-on-pole-beneath-triangular-canopy'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ()
    keywords = ('amusement', 'park', 'merry', 'go', 'round', 'toys')

    def build(self):
        self.add_polyline('canopy',(8,14),(24,4),(40,14),(22,14),closed=True)
        self.path('horse',(14,28),('L',(22,28)),('L',(26,28)),('L',(30,22)),('L',(34,22)),('L',(40,28)),('L',(36,30)),('L',(32,28)),('L',(30,36)),('L',(22,36)),('L',(14,36)),('A',(14,28),4,4,True),closed=True)
        self.add_polyline('rear-leg',(14,36),(8,44),(12,44))
        self.add_line('front-leg',(30,36),(36,44))
        self.path('tail',(14,28),('A',(8,24),6,4,True))
        self.add_line('pole-top',(22,14),(22,28))
        self.add_line('pole-bottom',(22,36),(22,44))
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
