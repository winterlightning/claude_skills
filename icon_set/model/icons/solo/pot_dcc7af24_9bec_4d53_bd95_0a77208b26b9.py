"""pot: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dcc7af24-9bec-4d53-bd95-0a77208b26b9'
SOURCE_PATH = 'pictographic-primitives/furnitures/pot_dcc7af24-9bec-4d53-bd95-0a77208b26b9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Pot(Solo48):
    icon_id = 'pot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('pot', 'furnitures')

    def build(self):
        # Plan: SQUARE; matched body corners, symmetric lid and a single smooth handle; rim kink removed.
        # Reference: No close Lucide match; reconstruct the supplied subject from its owning geometry.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L':self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C':self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A':self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry=None):
            ry=rx if ry is None else ry
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)

        def circle_nodes(name,cx,cy,r,nodes=()):
            import math
            pts=set(nodes)|{(cx-r,cy),(cx+r,cy),(cx,cy-r),(cx,cy+r)}
            assert all((x-cx)**2+(y-cy)**2==r*r for x,y in pts)
            pts=sorted(pts,key=lambda p:math.atan2(p[1]-cy,p[0]-cx))
            path(name,pts[0],[('A',pt,r,r,True) for pt in pts[1:]+pts[:1]],True)

        def rounded(name,x1,y1,x2,y2,r):
            path(name,(x1+r,y1),[('L',(x2-r,y1)),('A',(x2,y1+r),r,r,True),('L',(x2,y2-r)),('A',(x2-r,y2),r,r,True),('L',(x1+r,y2)),('A',(x1,y2-r),r,r,True),('L',(x1,y1+r)),('A',(x1+r,y1),r,r,True)],True)

        path('body',(8,19),[('L',(6,37)),('C',(6,40),(7,42),(10,42)),('L',(30,42)),('C',(33,42),(34,40),(34,37)),('L',(32,19))])
        self.add_polyline('rim',(6,19),(8,19),(10,19),(30,19),(32,19))
        path('lid',(10,19),[('C',(11,12),(14,8),(20,8)),('C',(26,8),(29,12),(30,19))])
        self.add_line('knob',(20,6),(20,8))
        path('handle',(32,19),[('C',(38,16),(42,21),(42,26)),('C',(42,30),(37,28),(33,28))])
        self.relate('connect','body','rim');self.relate('connect','lid','rim');self.relate('connect','knob','lid');self.relate('connect','handle','body');self.relate('connect','handle','rim')
