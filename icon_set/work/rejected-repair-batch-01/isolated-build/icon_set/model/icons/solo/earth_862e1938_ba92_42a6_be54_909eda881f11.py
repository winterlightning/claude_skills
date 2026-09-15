"""earth-maps: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '862e1938-ba92-42a6-be54-909eda881f11'
SOURCE_PATH = 'pictographic-primitives/maps/earth_862e1938-ba92-42a6-be54-909eda881f11.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class EarthMaps(Solo48):
    icon_id = 'earth-maps'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'maps')

    def build(self):
        # Plan: CIRCLE; clean continent curves end exactly on the globe; fitted corner detours and partial contacts removed.
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

        circle_nodes('globe',24,24,20,[(8,12),(12,40),(36,8),(40,36)])
        path('west',(8,12),[('C',(10,12),(13,14),(15,16)),('L',(13,24)),('C',(13,26),(18,27),(21,28)),('C',(21,34),(18,39),(12,40))])
        path('east',(36,8),[('C',(30,9),(27,12),(27,16)),('C',(27,18),(31,20),(33,22)),('L',(34,29)),('C',(36,33),(37,35),(40,36))])
        self.relate('connect','west','globe');self.relate('connect','east','globe')
