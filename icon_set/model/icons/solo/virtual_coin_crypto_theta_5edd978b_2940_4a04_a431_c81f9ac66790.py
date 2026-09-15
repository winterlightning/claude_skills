"""virtual-coin-crypto-theta: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5edd978b-2940-4a04-a431-c81f9ac66790'
SOURCE_PATH = 'pictographic-primitives/money/virtual coin crypto theta_5edd978b-2940-4a04-a431-c81f9ac66790.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class VirtualCoinCryptoTheta(Solo48):
    icon_id = 'virtual-coin-crypto-theta'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'theta', 'money')

    def build(self):
        # Plan: VRECT_L; four identical tangent corners; equal bars and mirrored central stems replace mismatched chamfers and arm lengths.
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

        path('frame',(12,4),[('L',(36,4)),('A',(40,8),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),
         ('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        for name,y,tip in [('upper',18,13),('lower',30,35)]:
         self.add_polyline(name,(18,y),(24,y),(30,y));self.add_line(name+'-stem',(24,y),(24,tip));self.relate('connect',name,name+'-stem')
