"""lab-tube-experiment: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb52e379-0f84-4c69-a8bd-3b7fd2c8c58e'
SOURCE_PATH = 'pictographic-primitives/science/lab tube experiment_fb52e379-0f84-4c69-a8bd-3b7fd2c8c58e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class LabTubeExperiment(Solo48):
    icon_id = 'lab-tube-experiment'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'tube', 'experiment', 'science')

    def build(self):
        # Plan: VRECT_L; true semicircular tube bottom, parallel walls and matching lip bevels.
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

        path('tube',(10,14),[('L',(10,30)),('A',(24,44),14,14,False),('A',(38,30),14,14,False),('L',(38,14))])
        self.add_polyline('rim',(10,14),(10,8),(8,4),(40,4),(38,8),(38,14))
        self.add_line('liquid',(10,14),(38,14))
        self.relate('connect','tube','rim');self.relate('connect','tube','liquid');self.relate('connect','rim','liquid')
