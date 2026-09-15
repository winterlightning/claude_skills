"""Lengthen the drill motor and shorten the exposed bit, improving their proportions; move the grip attachment with the motor and make the battery corners circular.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0893fef5-ea37-5289-a73e-db7faf9349f7'
SOURCE_PATH = 'pictographic-primitives/tools/power tools drill_0893fef5-ea37-5289-a73e-db7faf9349f7.svg'
AUTHOR = 'gpt-6'

class CordlessPowerDrill(Solo48):
    icon_id = 'cordless-power-drill-centerline-v2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('drill', 'power drill', 'cordless', 'power tool', 'battery', 'bit', 'construction', 'tool')

    def build(self) -> None:
        """Centerline review: preserve the silhouette; remove duplicated ink and split real attachments into shared nodes."""

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
        box('motor', 4, 8, 30, 14, 4)
        self.add_line('bit', (34, 15), (44, 15))
        self.relate('connect', 'bit', 'motor')
        self.add_line('grip', (14, 22), (10, 32))
        self.add_line('grip-right', (22, 32), (28, 22))
        self.relate('connect', 'grip-right', 'motor')
        self.relate('connect', 'grip-right', 'battery')
        self.relate('connect', 'grip', 'motor')
        box('battery', 6, 32, 24, 8, 4)
        self.relate('connect', 'grip', 'battery')
    variant_of = 'cordless-power-drill'
    variant_label = 'Batch 01 centerline repair'
