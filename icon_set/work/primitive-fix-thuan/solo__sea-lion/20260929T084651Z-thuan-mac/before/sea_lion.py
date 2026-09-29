# Review revision; previous candidates preserved.
"""sea-lion: HRECT_XL ink (6,6)-(42,42). Left-facing raised head, sweeping back and splayed flippers."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7188aa8a-305f-404d-bfe3-07ee8f265206'
SOURCE_PATH = 'pictographic-primitives/animals/seal body_7188aa8a-305f-404d-bfe3-07ee8f265206.svg'
AUTHOR = 'gpt-6'

class SeaLion(Solo48):
    icon_id = 'sea-lion'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('sea lion', 'seal', 'flippers', 'marine', 'animal', 'ocean', 'zoo', 'whiskers')

    def build(self):
        # Plan: Trace the sitting sea lion with a long neck and broad smooth haunch. Widen both flippers and remove the redundant cramped flipper mark.

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
        path('body',(16,6), [('A',(28,16),12,10,True),('L',(28,22)),('L',(30,22)),('A',(42,34),12,12,True),('L',(42,40)),('A',(40,42),2,2,True),('L',(32,42)),('L',(34,34)),('L',(30,32)),('A',(24,34),12,6,True),('L',(24,42)),('C',(16,38),(20,42),(16,42)),('L',(10,40)),('L',(6,38)),('L',(10,30)),('A',(8,24),14,14,True),('L',(6,18)),('L',(10,16)),('L',(6,14)),('A',(16,6),10,8,True)],True)
        self.add_dot('eye',(19,15))
