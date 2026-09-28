"""symbol-artillery: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7e31bff-1b16-45b4-8791-44858266dfbc'
SOURCE_PATH = 'pictographic-primitives/war/symbol artillery_a7e31bff-1b16-45b4-8791-44858266dfbc.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class SymbolArtillery(Solo48):
    icon_id = 'symbol-artillery'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('symbol', 'artillery', 'war')

    def build(self):
        # Plan: VRECT_L; mirrored rays and a smooth symmetric shell body with exact shared central nodes.
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

        path('body',(9,25),[('C',(9,22),(12,20),(15,19)),('C',(18,18),(21,17),(24,17)),('C',(27,17),(30,18),(33,19)),('C',(36,20),(39,22),(39,25)),('L',(39,36)),('C',(39,41),(31,44),(24,44)),('C',(17,44),(9,41),(9,36)),('L',(9,25))],True)
        self.add_polyline('rays',(8,4),(24,14),(40,4))
        self.add_polyline('center',(24,4),(24,14),(24,17))
        path('left-ray',(8,4),[('L',(8,12)),('C',(8,15),(11,18),(15,19))])
        path('right-ray',(40,4),[('L',(40,12)),('C',(40,15),(37,18),(33,19))])
        self.relate('connect','rays','center');self.relate('connect','center','body')
        for s in ['left-ray','right-ray']:self.relate('connect',s,'rays');self.relate('connect',s,'body')
