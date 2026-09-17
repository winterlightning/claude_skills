"""Hand Touching Forehead.

Plan: Right-facing head and extended ceremonial finger share the forehead point. Bounds (6,6)-(42,42).
Construction: Human reference minimal anatomy and Lucide hand contour; source face/profile touch.
Reduction: Removed eye and secondary finger crease.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'e1e75a9a-1285-46a2-b38e-bb62cba9ea5a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/bhaubeej_e1e75a9a-1285-46a2-b38e-bb62cba9ea5a.svg'
AUTHOR = 'gpt-6'


class HandTouchingForehead(Solo48):
    icon_id = 'hand-touching-forehead'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('hand', 'touching', 'forehead')

    def build(self) -> None:

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
        path('profile',(6,6),[('C',(20,14),(13,6),(18,9)),('L',(26,28)),('L',(20,28)),('L',(20,34)),('A',(14,40),6,6,True),('L',(10,40)),('L',(10,42))])
        path('hand',(42,6),[('L',(33,6)),('C',(20,14),(27,6),(23,10)),('L',(37,14)),('C',(42,24),(32,19),(35,25))])
        self.relate('connect','profile','hand')
