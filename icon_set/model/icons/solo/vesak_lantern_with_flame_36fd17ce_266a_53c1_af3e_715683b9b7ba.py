"""Vesak Lantern with Flame.

Plan: Diamond lantern with short suspension and two tails around flame. Bounds (6,6)-(42,42).
Construction: Source Vesak lantern and Lucide flame simple pointed contour.
Reduction: Wide truncated diamond preserves flame clearance; collars reduced to edges and two separate tails.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '36fd17ce-266a-53c1-af3e-715683b9b7ba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/vesak lantern_36fd17ce-266a-53c1-af3e-715683b9b7ba.svg'
AUTHOR = 'gpt-6'


class IconVesakLanternWithFlame(Solo48):
    icon_id = 'vesak-lantern-with-flame'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('vesak', 'lantern', 'with', 'flame')

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
        path('lantern',(16,10),[('L',(24,10)),('L',(32,10)),('L',(42,24)),('L',(32,38)),('L',(16,38)),('L',(6,24)),('L',(16,10))],True)
        self.add_line('suspend',(24,6),(24,10));self.relate('connect','suspend','lantern')
        for x in [16,32]:self.add_line('tail'+str(x),(x,38),(x,42));self.relate('connect','tail'+str(x),'lantern')
        path('flame',(24,19),[('C',(28,24),(26,21),(28,22)),('A',(20,24),4,4,True),('C',(24,19),(20,22),(22,21))],True)
