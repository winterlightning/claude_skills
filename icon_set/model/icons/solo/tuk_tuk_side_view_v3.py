# Review revision; previous candidates preserved.
"""tuk-tuk-side-view: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7e4ee830-b8bf-4393-b039-d51e7de41929'
SOURCE_PATH = 'pictographic-primitives/transportation/tuk tuk_7e4ee830-b8bf-4393-b039-d51e7de41929.svg'
AUTHOR = 'gpt-6'

class TukTukSideViewVariant3(Solo48):
    icon_id = 'tuk-tuk-side-view-v3'
    variant_of = 'tuk-tuk-side-view-v2'
    variant_label = 'Review revision: clear geometry and spacing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('tuk tuk', 'auto rickshaw', 'rickshaw', 'three wheeler', 'taxi', 'asia', 'vehicle', 'side view')

    def build(self) -> None:
        self.add_polyline('roof', (4, 8), (22, 8), (28, 8))
        self.add_polyline('rear-post', (4, 8), (4, 24), (4, 36))
        self.add_polyline('front-post', (22, 8), (22, 24), (22, 36))
        self.add_line('seat', (4, 24), (22, 24))
        self.add_polyline('floor', (12, 36), (22, 36), (32, 34))
        self.add_polyline('front-frame', (28, 8), (34, 18), (38, 28))
        self.add_line('handlebar', (34, 18), (40, 18))
        for name, cx, cy, r in (('rear-wheel', 8, 36, 4), ('front-wheel', 38, 34, 6)):
            points = ((cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r))
            for i, (a, b) in enumerate(zip(points, points[1:])):
                self.add_arc(f'{name}-{i}', a, b, radius_x=r)
            self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)
        for i, a in enumerate(self.primitives):
            for b in self.primitives[i + 1:]:
                if a.start in (b.start, b.end) or a.end in (b.start, b.end):
                    self.relate('connect', a.element_id, b.element_id)
