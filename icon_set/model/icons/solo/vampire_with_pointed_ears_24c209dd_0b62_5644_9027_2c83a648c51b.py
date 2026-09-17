"""Vampire with Pointed Ears.

Plan: Circular face touches curved shoulders, surrounded by pointed high cape. Bounds (4,8)-(44,40).
Construction: human_ref/user.svg and icon-avatar touching head/shoulders. Source cape silhouette.
Reduction: Pointed ear strokes join the face and collar; small face and hairline details omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '24c209dd-0b62-5644-9027-2c83a648c51b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/halloween vampire_24c209dd-0b62-5644-9027-2c83a648c51b.svg'
AUTHOR = 'gpt-6'


class IconVampireWithPointedEars(Solo48):
    icon_id = 'vampire-with-pointed-ears'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('vampire', 'with', 'pointed', 'ears')
    human_construction = "bust"

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
        circle('head',24,16,8)
        path('shoulders',(4,40),[('L',(4,38)),('A',(12,30),20,10,True),('A',(24,28),20,10,True),('A',(36,30),20,10,True),('A',(44,38),20,10,True),('L',(44,40))]);self.relate('connect','head','shoulders')
        path('cape',(4,8),[('L',(12,30)),('L',(24,40)),('L',(36,30)),('L',(44,8))]);self.relate('connect','cape','shoulders')

        self.add_line('ear-left',(16,16),(4,8));self.add_line('ear-right',(32,16),(44,8));self.relate('connect','ear-left','head');self.relate('connect','ear-right','head')
        self.relate('connect','ear-left','cape');self.relate('connect','ear-right','cape')
