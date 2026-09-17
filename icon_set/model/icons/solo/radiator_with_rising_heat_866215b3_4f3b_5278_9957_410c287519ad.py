"""Radiator with Rising Heat.

Plan: Rounded radiator with equal vertical ribs, feet and three heat waves. Bounds (6,6)-(42,42).
Construction: Source radiator repeated ribs; no useful exact local Lucide match.
Reduction: Three internal ribs replace four, heat waves reduced to coherent curves.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '866215b3-4f3b-5278-9957-410c287519ad'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/heater_866215b3-4f3b-5278-9957-410c287519ad.svg'
AUTHOR = 'gpt-6'


class IconRadiatorWithRisingHeat(Solo48):
    icon_id = 'radiator-with-rising-heat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    aliases = ()
    keywords = ('radiator', 'with', 'rising', 'heat')

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
        path('body',(10,22),[('L',(15,22)),('L',(24,22)),('L',(33,22)),('L',(38,22)),('A',(42,26),4,4,True),('L',(42,34)),('A',(38,38),4,4,True),('L',(33,38)),('L',(24,38)),('L',(15,38)),('L',(10,38)),('A',(6,34),4,4,True),('L',(6,26)),('A',(10,22),4,4,True)],True)
        for x in [15,24,33]:self.add_line('rib'+str(x),(x,22),(x,38));self.relate('connect','rib'+str(x),'body')
        for x,dx in [(10,-2),(38,2)]:self.add_line('foot'+str(x),(x,38),(x+dx,42));self.relate('connect','foot'+str(x),'body')
        for x in [12,24,36]:path('heat'+str(x),(x,6),[('C',(x,13),(x-4,8),(x+4,11))])
