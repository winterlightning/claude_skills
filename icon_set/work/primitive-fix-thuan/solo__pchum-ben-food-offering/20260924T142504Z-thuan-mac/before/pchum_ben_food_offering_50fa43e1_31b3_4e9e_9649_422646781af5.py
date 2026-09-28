"""Pchum Ben Food Offering.

Plan: Bottle, one upright leaf, and wrapped food parcel; centerlines (6,6)-(42,42).
Construction: Source offering; Lucide leaf uses one coherent leaf contour.
Reduction: Reduced paired leaves to one; omitted veins, narrow bands and second parcel.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '50fa43e1-31b3-4e9e-9649-422646781af5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/pchum ben acnestor day_50fa43e1-31b3-4e9e-9649-422646781af5.svg'
AUTHOR = 'gpt-6'


class IconPchumBenFoodOffering(Solo48):
    icon_id = 'pchum-ben-food-offering'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('pchum', 'ben', 'food', 'offering')

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
        path('bottle',(10,6),[('L',(18,6)),('L',(18,14)),('C',(22,22),(18,17),(22,18)),('L',(22,38)),('A',(18,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,22)),('C',(10,14),(6,18),(10,17)),('L',(10,6))],True)
        path('leaf',(34,6),[('C',(34,24),(46,14),(43,24)),('C',(34,6),(31,24),(32,12))],True)
        path('parcel',(32,32),[('L',(38,32)),('L',(42,42)),('L',(30,42)),('L',(32,32))],True)
