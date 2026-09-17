"""Roast Chicken Meal with Bottle.

Plan: Roast silhouette on platter, diagonal drumstick and bottle behind left. Bounds (6,6)-(42,42).
Construction: Source roast and bottle; coherent rounded food silhouette. No useful exact Lucide roast match.
Reduction: Simplified platter stroke and single round bone end, no bottle bands.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '36564268-460f-43ca-ab9e-6a481a21b37e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/eid feast food_36564268-460f-43ca-ab9e-6a481a21b37e.svg'
AUTHOR = 'gpt-6'


class IconRoastChickenMealWithBottle(Solo48):
    icon_id = 'roast-chicken-meal-with-bottle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('roast', 'chicken', 'meal', 'with', 'bottle')

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
        path('bottle',(6,26),[('L',(10,14)),('L',(10,6)),('L',(18,6)),('L',(18,14)),('L',(18,16))])
        path('roast',(10,42),[('C',(30,25),(10,31),(20,25)),('C',(42,42),(39,25),(42,33)),('L',(10,42))],True)
        path('leg',(30,25),[('L',(38,15))]);self.relate('connect','leg','roast')
        path('bone',(38,15),[('A',(38,9),3,3,True),('A',(38,15),3,3,True)],True);self.relate('connect','leg','bone')
        self.add_line('platter',(6,42),(10,42));self.relate('connect','platter','roast')
