"""Sun Rising over Mosque.

Plan: Onion dome between two minarets with sunrise above. Bounds (6,6)-(42,42).
Construction: Source mosque, Lucide sunrise uses open solar arc and detached rays.
Reduction: Minarets use single strokes, two ray marks, no tiny windows or horizontal dome band.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '5cd0e8a5-7585-4019-97b2-78a1e50f66d3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/islamic new year_5cd0e8a5-7585-4019-97b2-78a1e50f66d3.svg'
AUTHOR = 'gpt-6'


class IconSunRisingOverMosque(Solo48):
    icon_id = 'sun-rising-over-mosque'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('sun', 'rising', 'over', 'mosque')

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
        path('mosque',(16,42),[('L',(16,33)),('C',(24,22),(12,28),(22,26)),('C',(32,33),(26,26),(36,28)),('L',(32,42)),('L',(16,42))],True)
        for x in [6,42]:self.add_line('minaret'+str(x),(x,28),(x,42))
        path('sun',(16,14),[('A',(32,14),8,8,True)])
        self.add_line('ray-left',(6,14),(6,14));self.add_line('ray-right',(42,14),(42,14))
