"""Faucet and Toilet Pair.

Plan: Wall faucet upper left accompanies side-view toilet lower right. Bounds (6,6)-(42,42).
Construction: Source paired bathroom fixtures; no exact local Lucide toilet match.
Reduction: Decorative diagonal divider omitted; faucet handle is one stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'e9cf87b4-05c8-438b-ac42-51e95b0ff84f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/sanitation toilet sink_e9cf87b4-05c8-438b-ac42-51e95b0ff84f.svg'
AUTHOR = 'gpt-6'


class IconFaucetAndToiletPair(Solo48):
    icon_id = 'faucet-and-toilet-pair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    aliases = ()
    keywords = ('faucet', 'and', 'toilet', 'pair')

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
        path('tap',(6,22),[('L',(6,14)),('A',(14,6),8,8,True),('A',(22,14),8,8,True)])
        path('toilet',(22,26),[('L',(34,26)),('L',(34,14)),('L',(42,14)),('L',(42,34)),('L',(42,42)),('L',(28,42)),('L',(30,34)),('A',(22,26),8,8,True)],True)
        self.add_line('bowl',(34,26),(42,26));self.relate('connect','bowl','toilet')
