"""warp-flag: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31055c7d-f823-51b5-a0be-5eb87af6158d'
SOURCE_PATH = 'pictographic-primitives/design/warp flag_31055c7d-f823-51b5-a0be-5eb87af6158d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class WarpFlag(Solo48):
    icon_id = 'warp-flag'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'flag', 'design')

    def build(self):
        # Plan: HRECT_L; three equally spaced wave rails with shared endpoints and mirrored lobes.
        # Reference: Lucide flag: coherent flowing fabric boundary.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        # Rails are translations of one two-curve wave.
        for name,y in [('top',12),('middle',24),('bottom',36)]:
         path(name,(4,y),[('C',(12,y-16/3),(16,y-16/3),(24,y)),('C',(32,y+16/3),(36,y+16/3),(44,y))])
        self.add_line('left',(4,12),(4,36));self.add_line('right',(44,12),(44,36))
        for wall in ['left','right']:
         for rail in ['top','middle','bottom']:self.relate('connect',wall,rail)
