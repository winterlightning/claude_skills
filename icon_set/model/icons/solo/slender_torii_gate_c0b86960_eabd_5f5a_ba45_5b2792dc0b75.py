"""Upturned eaves and spaced posts; Lucide landmark informs structural rhythm. Thin double lintels omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0b86960-eabd-5f5a-ba45-5b2792dc0b75'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/japan shrine_c0b86960-eabd-5f5a-ba45-5b2792dc0b75.svg'
AUTHOR = 'gpt-6'

class SlenderToriiGate(Solo48):
    icon_id = 'slender-torii-gate'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('torii', 'gate', 'shrine', 'japan', 'shinto', 'temple', 'landmark', 'religion')

    def build(self) -> None:
        # Centerline extremes (5, 2, 43, 46).
        self.add_arc("eave-left", (5,2), (11,5), radius_x=6, radius_y=3, sweep=False)
        self.add_line("lintel-1", (11, 5), (14, 5))
        self.add_line("lintel-2", (14, 5), (24, 5))
        self.add_line("lintel-3", (24, 5), (34, 5))
        self.add_line("lintel-4", (34, 5), (37, 5))
        self.add_arc("eave-right", (37,5), (43,2), radius_x=6, radius_y=3, sweep=False)
        self.add_contour("roof", "eave-left", "lintel-1", "lintel-2", "lintel-3", "lintel-4", "eave-right")
        self.add_polyline("beam", (9,21), (14,21), (24,21), (34,21), (39,21))
        self.add_polyline("post-left", (14,5), (14,21), (12,46))
        self.relate("connect", "roof", "post-left")
        self.relate("connect", "beam", "post-left")
        self.add_polyline("post-right", (34,5), (34,21), (36,46))
        self.relate("connect", "roof", "post-right")
        self.relate("connect", "beam", "post-right")
