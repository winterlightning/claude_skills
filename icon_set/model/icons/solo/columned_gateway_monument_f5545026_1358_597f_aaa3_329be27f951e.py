"""Columned gateway monument: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5545026-1358-597f-aaa3-329be27f951e'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/brandenburg gate berlin_f5545026-1358-597f-aaa3-329be27f951e.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'columned-gateway-monument'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('gate', 'gateway', 'monument', 'brandenburg', 'berlin', 'landmark', 'arch', 'columns', 'architecture')

    def build(self):
        # Centerline extremes: (2,2)-(46,46).
        self.add_polyline("outline", (2,18), (14,18), (34,18), (46,18), (46,46), (36,46), (36,28), (12,28), (12,46), (2,46), closed=True)
        self.add_polyline("attic", (14,18), (14,10), (24,10), (34,10), (34,18))
        self.relate("connect", "attic", "outline")
        self.add_polyline("mast", (24,2), (24,5), (24,10))
        self.add_polyline("cross", (19,5), (24,5), (29,5))
        self.relate("connect", "mast", "cross")
        self.relate("connect", "mast", "attic")
        self.add_line("lintel-left", (2,28), (12,28))
        self.add_line("lintel-right", (36,28), (46,28))
        self.relate("connect", "lintel-left", "outline")
        self.relate("connect", "lintel-right", "outline")
