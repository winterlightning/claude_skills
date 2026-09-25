"""Ceremonial deity bust beneath two raised conch-like forms. Circular lower face replaces the rejected flat-bottomed arch, with symmetrical shoulders. Bounds (6,6)-(42,42).
Keyshape SQUARE; fresh revision for feedback: Bad stroke drawn.
Construction reference: Shared human_ref/user.svg informs rounded face and shoulders; original headdress and raised forms retained.
Omissions: Small forehead U and internal conch seams omitted for clearance; continuous face/shoulder contacts follow the original bust.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/vaikuntha ekadashi_0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arched-figure-beneath-paired-raised-forms-batch-014-08'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('vaikuntha', 'ekadashi')

    def build(self):
        self.path('head',(14,32),('L',(14,28)),('A',(34,28),10,10,True),('L',(34,32)),('A',(14,32),10,10,True),closed=True)
        self.path('left-shoulder',(14,32),('A',(6,40),8,8,False),('L',(6,42)))
        self.path('right-shoulder',(34,32),('A',(42,40),8,8,True),('L',(42,42)))
        self.add_polyline('raised-left',(6,16),(6,10),(12,6),(14,10))
        self.add_polyline('raised-right',(42,16),(42,10),(36,6),(34,10))
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
