"""playstation-vr: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7ccf92a-afad-5337-b90a-b52d403c4d46'
SOURCE_PATH = 'pictographic-primitives/technology/playstation vr_e7ccf92a-afad-5337-b90a-b52d403c4d46.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PlaystationVr(Solo48):
    icon_id = 'playstation-vr'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('technology', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('playstation', 'vr', 'technology')

    def build(self):
        # Plan: HRECT_L; true circular headband meets explicit visor nodes; both visor halves share matching tangent curves.
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

        path('headband',(6,26),[('A',(24,8),18,18,True),('A',(42,26),18,18,True)])
        path('visor',(4,32),[('C',(4,29),(4,28),(6,26)),('C',(10,22),(17,21),(24,21)),
         ('C',(31,21),(38,22),(42,26)),('C',(44,28),(44,29),(44,32)),
         ('C',(44,36),(43,40),(39,40)),('C',(34,40),(30,38),(24,38)),
         ('C',(18,38),(14,40),(9,40)),('C',(5,40),(4,36),(4,32))],True)
        self.relate('connect','headband','visor')
