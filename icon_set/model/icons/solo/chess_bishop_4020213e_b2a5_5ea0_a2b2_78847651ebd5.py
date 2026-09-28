"""Chess bishop with a rounded finial, bulbous head, narrow stem and flared pedestal. Mirrored arcs about x=24; bounds (10,4)-(38,44).
Keyshape VRECT_M; fresh revision for feedback: Bad stroke drawn.
Construction reference: Lucide chess-bishop: bulb head and flared pedestal; supplied original governs the top finial.
Omissions: No internal pedestal seam; original has a continuous outline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4020213e-b2a5-5ea0-a2b2-78847651ebd5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess bishop_4020213e-b2a5-5ea0-a2b2-78847651ebd5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chess-bishop'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    categories = ('primitives', 'hobbies')
    aliases = ()
    keywords = ('chess', 'bishop')

    def build(self):
        self.path('bishop',(20,8),('A',(28,8),4,4,True),('L',(28,10)),('A',(34,22),6,12,True),('A',(30,30),4,8,True),('A',(28,34),2,4,False),('L',(28,36)),('A',(34,40),6,4,False),('A',(38,44),4,4,True),('L',(10,44)),('A',(14,40),4,4,True),('A',(20,36),6,4,False),('L',(20,34)),('A',(18,30),2,4,False),('A',(14,22),4,8,True),('A',(20,10),6,12,True),('L',(20,8)),closed=True)
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
