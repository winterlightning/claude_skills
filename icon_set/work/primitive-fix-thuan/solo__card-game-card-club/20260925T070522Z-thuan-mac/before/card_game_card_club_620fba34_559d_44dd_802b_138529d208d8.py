"""card-game-card-club: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '620fba34-559d-44dd-802b-138529d208d8'
SOURCE_PATH = 'pictographic-primitives/entertainment/card game card club_620fba34-559d-44dd-802b-138529d208d8.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class CardGameCardClub(Solo48):
    icon_id = 'card-game-card-club'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('card', 'game', 'club', 'entertainment')

    def build(self):
        # Plan: VRECT_L; three clean club lobes, mirrored side bowls and an exact centered stem.
        # Reference: No inspected Lucide club match; preserve the three-lobe card-suit silhouette.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        path('club',(24,4),[('C',(29,4),(32,8),(32,13)),('C',(32,16),(31,18),(30,20)),
         ('C',(36,18),(40,22),(40,27)),('C',(40,32),(36,36),(31,36)),('C',(28,36),(26,34),(24,32)),
         ('C',(22,34),(20,36),(17,36)),('C',(12,36),(8,32),(8,27)),
         ('C',(8,22),(12,18),(18,20)),('C',(17,18),(16,16),(16,13)),('C',(16,8),(19,4),(24,4))],True)
        self.add_line('stem',(24,32),(24,44));self.relate('connect','stem','club')
