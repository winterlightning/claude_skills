"""Pumpkin.

Plan: Mirrored pumpkin lobes around axis24 and bent stem; centerlines (6,6)-(42,42).
Construction: Source lobed pumpkin; no useful exact Lucide pumpkin.
Reduction: Retained central seam, omitted secondary lobe seams to preserve spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '7a3a8b0a-72cc-50fc-8d70-d02028b9db8a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/pumpkin_7a3a8b0a-72cc-50fc-8d70-d02028b9db8a.svg'
AUTHOR = 'gpt-6'


class IconPumpkin(Solo48):
    icon_id = 'pumpkin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('pumpkin',)

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
        path('pumpkin',(24,12),[('C',(42,27),(38,8),(42,16)),('C',(24,42),(42,38),(35,42)),('C',(6,27),(13,42),(6,38)),('C',(24,12),(6,16),(10,8))],True)
        path('stem',(24,12),[('C',(30,6),(24,8),(26,6))]);self.relate('connect','stem','pumpkin')
        self.add_line('seam',(24,12),(24,42));self.relate('connect','seam','pumpkin');self.relate('connect','seam','stem')
