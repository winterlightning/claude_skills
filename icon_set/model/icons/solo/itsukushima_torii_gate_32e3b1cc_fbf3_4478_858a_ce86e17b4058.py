"""Upturned eaves and spaced posts; Lucide landmark informs structural rhythm. Thin double lintels omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32e3b1cc-fbf3-4478-858a-ce86e17b4058'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/shrine of itsukushima_32e3b1cc-fbf3-4478-858a-ce86e17b4058.svg'
AUTHOR = 'gpt-6'

class ItsukushimaToriiGate(Solo48):
    icon_id = 'itsukushima-torii-gate'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('itsukushima', 'torii', 'gate', 'shrine', 'japan', 'shinto', 'miyajima', 'landmark')

    def build(self) -> None:
        # Centerline extremes (2, 8, 46, 40).
        self.add_arc("eave-left", (2,8), (8,11), radius_x=6, radius_y=3, sweep=False)
        self.add_line("lintel-1", (8, 11), (10, 11))
        self.add_line("lintel-2", (10, 11), (24, 11))
        self.add_line("lintel-3", (24, 11), (38, 11))
        self.add_line("lintel-4", (38, 11), (40, 11))
        self.add_arc("eave-right", (40,11), (46,8), radius_x=6, radius_y=3, sweep=False)
        self.add_contour("roof", "eave-left", "lintel-1", "lintel-2", "lintel-3", "lintel-4", "eave-right")
        self.add_polyline("beam", (6,21), (10,21), (18,21), (30,21), (38,21), (42,21))
        self.add_polyline("post-left", (10,11), (10,21), (10,40))
        self.relate("connect", "roof", "post-left")
        self.relate("connect", "beam", "post-left")
        self.add_polyline("post-right", (38,11), (38,21), (38,40))
        self.relate("connect", "roof", "post-right")
        self.relate("connect", "beam", "post-right")
        self.add_line("aux-18", (18,21), (18,40))
        self.relate("connect", "beam", "aux-18")
        self.add_line("aux-30", (30,21), (30,40))
        self.relate("connect", "beam", "aux-30")
