"""mobile-me-logo: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '936a3619-3936-495a-bbd0-7dd442d5c39e'
SOURCE_PATH = 'pictographic-primitives/logos/mobile me logo_936a3619-3936-495a-bbd0-7dd442d5c39e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class MobileMeLogo(Solo48):
    icon_id = 'mobile-me-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('mobile', 'me', 'logo', 'logos')

    def build(self):
        # Plan: HRECT_L; smooth crown, matching shoulders and tangent base replace lumpy cloud joins.
        # Reference: Lucide cloud: continuous cloud silhouette.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        path('cloud',(14,40),[('A',(4,30),10,10,True),('A',(14,20),10,10,True),
         ('C',(14,13),(18,8),(24,8)),('C',(30,8),(34,13),(34,20)),
         ('A',(44,30),10,10,True),('A',(34,40),10,10,True),('L',(14,40))],True)
