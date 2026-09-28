"""card-game-card-spade: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2cf64d69-34f9-465c-a798-c36aec350d36'
SOURCE_PATH = 'pictographic-primitives/entertainment/card game card spade_2cf64d69-34f9-465c-a798-c36aec350d36.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class CardGameCardSpade(Solo48):
    icon_id = 'card-game-card-spade'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ()
    keywords = ('card', 'game', 'spade', 'entertainment')

    def build(self):
        # Plan: VRECT_L; mirrored spade shoulders and bowl curves with a centered tip and stem.
        # Reference: No inspected Lucide spade match; paired bowls and one shared axis.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        path('spade',(24,4),[('C',(20,11),(8,18),(8,27)),('C',(8,33),(12,37),(17,37)),
         ('C',(20,37),(22,35),(24,32)),('C',(26,35),(28,37),(31,37)),
         ('C',(36,37),(40,33),(40,27)),('C',(40,18),(28,11),(24,4))],True)
        self.add_line('stem',(24,32),(24,44));self.relate('connect','stem','spade')
