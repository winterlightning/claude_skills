"""Supermarket Building. Lucide store: facade and clear entrance. Semicircular roof feature and flag retained; roof band reduced to one line and paired doors indicated by a central seam."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd9fdb997-32f1-506d-978d-046d654ad111'
SOURCE_PATH = 'pictographic-primitives/shopping/supermarket_d9fdb997-32f1-506d-978d-046d654ad111.svg'
AUTHOR = 'gpt-6'

class SupermarketBuilding(Solo48):
    icon_id = 'supermarket-building'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('supermarket', 'building', 'store', 'entrance', 'flag', 'retail', 'shop')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42); roof cap and integral flag, mirrored entrance.
        self.add_polyline('roof',(6,24),(14,24),(24,24),(34,24),(42,24))
        self.add_arc('dome-left',(14,24),(24,14),radius_x=10)
        self.add_arc('dome-right',(24,14),(34,24),radius_x=10)
        self.add_contour('dome','dome-left','dome-right')
        self.relate('connect','roof','dome')
        self.add_polyline('flag',(24,14),(24,6),(34,6),(34,14),(24,14))
        self.relate('connect','flag','dome')
        self.add_polyline('facade',(8,24),(8,42),(24,42),(40,42),(40,24))
        self.relate('connect','facade','roof')
        self.add_line('door-seam',(24,42),(24,32))
        self.relate('connect','door-seam','facade')
