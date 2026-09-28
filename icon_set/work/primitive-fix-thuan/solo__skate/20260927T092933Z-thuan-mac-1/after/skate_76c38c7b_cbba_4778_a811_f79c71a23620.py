"""skate: reconstructed stroke graph on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '76c38c7b-cbba-4778-a811-f79c71a23620'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__skate/20260927T092933Z-thuan-mac-1/reference/skate_76c38c7b-cbba-4778-a811-f79c71a23620.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Skate(Solo48):
    icon_id = 'skate'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('skate', 'symbol')

    def build(self):
        # Plan: HRECT_M; mirrored smooth deck ends and larger aligned wheels.
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

        path('deck',(4,10),[('C',(5,16),(8,21),(12,24)),('L',(36,24)),('C',(40,21),(43,16),(44,10))])
        for i,x in enumerate([13,35]):
            self.add_arc(f'wheel-{i}-upper',(x-2,36),(x+2,36),radius_x=2)
            self.add_arc(f'wheel-{i}-lower',(x+2,36),(x-2,36),radius_x=2)
            self.add_contour(f'wheel-{i}',f'wheel-{i}-upper',f'wheel-{i}-lower',closed=True)
