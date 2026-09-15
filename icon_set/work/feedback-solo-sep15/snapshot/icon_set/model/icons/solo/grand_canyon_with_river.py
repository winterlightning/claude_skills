# Review candidate; original preserved.
"""A winding river separates stepped canyon walls; fine strata omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '021a0b5f-bd2d-4f08-b36b-7afe509eb0fc'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/grand canyon usa 1_021a0b5f-bd2d-4f08-b36b-7afe509eb0fc.svg'
AUTHOR = 'gpt-6'

class GrandCanyonWithRiver(Solo48):
    icon_id = 'grand-canyon-with-river'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('grand canyon', 'canyon', 'usa', 'arizona', 'river', 'cliff', 'landscape', 'nature', 'landmark')

    def build(self):
        # Plan: Broaden both cliff shoulders and use a smooth river bend; preserve the sun, distant ridge and open canyon between two cliffs.

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
        poly('left-cliff',(6,42),(6,22),(14,22),(14,30))
        poly('right-cliff',(42,42),(42,22),(34,22),(34,30))
        poly('ridge',(6,14),(14,6),(22,6),(28,12))
        path('river',(25,23), [('C',(22,35),(25,29),(23,31)),('C',(28,42),(24,38),(26,40))])
        circle('sun',39,9,3)
