"""Upturned eaves and spaced posts; Lucide landmark informs structural rhythm. Thin double lintels omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e270bb6-b63a-450c-ba07-cb7c4cbeafd3'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/japan shrine_1e270bb6-b63a-450c-ba07-cb7c4cbeafd3.svg'
AUTHOR = 'gpt-6'

class ToriiGate(Solo48):
    icon_id = 'torii-gate'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('torii', 'gate', 'shrine', 'japan', 'shinto', 'temple', 'landmark', 'religion')

    def build(self) -> None:
        # Centerline extremes (2, 5, 46, 43).
        self.add_arc("eave-left", (2,5), (8,8), radius_x=6, radius_y=3, sweep=False)
        self.add_line("lintel-1", (8, 8), (12, 8))
        self.add_line("lintel-2", (12, 8), (24, 8))
        self.add_line("lintel-3", (24, 8), (36, 8))
        self.add_line("lintel-4", (36, 8), (40, 8))
        self.add_arc("eave-right", (40,8), (46,5), radius_x=6, radius_y=3, sweep=False)
        self.add_contour("roof", "eave-left", "lintel-1", "lintel-2", "lintel-3", "lintel-4", "eave-right")
        self.add_polyline("beam", (6,20), (12,20), (24,20), (36,20), (42,20))
        self.add_polyline("post-left", (12,8), (12,20), (10,43))
        self.relate("connect", "roof", "post-left")
        self.relate("connect", "beam", "post-left")
        self.add_polyline("post-right", (36,8), (36,20), (38,43))
        self.relate("connect", "roof", "post-right")
        self.relate("connect", "beam", "post-right")
        self.add_line("tie", (24,8), (24,20))
        self.relate("connect", "tie", "roof")
        self.relate("connect", "tie", "beam")
