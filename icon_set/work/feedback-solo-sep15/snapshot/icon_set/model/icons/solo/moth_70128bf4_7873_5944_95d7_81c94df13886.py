"""Symmetric moth with small domed head and broad swept wings tapering into an abdomen. Thin source legs and antennae omitted to favor the characteristic wing silhouette. Lucide heart informs mirrored lobes; no useful moth match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70128bf4-7873-5944-95d7-81c94df13886'
SOURCE_PATH = 'pictographic-primitives/animals/moth_70128bf4-7873-5944-95d7-81c94df13886.svg'
AUTHOR = 'gpt-6'


class Moth(Solo48):
    icon_id = 'moth'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('moth', 'animal')

    def build(self) -> None:
        # HRECT_XL: authored to its exact SOLO48 centerline bounds.
        self.add_bezier('head-top', (18, 12), *(((18.42928338, 8.52884098), (20.99406902, 6), (24, 6)),))
        self.add_bezier('head-right', (24, 6), *(((27.00593098, 6), (29.57071662, 8.52884098), (30, 12)),))
        self.add_contour('head', 'head-top', 'head-right', closed=False)
        self.add_line('wing-left-leading', (18, 12), (6, 30))
        self.add_bezier('wing-left-tip', (6, 30), *(((6, 32.47520861), (6, 35.52479139), (6, 38)),))
        self.add_arc('wing-left-bottom', (6, 38), (12, 42), radius_x=10, radius_y=5, sweep=False)
        self.add_arc('wing-left-inner', (12, 42), (24, 29), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('wing-right-inner', (24, 29), (36, 42), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('wing-right-bottom', (36, 42), (42, 38), radius_x=10, radius_y=5, sweep=False)
        self.add_bezier('wing-right-tip', (42, 38), *(((42, 35.52479139), (42, 32.47520861), (42, 30)),))
        self.add_line('wing-right-leading', (42, 30), (30, 12))
        self.add_contour('wings', 'wing-left-leading', 'wing-left-tip', 'wing-left-bottom', 'wing-left-inner', 'wing-right-inner', 'wing-right-bottom', 'wing-right-tip', 'wing-right-leading', closed=False)
        self.relate("connect", 'head', 'wings')
