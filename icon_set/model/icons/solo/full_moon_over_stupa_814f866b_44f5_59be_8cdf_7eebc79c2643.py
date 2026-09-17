"""Full Moon over Stupa.

Plan: Moon upper left; domed stupa lower right with triangular axial spire. Bounds (6,6)-(42,42).
Construction: Source scene; Lucide circular construction for moon.
Reduction: Removed crater, extra tower tiers and door to allocate clear moon/shrine spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '814f866b-44f5-59be-8cdf-7eebc79c2643'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/poya day fullmoon_814f866b-44f5-59be-8cdf-7eebc79c2643.svg'
AUTHOR = 'gpt-6'


class FullMoonOverStupa(Solo48):
    icon_id = 'full-moon-over-stupa'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('full', 'moon', 'over', 'stupa')

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
        circle('moon',12,12,6)
        path('dome',(22,42),[('A',(32,28),10,14,True),('A',(42,42),10,14,True),('L',(22,42))],True)
        self.add_polyline('spire',(32,6),(40,20),(32,20),(24,20),closed=True)
        self.add_line('tower',(32,20),(32,28))
        self.relate('connect','tower','spire');self.relate('connect','tower','dome')
