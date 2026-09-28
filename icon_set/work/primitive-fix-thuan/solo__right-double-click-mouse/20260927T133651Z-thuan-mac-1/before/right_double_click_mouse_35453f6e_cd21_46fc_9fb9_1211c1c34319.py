"""Right Double Click Mouse.

Plan: SQUARE (6,6)-(42,42). Rounded mouse and two nested click arcs above
its right button. Lucide mouse supplies the tangent capsule construction.
The click arcs are intentionally asymmetric and retain two distinct signals.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35453f6e-cd21-46fc-9fb9-1211c1c34319'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/computers/batch-06/right double click mouse_35453f6e-cd21-46fc-9fb9-1211c1c34319.svg'
AUTHOR = "gpt-6"

class RightDoubleClickMouse(Solo48):
    icon_id = 'right-double-click-mouse'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('right', 'double', 'click', 'mouse')

    def build(self):
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path("mouse",(16,20),[("A",(26,30),10,10,True),("L",(26,32)),("A",(6,32),10,10,True),("L",(6,30)),("A",(16,20),10,10,True)],True)
        path("button",(16,20),[("L",(16,25)),("A",(23,32),7,7,False),("L",(26,32))])
        self.relate("connect","mouse","button")
        path("click-inner",(26,15),[("A",(33,22),7,7,True)])
        path("click-outer",(26,6),[("A",(42,22),16,16,True)])
