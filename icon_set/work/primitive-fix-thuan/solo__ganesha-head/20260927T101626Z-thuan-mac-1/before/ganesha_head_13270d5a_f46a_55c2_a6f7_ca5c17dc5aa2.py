"""Ganesha Head.

Plan: Crowned elephant head; matching broad ears and an asymmetric curled trunk. Bounds (6,6)-(42,42).
Construction: Source crown, elephant ears and right curl; no useful Lucide elephant match.
Reduction: Omitted facial marks and extra forehead seam; open-ended trunk curve preserves a broad curl without a narrow pocket.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '13270d5a-f46a-55c2-a6f7-ca5c17dc5aa2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/ganesh chaturthi_13270d5a-f46a-55c2-a6f7-ca5c17dc5aa2.svg'
AUTHOR = 'gpt-6'


class GaneshaHead(Solo48):
    icon_id = 'ganesha-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('ganesha', 'head')

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
        path('head',(30,28),[('C',(34,18),(36,24),(35,20)),('L',(24,6)),('L',(14,18)),('C',(18,30),(12,24),(14,30)),('L',(18,34)),('A',(26,42),8,8,False),('L',(34,42))])
        path('ear-left',(14,18),[('C',(6,22),(8,14),(6,16)),('C',(18,30),(6,32),(12,34))])
        path('ear-right',(34,18),[('C',(42,22),(40,14),(42,16)),('C',(30,28),(42,32),(36,34))])
        self.relate('connect','ear-left','head');self.relate('connect','ear-right','head')
