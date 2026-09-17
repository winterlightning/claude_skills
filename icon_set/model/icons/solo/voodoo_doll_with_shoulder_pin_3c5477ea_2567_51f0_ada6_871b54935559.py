"""Voodoo Doll with Shoulder Pin.

Plan: Blank rounded doll with spread legs and a pin entering right shoulder. Bounds (6,6)-(42,42).
Construction: Source doll; human_ref simple rounded limbs as toy geometry.
Reduction: Blank circular toy head, single-stroke limbs and right shoulder pin retain the source identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '3c5477ea-2567-51f0-ada6-871b54935559'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/halloween voodoo doll_3c5477ea-2567-51f0-ada6-871b54935559.svg'
AUTHOR = 'gpt-6'


class IconVoodooDollWithShoulderPin(Solo48):
    icon_id = 'voodoo-doll-with-shoulder-pin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('voodoo', 'doll', 'with', 'shoulder', 'pin')

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
        circle('head',20,14,8)
        self.add_line('body',(20,22),(20,34));self.relate('connect','head','body')
        for name,a,b in [('arm-left',(20,30),(6,32)),('arm-right',(20,30),(34,32)),('leg-left',(20,34),(12,42)),('leg-right',(20,34),(30,42))]:self.add_line(name,a,b);self.relate('connect',name,'body')
        circle('pin-head',39,10,3);self.add_line('pin',(39,13),(34,32));self.relate('connect','pin','pin-head');self.relate('connect','pin','arm-right')
