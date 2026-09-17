"""Smiling Boy in Round Cap.

Plan: Rounded face below domed cap, mirrored closed eyes and smile. Bounds (6,6)-(42,42).
Construction: human_ref/user.svg simple circular face vocabulary. Source is head-only, not an avatar bust.
Reduction: Omitted ears and central cap seam; small closed eyes become eye dots, retaining the smile.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'de769bf2-a3ba-4ba6-9576-1ee1987a08e0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/chinese kid boy_de769bf2-a3ba-4ba6-9576-1ee1987a08e0.svg'
AUTHOR = 'gpt-6'


class IconSmilingBoyInRoundCap(Solo48):
    icon_id = 'smiling-boy-in-round-cap'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('smiling', 'boy', 'in', 'round', 'cap')

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
        path('head',(6,18),[('A',(24,6),18,12,True),('A',(42,18),18,12,True),('C',(24,42),(42,36),(35,42)),('C',(6,18),(13,42),(6,36))],True)
        self.add_line('brim',(6,18),(42,18));self.relate('connect','brim','head')
        self.add_dot('eye-left',(15,26));self.add_dot('eye-right',(33,26))
        path('smile',(21,32),[('C',(27,32),(23,34),(25,34))])
