"""ghost: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a257f108-5e8d-40d4-97ad-643846319b7b'
SOURCE_PATH = 'pictographic-primitives/symbol/ghost_a257f108-5e8d-40d4-97ad-643846319b7b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Ghost(Solo48):
    icon_id = 'ghost'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('ghost', 'symbol')

    def build(self):
        # Plan: VRECT_L; circular crown, straight sides, and evenly repeated scallops.
        # Reference: Lucide ghost: smooth dome and deliberate repeated hem.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        path('ghost',(8,36),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,36)),
         ('C',(40,40),(40,44),(36,44)),('C',(33,44),(33,40),(30,40)),('C',(27,40),(27,44),(24,44)),
         ('C',(21,44),(21,40),(18,40)),('C',(15,40),(15,44),(12,44)),('C',(8,44),(8,40),(8,36))],True)
