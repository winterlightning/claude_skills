"""Three-Light Ceiling Fixture. SQUARE centerlines (6,6)-(42,42): three heads spread across a shared canopy. Reduce the canopy to its bar and the bell flares to tapered outlines; preserve the outward angles.
Lucide lamp-ceiling / lamp-floor inform simple shades and explicit support joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f22a8a30-790b-4725-b4c1-de88b2abc933'
SOURCE_PATH = 'pictographic-primitives/lamps/lamp three_f22a8a30-790b-4725-b4c1-de88b2abc933.svg'
AUTHOR = 'gpt-6'


class ThreeLightCeilingFixture(Solo48):
    icon_id = 'three-light-ceiling-fixture'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'lamps'
    categories = ('lamps', 'primitives')
    aliases = ()
    keywords = ('lamp', 'ceiling', 'fixture', 'spotlight', 'three', 'lighting')

    def build(self):
        # Plan: Three broad trapezoidal lamp shades share one canopy and equal cord stations. Stagger heights to separate shades; omit the short top cord.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        poly('canopy',(10,8),(24,8),(38,8))
        for j,(x,t,b) in enumerate(((10,16,24),(24,32,40),(38,16,24))):
         line(f'cord-{j}',(x,8),(x,t));join(f'cord-{j}','canopy')
         poly(f'shade-{j}',(x-4,t),(x,t),(x+4,t),(x+6,b),(x-6,b),closed=True);join(f'cord-{j}',f'shade-{j}')
