"""Buffalo head with broad outward horns, tapered face and low curved muzzle. Shared axis x=24; extremes (4,8)-(44,40).
Keyshape HRECT_L; fresh revision for feedback: Bad stroke drawn.
Construction reference: No useful local Lucide subject match; supplied original defines the silhouette.
Omissions: Tiny eyes and ear outlines omitted to retain horn and muzzle spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dfa6681e-c282-4464-9e3f-8da4256d4f83'
SOURCE_PATH = 'pictographic-primitives/animals/buffalo_dfa6681e-c282-4464-9e3f-8da4256d4f83.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'buffalo-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('buffalo',)

    def build(self):
        self.path('horns',(4,8),('A',(12,16),8,8,False),('A',(24,16),6,4,True),('A',(36,16),6,4,True),('A',(44,8),8,8,False),('A',(36,24),8,16,True),('L',(30,24)),('L',(24,20)),('L',(18,24)),('L',(12,24)),('A',(4,8),8,16,True),closed=True)
        self.path('face',(12,24),('L',(16,36)),('A',(24,40),8,4,False),('A',(32,36),8,4,False),('L',(36,24)))
        self.add_dot('muzzle',(24,31))
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
