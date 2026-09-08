"""Minoan palace: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '194f3651-4280-5fce-8d9a-c4d0aaa5c514'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/minoan palace_194f3651-4280-5fce-8d9a-c4d0aaa5c514.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'minoan-palace'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('minoan', 'palace', 'knossos', 'crete', 'greece', 'ancient', 'columns', 'ruins', 'heritage')

    def build(self):
        # Centerline extremes: (2,5)-(46,43); raised columned hall.
        self.add_polyline("roof", (2,13), (24,5), (46,13))
        self.add_polyline("hall", (2,13), (2,29), (12,29), (20,29), (28,29), (36,29), (46,29), (46,13))
        self.add_polyline("base", (2,43), (12,43), (20,43), (28,43), (36,43), (46,43))
        for x in (12,20,28,36):
            self.add_line(f"column-{x}", (x,29), (x,43))
            self.relate("connect", f"column-{x}", "hall")
            self.relate("connect", f"column-{x}", "base")
        self.add_line("window-left", (17,20), (17,22))
        self.add_line("window-right", (31,20), (31,22))
        self.relate("connect", "roof", "hall")
