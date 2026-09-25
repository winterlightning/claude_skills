"""Bowl of Dip with Chip.

Plan: Bowl of dip with a triangular chip rising above its rim.
Reduction / construction: Soup: broad rounded bowl; omit dip swirl and chip speckles to preserve open space.
Envelope: SQUARE, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f74495e0-707c-43b4-9e73-9b2b4b692567'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hummus_f74495e0-707c-43b4-9e73-9b2b4b692567.svg'
AUTHOR = 'gpt-6'


class Batch064Icon12(Solo48):
    icon_id = 'bowl-of-dip-with-chip-batch-064'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bowl', 'of', 'dip', 'with', 'chip')

    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            point=start
            for i,command in enumerate(commands):
                kind,end,*args=command
                member=f"{name}-{i}"
                if kind=='L':
                    self.add_line(member,point,end)
                else:
                    rx,ry,sweep=args
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep)
                members.append(member)
                point=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)

        path('bowl',(6,26),[('L',(20,26)),('L',(30,26)),('L',(42,26)),('A',(6,26),18,16,True)],True)
        self.add_polyline('chip',(20,26),(26,6),(40,16),(30,26))
        self.relate('connect','bowl','chip')
