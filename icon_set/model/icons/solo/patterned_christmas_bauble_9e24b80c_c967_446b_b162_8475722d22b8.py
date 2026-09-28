"""Patterned Christmas Bauble.

Plan: Round ornament with short suspension and broad zigzag middle band. Bounds (8,4)-(40,44).
Construction: Source patterned bauble; circle/ellipse construction on cardinal axes.
Reduction: Removed tiny dots and narrow cap; one zigzag stroke preserves the patterned identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '9e24b80c-c967-446b-b162-8475722d22b8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/tree ornament_9e24b80c-c967-446b-b162-8475722d22b8.svg'
AUTHOR = 'gpt-6'


class IconPatternedChristmasBauble(Solo48):
    icon_id = 'patterned-christmas-bauble'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('patterned', 'christmas', 'bauble')

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
        path('bauble',(24,12),[('A',(40,28),16,16,True),('A',(24,44),16,16,True),('A',(8,28),16,16,True),('A',(24,12),16,16,True)],True)
        self.add_line('string',(24,4),(24,12));self.relate('connect','string','bauble')
        self.add_polyline('zigzag',(8,28),(16,22),(24,28),(32,22),(40,28))
        self.relate('connect','zigzag','bauble')
