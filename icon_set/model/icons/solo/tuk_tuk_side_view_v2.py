# Review candidate; original preserved.
"""tuk-tuk-side-view: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7e4ee830-b8bf-4393-b039-d51e7de41929'
SOURCE_PATH = 'pictographic-primitives/transportation/tuk tuk_7e4ee830-b8bf-4393-b039-d51e7de41929.svg'
AUTHOR = 'gpt-6'

class TukTukSideViewVariant2(Solo48):
    icon_id = 'tuk-tuk-side-view-v2'
    variant_of = 'tuk-tuk-side-view'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('tuk tuk', 'auto rickshaw', 'rickshaw', 'three wheeler', 'taxi', 'asia', 'vehicle', 'side view')

    def build(self) -> None:
        """Opening repair: Stopped the front fork at the wheel rim, leaving the wheel counter open."""
        self.add_polyline('roof', (6, 8), (6, 8), (22, 8), (28, 8))
        self.add_polyline('rear-post', (6, 8), (6, 24), (6, 36))
        self.add_polyline('front-post', (22, 8), (22, 24), (22, 36))
        self.add_line('seat', (6, 24), (22, 24))
        self.add_polyline('floor', (14, 36), (22, 36), (32, 34))
        self.add_polyline('front-frame', (28, 8), (34, 18), (38, 28))
        self.add_line('handlebar', (34, 18), (40, 18))
        self.add_arc('rear-top', (6, 36), (14, 36), radius_x=4)
        self.add_arc('rear-bottom', (14, 36), (6, 36), radius_x=4)
        self.add_contour('rear-wheel', 'rear-top', 'rear-bottom', closed=True)
        self.add_arc('front-tr', (38, 28), (42, 34), radius_x=6)
        self.add_arc('front-bottom', (42, 34), (32, 34), radius_x=6)
        self.add_arc('front-tl', (32, 34), (38, 28), radius_x=6)
        self.add_contour('front-wheel', 'front-tr', 'front-bottom', 'front-tl', closed=True)
        for i, a in enumerate(self.primitives):
            for b in self.primitives[i + 1:]:
                if a.start in (b.start, b.end) or a.end in (b.start, b.end):
                    self.relate('connect', a.element_id, b.element_id)
