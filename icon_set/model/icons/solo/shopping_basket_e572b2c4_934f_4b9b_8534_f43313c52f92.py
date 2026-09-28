"""shopping-basket-e572b2c4: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e572b2c4-934f-4b9b-8534-f43313c52f92'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping basket_e572b2c4-934f-4b9b-8534-f43313c52f92.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ShoppingBasketE572b2c4(Solo48):
    icon_id = 'shopping-basket-e572b2c4'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('shopping', 'basket')

    def build(self):
        # Plan: HRECT_L; mirrored basket sides, tangent bottom corners and a smooth shared handle; no mismatched fitted corner pieces.
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

        self.add_polyline('rim',(4,18),(8,18),(40,18),(44,18))
        path('basket',(8,18),[('L',(10,35)),('C',(10+4/17,37),(12,40),(16,40)),('L',(32,40)),('C',(36,40),(38-4/17,37),(38,35)),('L',(40,18))])
        path('handle',(8,18),[('C',(11,12),(12,8),(18,8)),('L',(30,8)),('C',(36,8),(37,12),(40,18))])
        self.relate('connect','basket','rim');self.relate('connect','handle','rim');self.relate('connect','basket','handle')
