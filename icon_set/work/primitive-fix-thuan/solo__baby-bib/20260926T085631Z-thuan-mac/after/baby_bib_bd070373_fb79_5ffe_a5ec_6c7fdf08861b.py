from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bd070373-fb79-5ffe-a5ec-6c7fdf08861b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__baby-bib/20260926T085631Z-thuan-mac/reference/baby care bib_bd070373-fb79-5ffe-a5ec-6c7fdf08861b.svg'
AUTHOR = 'claude-opus-5-5'

class BabyBib(Solo48):
    icon_id = 'baby-bib'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "babies"
    categories = ("babies", "primitives")
    aliases = ()
    keywords = ('bib', 'baby', 'feeding', 'infant', 'mealtime', 'childcare', 'bear', 'apron')

    # Designed to centerline extremes (6, 6)–(42, 42).
    def build(self) -> None:
        # Plan: one closed bib outline, mirrored about x=24. The body below y=24 is a
        # true r18 circle about (24,24); the shoulders are quarter ellipses
        # (centre (16|32,24), rx10 ry18) that meet the circle with vertical
        # tangents at (6,24)/(42,24), so the sides stay wide and smooth.
        self.add_arc('bib-1', (16, 6), (6, 24), radius_x=10, radius_y=18, sweep=False)
        self.add_arc('bib-2', (6, 24), (24, 42), radius_x=18, radius_y=18, sweep=False)
        self.add_arc('bib-3', (24, 42), (42, 24), radius_x=18, radius_y=18, sweep=False)
        self.add_arc('bib-4', (42, 24), (32, 6), radius_x=10, radius_y=18, sweep=False)
        self.add_arc('bib-5', (32, 6), (35, 12), radius_x=6, radius_y=7, sweep=True)
        self.add_arc('bib-6', (35, 12), (13, 12), radius_x=11, radius_y=9, sweep=True)
        self.add_arc('bib-7', (13, 12), (16, 6), radius_x=6, radius_y=7, sweep=True)
        self.add_contour('bib', 'bib-1', 'bib-2', 'bib-3', 'bib-4', 'bib-5', 'bib-6', 'bib-7', closed=True)
