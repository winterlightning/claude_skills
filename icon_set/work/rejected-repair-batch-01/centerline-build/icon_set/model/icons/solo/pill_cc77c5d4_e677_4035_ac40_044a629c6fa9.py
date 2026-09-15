"""pill: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc77c5d4-e677-4035-ac40-044a629c6fa9'
SOURCE_PATH = 'pictographic-primitives/health/pill_cc77c5d4-e677-4035-ac40-044a629c6fa9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Pill(Solo48):
    icon_id = 'pill'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('pill', 'health')

    def build(self):
        # Plan: SQUARE; matching diagonal capsule ends with smooth tangents and one exact seam.
        # Reference: Lucide pill: parallel barrel edges and paired rounded caps.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        path('capsule',(9,25),[('L',(25,9)),('C',(29,5),(35,5),(39,9)),('C',(43,13),(43,19),(39,23)),
         ('L',(23,39)),('C',(19,43),(13,43),(9,39)),('C',(5,35),(5,29),(9,25))],True)
        self.add_line('seam',(17,17),(31,31));self.relate('connect','seam','capsule')
