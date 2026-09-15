"""glass-drinks: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ad0cd10-bf8c-4b51-9e81-06a67e3d6f68'
SOURCE_PATH = 'pictographic-primitives/drinks/glass_3ad0cd10-bf8c-4b51-9e81-06a67e3d6f68.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class GlassDrinks(Solo48):
    icon_id = 'glass-drinks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('glass', 'drinks')

    def build(self):
        # Plan: VRECT_L; symmetric circular bowl with its stem attached at the exact bottom extreme.
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

        path('bowl',(8,12),[('L',(8,4)),('L',(40,4)),('L',(40,12)),('A',(24,28),16,16,True),('A',(8,12),16,16,True)],True)
        self.add_line('stem',(24,28),(24,44));self.add_polyline('base',(14,44),(24,44),(34,44))
        self.relate('connect','stem','bowl');self.relate('connect','stem','base')
