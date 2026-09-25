"""Striped Candy Cane.

Plan: Round hook, thick straight shaft, two diagonal stripe boundaries. Bounds (8,4)-(40,44).
Construction: Lucide candy-cane concentric hook and rounded ends; source upright left hook.
Reduction: One diagonal stripe boundary replaces three closely spaced stripes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '0af588e4-e000-4d1d-aa24-f440273a2df0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/sugar cane_0af588e4-e000-4d1d-aa24-f440273a2df0.svg'
AUTHOR = 'gpt-6'


class IconStripedCandyCane(Solo48):
    icon_id = 'striped-candy-cane'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('striped', 'candy', 'cane')

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
        path('cane',(8,20),[('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,28)),('L',(40,40)),('A',(32,40),4,4,True),('L',(32,32)),('L',(32,20)),('A',(24,12),8,8,False),('A',(16,20),8,8,False),('A',(8,20),4,4,True)],True)
        self.add_line('stripe',(32,32),(40,28));self.relate('connect','stripe','cane')
