"""plant-93a59e45: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93a59e45-5521-49b0-9911-63d35bb7f98a'
SOURCE_PATH = 'pictographic-primitives/nature/plant_93a59e45-5521-49b0-9911-63d35bb7f98a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Plant93a59e45(Solo48):
    icon_id = 'plant-93a59e45'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    categories = ('nature', 'primitives')
    aliases = ()
    keywords = ('plant', 'nature')

    def build(self):
        # Plan: SQUARE; mirrored leaf curves with shared vein/stem nodes; no duplicate tip or one-unit attachment fragments.
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

        path('leaves',(24,36),[('C',(14,36),(6,29),(6,20)),('C',(12,21),(16,23),(18,26)),
         ('C',(16,18),(20,10),(24,6)),('C',(28,10),(32,18),(30,26)),
         ('C',(32,23),(36,21),(42,20)),('C',(42,29),(34,36),(24,36))],True)
        self.add_line('stem',(24,36),(24,42));self.relate('connect','stem','leaves')

        path('veins',(18,26),[('C',(19,30),(22,34),(24,36)),('C',(26,34),(29,30),(30,26))])
        self.relate('connect','veins','leaves');self.relate('connect','veins','stem')
