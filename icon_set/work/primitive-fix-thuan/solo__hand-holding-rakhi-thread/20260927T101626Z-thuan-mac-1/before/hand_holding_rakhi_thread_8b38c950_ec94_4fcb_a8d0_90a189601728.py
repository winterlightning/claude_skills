"""Hand Holding Rakhi Thread.

Plan: Curled diagonal hand holds thread running to round rakhi upper right. Bounds (6,6)-(42,42).
Construction: Lucide hand curved thumb/palm; source diagonal hand and round thread ornament.
Reduction: Reduced folded finger creases to one thumb notch.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '8b38c950-ec94-4fcb-a8d0-90a189601728'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/raksha bandhan 1_8b38c950-ec94-4fcb-a8d0-90a189601728.svg'
AUTHOR = 'gpt-6'


class HandHoldingRakhiThread(Solo48):
    icon_id = 'hand-holding-rakhi-thread'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('hand', 'holding', 'rakhi', 'thread')

    def build(self) -> None:

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
        path('hand',(6,34),[('L',(6,25)),('C',(10,18),(6,22),(8,20)),('L',(20,8)),('A',(26,14),5,5,True),('L',(20,20)),('L',(27,24)),('C',(30,33),(32,26),(32,30)),('L',(23,40)),('C',(14,42),(20,42),(17,42)),('L',(6,34))],True)
        path('rakhi',(30,12),[('A',(42,12),6,6,True),('A',(36,18),6,6,True),('A',(30,12),6,6,True)],True)
        self.add_line('thread',(36,18),(30,33));self.relate('connect','thread','hand');self.relate('connect','thread','rakhi')
        self.add_line('tail',(6,34),(6,42));self.relate('connect','tail','hand')
