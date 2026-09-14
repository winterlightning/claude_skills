"""An upright plunger with rounded grip, shaft and domed rubber cup; collar omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dfc988bf-35dc-4e0a-9e72-5d1f118160a6'
SOURCE_PATH = 'pictographic-primitives/tools/toilet unclog_dfc988bf-35dc-4e0a-9e72-5d1f118160a6.svg'
AUTHOR = 'gpt-6'

class RubberPlunger(Solo48):
    icon_id = 'rubber-plunger'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('plunger', 'toilet', 'unclog', 'drain', 'plumbing', 'bathroom', 'suction', 'tool')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.

        def box(n, x, y, w, h, r=0):
            if not r:
                self.add_polyline(n, (x, y), (x + w, y), (x + w, y + h), (x, y + h), closed=True)
                return
            pts = [(x + r, y), (x + w - r, y), (x + w, y + r), (x + w, y + h - r), (x + w - r, y + h), (x + r, y + h), (x, y + h - r), (x, y + r)]
            for j in range(8):
                a, b = (pts[j], pts[(j + 1) % 8])
                if j % 2:
                    self.add_arc(n + str(j), a, b, radius_x=r)
                else:
                    self.add_line(n + str(j), a, b)
            self.add_contour(n, *[n + str(j) for j in range(8)], closed=True)
        box('grip', 20, 4, 8, 12, 4)
        self.add_line('shaft', (24, 16), (24, 28))
        self.relate('connect', 'shaft', 'grip')
        self.add_arc('cup-left', (8, 44), (24, 28), radius_x=16)
        self.add_arc('cup-right', (24, 28), (40, 44), radius_x=16)
        self.add_line('rim', (40, 44), (8, 44))
        self.add_contour('cup', 'cup-left', 'cup-right', 'rim', closed=True)
        self.relate('connect', 'shaft', 'cup')
