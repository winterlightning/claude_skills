"""water-bottle-glass: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8717b7d0-2a5a-5dcc-9d53-f284ee945681'
SOURCE_PATH = 'pictographic-primitives/drinks/water bottle glass_8717b7d0-2a5a-5dcc-9d53-f284ee945681.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class WaterBottleGlass(Solo48):
    icon_id = 'water-bottle-glass'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('water', 'bottle', 'glass', 'drinks')

    def build(self):
        # Plan: VRECT_L; paired bottle shoulders, equal corner radii and a smooth water surface.
        # Reference: No close Lucide bottle match; mirrored bottle boundary and flowing waterline.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        path('bottle',(18,4),[('L',(18,8)),('C',(18,12),(8,12),(8,18)),('L',(8,24)),('L',(8,39)),
         ('C',(8,42),(10,44),(14,44)),('L',(34,44)),('C',(38,44),(40,42),(40,39)),
         ('L',(40,24)),('L',(40,18)),('C',(40,12),(30,12),(30,8)),('L',(30,4))])
        path('water',(8,24),[('C',(18,20),(30,28),(40,24))]);self.relate('connect','water','bottle')
