"""supermarket: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ecb2335d-e13a-55e5-b6ac-15187eac9fdd'
SOURCE_PATH = 'pictographic-primitives/school-learning/supermarket_ecb2335d-e13a-55e5-b6ac-15187eac9fdd.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Supermarket(Solo48):
    icon_id = 'supermarket'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'school-learning'
    aliases = ()
    keywords = ('supermarket', 'school-learning')

    def build(self):
        # Plan: SQUARE; symmetric building tiers and door, with a straight flag and exact roof junctions.
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

        self.add_polyline('body',(8,24),(8,42),(20,42),(28,42),(40,42),(40,24))
        self.add_polyline('left-step',(6,24),(8,24),(16,24),(16,15))
        self.add_polyline('right-step',(42,24),(40,24),(32,24),(32,15))
        self.add_polyline('roof',(14,15),(16,15),(24,15),(32,15),(34,15))
        self.add_polyline('flag',(24,15),(24,6),(32,6))
        path('door',(20,42),[('L',(20,34)),('A',(24,30),4,4,True),('A',(28,34),4,4,True),('L',(28,42))])
        for side in ['left-step','right-step']:self.relate('connect',side,'body');self.relate('connect',side,'roof')
        self.relate('connect','roof','flag');self.relate('connect','door','body')
