"""Chess knight beside a pawn. Curved knight mane and rounded muzzle; pawn head flows into a broad tapered pedestal instead of a pinched triangle. Bounds (6,6)-(42,42).
Keyshape SQUARE; fresh revision for feedback: Bad stroke drawn.
Construction reference: Lucide chess-knight: round mane; chess-pawn: integrated round head and flared stem.
Omissions: Tiny horse eye and layered pedestal seams omitted; both full piece silhouettes retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e8184764-3245-40c1-a10d-883944a9fe13'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/chess_e8184764-3245-40c1-a10d-883944a9fe13.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chess-knight-and-pawn-batch-013-03'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    categories = ('primitives', 'hobbies')
    aliases = ()
    keywords = ('chess',)

    def build(self):
        self.path('knight',(14,6),('A',(22,18),8,12,True),('L',(22,42)),('L',(6,42)),('L',(10,28)),('L',(14,20)),('L',(8,20)),('A',(6,18),2,2,True),('L',(6,16)),('L',(14,10)),('L',(14,6)),closed=True)
        self.add_polyline('pawn-body',(33,24),(32,42),(42,42),(41,24))
        self.add_arc('pawn-head',(41,24),(33,24),radius_x=5,large_arc=True,sweep=False)
        self.contours=[c for c in self.contours if c.contour_id!='pawn-body']
        self.add_contour('pawn','pawn-body-1','pawn-body-2','pawn-body-3','pawn-head',closed=True)
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
