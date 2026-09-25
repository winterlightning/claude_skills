"""Embassy Building. Retains the identifying silhouette and visible features.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide building-2: tall main block, smaller annex and simple window marks; source specifies the right sloping annex.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd29397ed-5128-4fea-aca9-6d520b50eaf4'
SOURCE_PATH = 'pictographic-primitives/symbol/embassy_d29397ed-5128-4fea-aca9-6d520b50eaf4.svg'
AUTHOR = 'gpt-6'


class EmbassyBuilding(Solo48):
    icon_id = 'embassy-building'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('embassy', 'building', 'office', 'government', 'consulate', 'city', 'architecture', 'tower')

    def build(self) -> None:
        self.add_polyline('tower', (10, 42), (10, 6), (32, 6), (32, 20), (32, 42))
        self.add_polyline('ground', (6, 42), (10, 42), (32, 42), (42, 42))
        self.add_polyline('annex', (32, 20), (42, 26), (42, 42))
        self.relate("connect", 'tower', 'ground')
        self.relate("connect", 'tower', 'annex')
        self.relate("connect", 'ground', 'annex')
        self.add_line('window-one', (18, 20), (24, 20))
        self.add_line('window-two', (18, 30), (24, 30))
