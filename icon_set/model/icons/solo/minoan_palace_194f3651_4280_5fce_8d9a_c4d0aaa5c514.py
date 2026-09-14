"""Minoan palace: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '194f3651-4280-5fce-8d9a-c4d0aaa5c514'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/minoan palace_194f3651-4280-5fce-8d9a-c4d0aaa5c514.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'minoan-palace'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('minoan', 'palace', 'knossos', 'crete', 'greece', 'ancient', 'columns', 'ruins', 'heritage')

    def build(self):
        # HRECT_L centerline extremes (6,8)-(42,40).
        # Building owns silhouette and attached architecture; repeat pairs share axes.
        self.add_polyline("roof", (6,16), (24,8), (42,16))
        self.add_polyline("hall", (6,16), (6,28), (12,28), (24,28), (36,28), (42,28), (42,16))
        self.add_polyline("base", (6,40), (12,40), (24,40), (36,40), (42,40))
        for x in (12,24,36):
            self.add_line(f"column-{x}", (x,28), (x,40))
            self.relate("connect", f"column-{x}", "hall")
            self.relate("connect", f"column-{x}", "base")
        for x in (17,31):
            self.add_dot(f"window-{x}", (x,20))
        self.relate("connect", "roof", "hall")
