# Review revision; previous candidates preserved.
"""The Leaning Tower of Pisa with sloping floor bands; the doorway and upper mast are omitted for clear spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9a3f8c8c-6f0b-50d0-bd62-91718e949e17'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/pisa tower_9a3f8c8c-6f0b-50d0-bd62-91718e949e17.svg'
AUTHOR = 'gpt-6'

class LeaningTowerOfPisa(Solo48):
    icon_id = 'leaning-tower-of-pisa'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('pisa', 'tower', 'italy', 'leaning', 'landmark', 'campanile', 'travel', 'architecture')

    def build(self):
        # Plan: One tilted shaft owns parallel floor stations; reduce four cramped storeys to three wider bands while preserving the lean and ground line.

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
        poly('shaft',(19,6),(35,10),(32,22),(30,30),(27,42),(10,42),(14,26),(16,18),closed=True)
        poly('ground',(6,42),(10,42),(27,42),(42,42));join('ground','shaft')
