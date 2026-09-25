"""smile-fd6ce47d: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd6ce47d-6adc-5951-8160-a2f6a03df6da'
SOURCE_PATH = 'pictographic-primitives/smileys/smile_fd6ce47d-6adc-5951-8160-a2f6a03df6da.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class SmileFd6ce47d(Solo48):
    icon_id = 'smile-fd6ce47d'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('smile', 'smileys')

    def build(self):
        # Plan: CIRCLE; identical smooth closed-eye arches and one symmetric smile; remove tiny loops, retraced cubics and asymmetric eye ends.
        # Reference: Shared human_ref/user.svg: circular head vocabulary; supplied expression has no body.
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

        oval('face',24,24,20)
        for name,cx in [('left',16),('right',32)]:
         path(name+'-eye',(cx-3,20),[('A',(cx+3,20),3,3,True)])
        path('smile',(14,29),[('C',(16,33),(20,35),(24,35)),('C',(28,35),(32,33),(34,29))])
