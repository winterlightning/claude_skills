"""Ugadi Kalash and Bowl.

Plan: Round kalash left with pointed foliage and small bowl right. Bounds (6,6)-(42,42).
Construction: Source ritual vessels; Lucide leaf and cooking-pot coherent silhouettes.
Reduction: One large leaf replaces three crowded leaves; single pot rim, separated bowl and straight spoon.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '4d447beb-a73a-497b-b364-e527271a9f1c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/ugadi 1_4d447beb-a73a-497b-b364-e527271a9f1c.svg'
AUTHOR = 'gpt-6'


class IconUgadiKalashAndBowl(Solo48):
    icon_id = 'ugadi-kalash-and-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('ugadi', 'kalash', 'and', 'bowl')

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
        path('pot',(8,24),[('L',(18,24)),('C',(20,34),(19,28),(20,30)),('A',(6,34),7,8,True),('C',(8,24),(6,30),(7,28))],True)
        path('leaf',(8,24),[('C',(13,6),(6,16),(10,9)),('C',(18,24),(20,12),(20,20))]);self.relate('connect','leaf','pot')
        path('bowl',(30,34),[('L',(36,34)),('L',(42,34)),('A',(30,34),6,8,True)],True)
        self.add_line('spoon',(36,34),(36,24));self.relate('connect','spoon','bowl')
