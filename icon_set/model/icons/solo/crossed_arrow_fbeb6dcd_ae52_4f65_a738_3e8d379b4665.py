"""crossed-arrow: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fbeb6dcd-ae52-4f65-a738-3e8d379b4665'
SOURCE_PATH = 'pictographic-primitives/symbol/crossed arrow_fbeb6dcd-ae52-4f65-a738-3e8d379b4665.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class CrossedArrow(Solo48):
    icon_id = 'crossed-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('crossed', 'arrow', 'symbol')

    def build(self):
        # Plan: SQUARE; matching arrowheads with centered shafts and mirrored smooth tail curls; no broken arc/line tail.
        # Reference: Lucide move-up-right: straight arrow direction and shared attachment points.
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

        # Mirrored hollow arrowheads, centered shafts, and paired circular tails.
        self.add_polyline('head-left',(6,6),(20,8),(8,20),closed=True)
        self.add_polyline('head-right',(42,6),(28,8),(40,20),closed=True)
        self.add_polyline('shaft-left',(14,14),(24,24),(34,34))
        self.add_polyline('shaft-right',(34,14),(24,24),(14,34))
        self.relate('connect','head-left','shaft-left');self.relate('connect','head-right','shaft-right');self.relate('connect','shaft-left','shaft-right')
        path('tail-left',(6,36),[('C',(6,32),(10,30),(14,34)),('C',(18,38),(16,42),(12,42))])
        path('tail-right',(42,36),[('C',(42,32),(38,30),(34,34)),('C',(30,38),(32,42),(36,42))])
        self.relate('connect','tail-left','shaft-right');self.relate('connect','tail-right','shaft-left')
