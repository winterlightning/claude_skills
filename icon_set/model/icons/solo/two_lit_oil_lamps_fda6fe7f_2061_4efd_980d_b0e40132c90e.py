"""Two Lit Oil Lamps.

Plan: Two staggered oil bowls and pointed flames. Bounds (6,6)-(42,42).
Construction: Source diya pair and Lucide flame coherent teardrop.
Reduction: Separated staggered lamps with plain rims; omitted small wick strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'fda6fe7f-2061-4efd-980d-b0e40132c90e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/diwalis_fda6fe7f-2061-4efd-980d-b0e40132c90e.svg'
AUTHOR = 'gpt-6'


class IconTwoLitOilLamps(Solo48):
    icon_id = 'two-lit-oil-lamps'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('two', 'lit', 'oil', 'lamps')

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
        path('back-bowl',(6,26),[('L',(20,26)),('A',(6,26),7,7,True)],True)
        path('back-flame',(13,6),[('C',(17,13),(15,9),(17,10)),('A',(9,13),4,4,True),('C',(13,6),(9,10),(11,9))],True)
        path('front-bowl',(28,35),[('L',(42,35)),('A',(28,35),7,7,True)],True)
        path('front-flame',(35,15),[('C',(39,22),(37,18),(39,19)),('A',(31,22),4,4,True),('C',(35,15),(31,19),(33,18))],True)
