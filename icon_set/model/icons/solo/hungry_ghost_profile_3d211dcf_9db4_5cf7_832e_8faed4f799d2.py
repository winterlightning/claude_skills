"""Hungry Ghost Profile.

Plan: Left-facing supernatural face with pointed nose, open mouth and ornamental hat. Bounds (6,6)-(42,42).
Construction: Human-reference economy for facial silhouette; source profile and tall hat. Lucide ghost informs minimal facial detail only.
Reduction: Omitted the tiny eye; enlarged mouth and hat opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '3d211dcf-9db4-5cf7-832e-8faed4f799d2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/hungry ghost festival side_3d211dcf-9db4-5cf7-832e-8faed4f799d2.svg'
AUTHOR = 'gpt-6'


class IconHungryGhostProfile(Solo48):
    icon_id = 'hungry-ghost-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('hungry', 'ghost', 'profile')

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
        # Face uses the hat's lower brim as its upper boundary, avoiding a doubled seam.
        path('face',(14,18),[('C',(6,28),(9,21),(6,24)),('L',(20,26)),('C',(12,32),(20,30),(16,32)),('L',(12,38)),('A',(16,42),4,4,False),('C',(34,28),(24,42),(32,36))])
        path('hat',(8,18),[('L',(8,6)),('C',(34,14),(18,6),(28,9)),('L',(34,10)),('A',(42,10),4,4,True),('L',(42,22)),('C',(34,28),(42,27),(38,30)),('C',(14,18),(26,22),(20,18)),('L',(8,18))],True)
        self.relate('connect','face','hat')
