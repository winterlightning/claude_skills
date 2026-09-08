"""Symmetric moth with small domed head and broad swept wings tapering into an abdomen. Thin source legs and antennae omitted to favor the characteristic wing silhouette. Lucide heart informs mirrored lobes; no useful moth match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70128bf4-7873-5944-95d7-81c94df13886'
SOURCE_PATH = 'pictographic-primitives/animals/moth_70128bf4-7873-5944-95d7-81c94df13886.svg'
AUTHOR = 'gpt-6'


class Moth(Solo48):
    icon_id = 'moth'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('moth', 'animal')

    def build(self) -> None:
        # HRECT_XL: authored to its exact SOLO48 centerline bounds.
        self.add_arc('head-top', (18, 12), (24, 5), radius_x=6, radius_y=7, sweep=True)
        self.add_arc('head-right', (24, 5), (30, 12), radius_x=6, radius_y=7, sweep=True)
        self.add_contour('head', 'head-top', 'head-right', closed=False)
        self.add_line('wing-left-leading', (18, 12), (5, 30))
        self.add_arc('wing-left-tip', (5, 30), (2, 38), radius_x=3, radius_y=8, sweep=False)
        self.add_arc('wing-left-bottom', (2, 38), (12, 43), radius_x=10, radius_y=5, sweep=False)
        self.add_arc('wing-left-inner', (12, 43), (24, 29), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('wing-right-inner', (24, 29), (36, 43), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('wing-right-bottom', (36, 43), (46, 38), radius_x=10, radius_y=5, sweep=False)
        self.add_arc('wing-right-tip', (46, 38), (43, 30), radius_x=3, radius_y=8, sweep=False)
        self.add_line('wing-right-leading', (43, 30), (30, 12))
        self.add_contour('wings', 'wing-left-leading', 'wing-left-tip', 'wing-left-bottom', 'wing-left-inner', 'wing-right-inner', 'wing-right-bottom', 'wing-right-tip', 'wing-right-leading', closed=False)
        self.relate("connect", 'head', 'wings')
