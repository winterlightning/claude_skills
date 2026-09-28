"""dollar-sign: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7930e153-2438-44ec-8db7-960bb9aa10cc'
SOURCE_PATH = 'pictographic-primitives/state/dollar sign_7930e153-2438-44ec-8db7-960bb9aa10cc.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class DollarSign(Solo48):
    icon_id = 'dollar-sign'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives-generate', 'state')
    aliases = ()
    keywords = ('dollar', 'sign', 'state')

    def build(self):
        # Plan: VRECT_L; one tangent-continuous S, paired bowls, exact intersections at three shared stem nodes.
        # Reference: Lucide dollar-sign: coherent bowl and stem geometry.
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

        path('s',(38,14),[('C',(36,10),(30,8),(24,8)),('C',(15,8),(8,10),(8,16)),
         ('C',(8,22),(16,23),(24,24)),('C',(32,25),(40,26),(40,32)),
         ('C',(40,38),(33,40),(24,40)),('C',(18,40),(12,38),(10,34))])
        self.add_polyline('stem',(24,4),(24,8),(24,24),(24,40),(24,44));self.relate('connect','stem','s')
