"""Presentation (office): a pull-down projection screen hanging from its rail, with a ring pull.

Symbol plan: full-width rail; screen walls hang from it and round into the bottom edge; a cord on
axis x=24 drops from the screen to a ring. Keyshape: SQUARE.
Repair (2026-09-30): the ring sat 5 units under the screen (build gate internal spacing); the screen
now ends 9 above the ring, and the ring keeps a 6-unit hole.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '17f53de2-7f28-4023-80ae-484c48ce0e0e'
SOURCE_PATH = 'pictographic-primitives/office/presentation_17f53de2-7f28-4023-80ae-484c48ce0e0e.svg'
AUTHOR = 'claude-opus-5-5'

class Presentation(Solo48):
    icon_id = 'presentation'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    categories = ('office', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('presentation', 'office')

    def _circle(self, name, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r, radius_y=ry)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r, radius_y=ry)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def _path(self, name, start, parts, closed=False):
        ids = []
        p = start
        for j, s in enumerate(parts):
            i = f'{name}-{j}'
            q = s[1]
            if s[0] == 'L':
                self.add_line(i, p, q)
            else:
                self.add_arc(i, p, q, radius_x=s[2], radius_y=s[3], sweep=s[4])
            ids.append(i)
            p = q
        self.add_contour(name, *ids, closed=closed)

    def build(self):
        # Rail split where the screen walls hang from it.
        self.add_line('rail-left', (6, 6), (10, 6))
        self.add_line('rail-mid', (10, 6), (38, 6))
        self.add_line('rail-right', (38, 6), (42, 6))
        self.add_contour('rail', 'rail-left', 'rail-mid', 'rail-right')
        self._path('screen', (10, 6), [('L', (10, 19)), ('A', (14, 23), 4, 4, False), ('L', (24, 23)),
                                       ('L', (34, 23)), ('A', (38, 19), 4, 4, False), ('L', (38, 6))])
        self.relate('connect', 'screen', 'rail')
        self._circle('pull', 24, 37, 5)
        self.add_line('cord', (24, 23), (24, 32))
        self.relate('connect', 'cord', 'screen')
        self.relate('connect', 'cord', 'pull')
