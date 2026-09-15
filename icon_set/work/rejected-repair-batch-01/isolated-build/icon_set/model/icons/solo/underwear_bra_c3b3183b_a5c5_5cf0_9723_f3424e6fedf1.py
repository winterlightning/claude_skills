"""underwear-bra-clothes: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3b3183b-a5c5-5cf0-9723-f3424e6fedf1'
SOURCE_PATH = 'pictographic-primitives/clothes/underwear bra_c3b3183b-a5c5-5cf0-9723-f3424e6fedf1.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class UnderwearBraClothes(Solo48):
    icon_id = 'underwear-bra-clothes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('underwear', 'bra', 'clothes')

    def build(self):
        # Plan: HRECT_L; mirrored cups, straight equal straps and a shared center bridge replace uneven fitted curvature.
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

        self.add_line('left-strap',(8,8),(8,21));self.add_line('right-strap',(40,8),(40,21))
        path('left-cup',(8,21),[('C',(13,23),(21,26),(22,34)),('C',(23,38),(18,40),(14,40)),('C',(8,40),(4,36),(4,30)),('C',(4,26),(6,23),(8,21))],True)
        path('right-cup',(40,21),[('C',(35,23),(27,26),(26,34)),('C',(25,38),(30,40),(34,40)),('C',(40,40),(44,36),(44,30)),('C',(44,26),(42,23),(40,21))],True)
        self.add_line('bridge',(22,34),(26,34))
        for side in ['left','right']:
         self.relate('connect',side+'-strap',side+'-cup');self.relate('connect','bridge',side+'-cup')
