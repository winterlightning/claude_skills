"""Tilted torn seed packet enclosing a broad pointed leaf and its stem. Packet owns the leaf clearance; the tear retains its stepped edge. Leaf construction informed by Lucide leaf; asymmetric tilt comes from the reference.
Hosting probes using plus-sign-state-131, heart-state-63, check-mark: invalid, invalid, valid. Full content occupies the slot; see batch hosting report.
Whole subject explicitly authorized by user; preserve saved family.
Keyshape: HRECT_XL; fine source details simplified only for native readability.
"""
from ._base import Container64
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '26bdd2d7-225b-4772-9349-d559efef88cf'
SOURCE_PATH = 'pictographic-primitives/farming/seed bag_26bdd2d7-225b-4772-9349-d559efef88cf.svg'
AUTHOR = "gpt-6"

class Icon(Container64):
    icon_id = 'plant-seed-packet'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'farming'
    aliases = ('Plant Seed Packet',)
    keywords = ('plant', 'seed', 'packet')
    def build(self):
        self.add_polyline("packet", (2,24),(48,6),(62,44),(22,58),(19,50),(13,52),(10,44),(6,46),closed=True)
        self.add_bezier("leaf-right", (44,18), ((44,34),(42,44),(26,40)))
        self.add_bezier("leaf-left", (26,40), ((16,32),(26,22),(44,18)))
        self.add_contour("leaf","leaf-right","leaf-left",closed=True)
        self.add_polyline("vein",(22,44),(26,40),(34,32))
        self.relate("connect","leaf","vein")
