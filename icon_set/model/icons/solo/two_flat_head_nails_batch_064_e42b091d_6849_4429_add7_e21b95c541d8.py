"""Two Construction Nails.

Plan: Two flat head nails with an upright left shaft and a deliberately tilted right shaft.
Reduction / construction: No exact Lucide match; simplify each nail to a T stroke with a long shaft.
Envelope: SQUARE, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e42b091d-6849-4429-add7-e21b95c541d8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hardware nails_e42b091d-6849-4429-add7-e21b95c541d8.svg'
AUTHOR = 'gpt-6'


class Batch064Icon4(Solo48):
    icon_id = 'two-flat-head-nails-batch-064'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('two', 'flat', 'head', 'nails')

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

        self.add_polyline('left-head',(6,6),(14,6),(22,6))
        self.add_line('left-shaft',(14,6),(14,42))
        self.relate('connect','left-head','left-shaft')
        self.add_polyline('right-head',(28,12),(35,16),(42,20))
        self.add_line('right-shaft',(35,16),(27,40))
        self.relate('connect','right-head','right-shaft')
