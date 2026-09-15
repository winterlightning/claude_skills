"""A diamond-topped mountain with a jagged snow line near its peak melts into dripping wavy layers that narrow to a rounded base.

Plan: Symmetric mountain peak and broad ink-drop base, attached snow zigzag.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: mountain: deliberate angular summit; flower-2: coherent rounded contour.
Simplification: Multiple ink ripples reduce to one broad flowing drop.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '284bd116-a688-437f-8349-e9b0799bf5bb'
SOURCE_PATH = 'pictographic-primitives/logos/inkscape logo_284bd116-a688-437f-8349-e9b0799bf5bb.svg'
AUTHOR = 'gpt-6'


class InkscapeLogo(Solo48):
    icon_id = 'inkscape-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('inkscape', 'vector', 'drawing', 'logo', 'brand', 'open-source', 'mountain')

    def build(self):
        # Plan: Keep the peaked mountain and ink-shaped base, using coherent curves and a smaller detached snow chevron with room on every side.

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
        poly('peak',(6,24),(24,6),(42,24))
        path('base',(42,24), [('C',(32,36),(42,36),(34,30)),('A',(16,36),8,6,True),('C',(6,24),(14,30),(6,36))]);join('base','peak')
        poly('snow',(18,24),(24,18),(30,24))
