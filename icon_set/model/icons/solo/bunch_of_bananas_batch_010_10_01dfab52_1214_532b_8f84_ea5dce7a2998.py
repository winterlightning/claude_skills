"""Bunch of bananas with a common short stem and two nested sweeping fruit contours. Extremes (6,6)-(42,42); asymmetric fruit bend follows source.
Keyshape SQUARE; fresh revision for feedback: Bad stroke drawn.
Construction reference: Lucide banana: coherent outer belly and nested curved fruit, rebalanced as a bunch.
Omissions: Third narrow fruit seam omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '01dfab52-1214-532b-8f84-ea5dce7a2998'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/banana_01dfab52-1214-532b-8f84-ea5dce7a2998.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bunch-of-bananas-batch-010-10'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('banana',)

    def build(self):
        self.path('outer',(30,6),('L',(38,6)),('L',(38,14)),('A',(42,24),12,18,True),('A',(24,42),18,18,True),('A',(6,28),18,14,True),('A',(30,14),24,14,False),('L',(30,6)),closed=True)
        self.path('fruit-seam',(30,14),('A',(14,38),20,24,True))
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
