"""A capsule pocket tool with a leaning serrated saw; fine teeth reduced to broad steps."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '35548e2e-67ff-591f-b9f4-a9495b527fac'
SOURCE_PATH = 'pictographic-primitives/tools/swiss army knife saw_35548e2e-67ff-591f-b9f4-a9495b527fac.svg'
AUTHOR = 'gpt-6'

class PocketMultitoolSawVariant2(Solo48):
    icon_id = 'pocket-multitool-saw-v2'
    variant_of = 'pocket-multitool-saw'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('swiss army knife', 'multitool', 'saw', 'pocket knife', 'camping', 'outdoor', 'blade', 'tool')

    def build(self) -> None:
        """Reduce the crowded saw teeth to two broad steps with one clear blade opening."""

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
        box('body', 6, 30, 36, 12, 6)
        self.add_polyline('saw', (32, 30), (14, 6), (6, 14), (10, 14), (10, 22), (16, 22), (16, 30))
        self.relate('connect', 'saw', 'body')
