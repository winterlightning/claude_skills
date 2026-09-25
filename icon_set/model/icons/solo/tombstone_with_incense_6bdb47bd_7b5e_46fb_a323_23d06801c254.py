"""Tombstone with Incense.

Plan: Round-topped gravestone above base, with incense sticks in front. Bounds (6,6)-(42,42).
Construction: Source tombstone outline; no useful exact Lucide incense match.
Reduction: One incense stick and bowl holder; omitted plinth to preserve holder clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '6bdb47bd-7b5e-46fb-a323-23d06801c254'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/qingming festival_6bdb47bd-7b5e-46fb-a323-23d06801c254.svg'
AUTHOR = 'gpt-6'


class IconTombstoneWithIncense(Solo48):
    icon_id = 'tombstone-with-incense'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('tombstone', 'with', 'incense')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path('stone',(6,32),[('L',(6,24)),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('L',(42,32))])
        path('holder',(18,36),[('L',(24,36)),('L',(30,36)),('A',(18,36),6,6,True)],True)
        self.add_line('incense',(24,20),(24,36));self.relate('connect','incense','holder')
