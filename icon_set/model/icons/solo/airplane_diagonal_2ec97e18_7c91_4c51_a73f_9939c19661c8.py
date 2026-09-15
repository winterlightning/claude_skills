"""Airplane. Keeps the upper-right nose, swept wings and tail fins; omits surface detail. Deliberate diagonal orientation.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide plane: one swept-wing silhouette with a rounded nose and distinct tail fins.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ec97e18-7c91-4c51-a73f-9939c19661c8'
SOURCE_PATH = 'pictographic-primitives/symbol/airplane_2ec97e18-7c91-4c51-a73f-9939c19661c8.svg'
AUTHOR = 'gpt-6'


class AirplaneDiagonal(Solo48):
    icon_id = 'airplane-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('airplane', 'plane', 'flight', 'travel', 'aircraft', 'airport', 'trip', 'aviation')

    def build(self):
        # Plan: Lucide plane: widen both wing tips and tail fins coherently; preserve the diagonal fuselage and rounded nose.

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
        path('airframe',(34,6), [('A',(42,14),8,8,True),('L',(34,24)),('L',(42,34)),('L',(34,42)),('L',(26,30)),('L',(20,36)),('L',(22,42)),('L',(12,42)),('L',(12,36)),('L',(6,34)),('L',(6,24)),('L',(14,26)),('L',(20,20)),('L',(6,12)),('L',(12,6)),('L',(26,14)),('L',(34,6))],True)
