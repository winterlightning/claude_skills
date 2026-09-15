"""curly-brackets-programing: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9944ea4-e25f-57dc-a6ca-a168c1412bdb'
SOURCE_PATH = 'pictographic-primitives/programing/curly brackets_c9944ea4-e25f-57dc-a6ca-a168c1412bdb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class CurlyBracketsPrograming(Solo48):
    icon_id = 'curly-brackets-programing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('curly', 'brackets', 'programing')

    def build(self):
        # Plan: HRECT_L; mirrored braces with matching shoulders and centered cusps.
        # Reference: Lucide braces: paired repeated curved brackets.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        for side,mirror in [('left',False),('right',True)]:
         def p(x,y):return (48-x,y) if mirror else (x,y)
         path(side,p(12,8),[('L',p(10,8)),('C',p(7,8),p(6,10),p(6,13)),('L',p(6,18)),
         ('C',p(6,22),p(6,24),p(4,24)),('C',p(6,24),p(6,26),p(6,30)),('L',p(6,35)),
         ('C',p(6,38),p(7,40),p(10,40)),('L',p(12,40))])
