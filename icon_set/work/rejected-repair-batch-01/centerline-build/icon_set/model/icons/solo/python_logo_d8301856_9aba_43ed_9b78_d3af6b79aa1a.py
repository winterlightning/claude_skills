"""python-logo: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8301856-9aba-43ed-9b78-d3af6b79aa1a'
SOURCE_PATH = 'pictographic-primitives/logos/python logo_d8301856-9aba-43ed-9b78-d3af6b79aa1a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PythonLogo(Solo48):
    icon_id = 'python-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('python', 'logo', 'logos')

    def build(self):
        # Plan: SQUARE; smooth aligned interlocking runs with coherent corner tangents; subpixel undulations removed.
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

        # Two interlocking smooth runs, related by a half-turn.
        path('upper',(24,16),[('L',(16,16)),('L',(16,10)),('C',(16,7),(19,6),(24,6)),('C',(29,6),(32,7),(32,12)),('L',(32,17)),('C',(32,22),(29,24),(24,24)),('L',(22,24)),('C',(18,24),(16,26),(16,32)),('L',(12,32)),('C',(8,32),(6,29),(6,24)),('C',(6,19),(8,16),(12,16)),('L',(16,16))])
        path('lower',(24,32),[('L',(32,32)),('L',(32,38)),('C',(32,41),(29,42),(24,42)),('C',(19,42),(16,41),(16,36)),('L',(16,32))])
        path('right',(32,16),[('L',(36,16)),('C',(40,16),(42,19),(42,24)),('C',(42,29),(40,32),(36,32)),('L',(32,32))])
        self.relate('connect','upper','lower');self.relate('connect','upper','right');self.relate('connect','lower','right')
