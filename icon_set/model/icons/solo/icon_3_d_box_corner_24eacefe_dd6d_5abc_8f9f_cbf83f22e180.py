"""icon-3-d-box-corner: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24eacefe-dd6d-5abc-8f9f-cbf83f22e180'
SOURCE_PATH = 'pictographic-primitives/technology/3 d box corner_24eacefe-dd6d-5abc-8f9f-cbf83f22e180.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Icon3DBoxCorner(Solo48):
    icon_id = 'icon-3-d-box-corner'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('d', 'box', 'corner', 'technology')

    def build(self):
        # Plan: SQUARE; all cube edges meet shared integer vertices; shortened side walls repaired.
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

        self.add_polyline('top',(24,14),(36,21),(24,28),(12,21),closed=True)
        self.add_polyline('bottom',(12,21),(12,35),(24,42),(36,35),(36,21))
        self.add_line('front',(24,28),(24,42))
        self.add_line('upper-axis',(24,14),(24,6))
        self.add_line('left-axis',(12,35),(6,39));self.add_line('right-axis',(36,35),(42,39))
        self.relate('connect','top','bottom');self.relate('connect','front','top');self.relate('connect','front','bottom');self.relate('connect','upper-axis','top')
        self.relate('connect','left-axis','bottom');self.relate('connect','right-axis','bottom')
