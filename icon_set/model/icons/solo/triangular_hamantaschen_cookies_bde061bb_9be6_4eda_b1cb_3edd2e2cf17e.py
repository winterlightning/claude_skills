"""Triangular Hamantaschen Cookies.

Plan: Two triangular pastries offset diagonally; front folded seam. Bounds (6,6)-(42,42).
Construction: Source triangular cookies; no useful exact Lucide hamantaschen match.
Reduction: Plain triangular pastry contours retain the diagonal pair; small internal fold seams omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'bde061bb-9be6-4eda-b1cb-3edd2e2cf17e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/purim feast of lots_bde061bb-9be6-4eda-b1cb-3edd2e2cf17e.svg'
AUTHOR = 'gpt-6'


class IconTriangularHamantaschenCookies(Solo48):
    icon_id = 'triangular-hamantaschen-cookies'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('triangular', 'hamantaschen', 'cookies')

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
        path('front',(6,42),[('L',(20,18)),('L',(28,32)),('L',(34,42)),('L',(6,42))],True)
        path('rear',(20,18),[('L',(28,6)),('L',(42,30)),('L',(28,32))]);self.relate('connect','rear','front')
