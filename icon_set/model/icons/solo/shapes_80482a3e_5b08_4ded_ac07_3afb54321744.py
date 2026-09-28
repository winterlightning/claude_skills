"""shapes: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80482a3e-5b08-4ded-ac07-3afb54321744'
SOURCE_PATH = 'pictographic-primitives/design/shapes_80482a3e-5b08-4ded-ac07-3afb54321744.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Shapes(Solo48):
    icon_id = 'shapes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('shapes', 'design')

    def build(self):
        # Plan: SQUARE; true circle ends exactly on the foreground square; one-unit connector stubs removed.
        # Reference: Lucide shapes: a shared overlap boundary between the circle and square.
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

        self.add_polyline('square',(19,19),(32,19),(42,19),(42,42),(19,42),(19,32),closed=True)
        path('circle',(32,19),[('A',(19,6),13,13,False),('A',(6,19),13,13,False),('A',(19,32),13,13,False)])
        self.relate('connect','circle','square')
