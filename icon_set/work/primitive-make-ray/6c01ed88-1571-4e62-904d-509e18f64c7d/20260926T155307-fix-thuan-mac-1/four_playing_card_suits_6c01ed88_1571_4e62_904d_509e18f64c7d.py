"""Four card suits in a two-by-two grid: diamond, club, spade and heart.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: one suit per 14-unit cell, 8 apart. Diamond, club and spade
keep the parent's outlines and stems. The heart is rebuilt with the
library's heart construction (the `hand-holding-heart` heart at r3): two r3
lobe semicircles meeting in a notch at (35,31), r5 shoulders, and straight
sides to the tip at (35,42), mirrored about x=35.
Revision: the rejected heart had no top notch and read as a shield
(feedback: "heart"); the notched two-lobe heart now reads.
Reduction: fine lobe curvature simplified to circular/elliptical arcs.
Construction reference: Lucide `heart` (two lobes into a point).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6c01ed88-1571-4e62-904d-509e18f64c7d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__four-playing-card-suits/20260926T152509Z-thuan-mac-1/reference/card game symbols_6c01ed88-1571-4e62-904d-509e18f64c7d.svg'
AUTHOR = "claude-opus-5-5"

class Drawing(Solo48):
    icon_id='four-playing-card-suits'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=('card game symbols',)
    keywords=('playing', 'card', 'suits', 'poker', 'casino', 'heart', 'spade', 'club', 'diamond')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start;members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
                else:self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m);here=end
            self.add_contour(name,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        poly('diamond',(13,6),(20,13),(13,20),(6,13),closed=True)
        path('club',(32,10),[('A',(38,10),3,4,True),('A',(42,15),4,5,True),('A',(35,17),4,4,True),('A',(28,15),4,4,True),('A',(32,10),4,5,True)],True)
        line('club-stem',(35,17),(35,20));join('club-stem','club')
        path('spade',(13,29),[('L',(7,35)),('A',(13,38),4,4,False),('A',(19,35),4,4,False),('L',(13,29))],True)
        line('spade-stem',(13,38),(13,42));join('spade-stem','spade')
        # heart: library heart construction at r3, axis x=35
        cx, y, r, tip = 35, 31, 3, 42
        path('heart', (cx, y), [('A', (cx - 2 * r, y), r, r, False), ('A', (cx - 2 * r + 2, y + 4), 5, 5, False),
                                ('L', (cx, tip)), ('L', (cx + 2 * r - 2, y + 4)),
                                ('A', (cx + 2 * r, y), 5, 5, False), ('A', (cx, y), r, r, False)], True)
