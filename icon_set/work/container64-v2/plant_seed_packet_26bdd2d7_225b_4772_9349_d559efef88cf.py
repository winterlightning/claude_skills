"""Tilted torn seed packet enclosing a broad pointed leaf and its stem. Packet owns the leaf clearance; the tear retains its stepped edge. Leaf construction informed by Lucide leaf; asymmetric tilt comes from the reference.
Hosting probes using plus-sign-state-131, heart-state-63, check-mark: invalid, invalid, valid. Full content occupies the slot; see batch hosting report.
Whole subject explicitly authorized by user; preserve saved family.
Keyshape: HRECT_XL; fine source details simplified only for native readability.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (plant-seed-packet HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: vein start pulled clear of the notch.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '26bdd2d7-225b-4772-9349-d559efef88cf'
SOURCE_PATH = 'pictographic-primitives/farming/seed bag_26bdd2d7-225b-4772-9349-d559efef88cf.svg'
AUTHOR = 'claude-opus-5-5'


class Icon(Container64):
    icon_id = 'plant-seed-packet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'farming'
    categories = ('farming', 'primitives')
    aliases = ('Plant Seed Packet',)
    keywords = ('plant', 'seed', 'packet')

    def build(self) -> None:
        self.add_line('packet-1', (4, 26), (48, 10))
        self.add_line('packet-2', (48, 10), (60, 42))
        self.add_line('packet-3', (60, 42), (22, 54))
        self.add_line('packet-4', (22, 54), (19, 47))
        self.add_line('packet-5', (19, 47), (13, 49))
        self.add_line('packet-6', (13, 49), (10, 42))
        self.add_line('packet-7', (10, 42), (7, 44))
        self.add_line('packet-8', (7, 44), (4, 26))
        self.add_bezier('leaf-right', (44, 20), ((44, 33.5), (42, 42), (26, 38)))
        self.add_bezier('leaf-left', (26, 38), ((16, 32), (26, 24), (44, 20)))
        self.add_line('vein-1', (23, 41), (26, 38))
        self.add_line('vein-2', (26, 38), (34, 32))
        self.add_contour('packet', 'packet-1', 'packet-2', 'packet-3', 'packet-4', 'packet-5', 'packet-6', 'packet-7', 'packet-8', closed=True)
        self.add_contour('leaf', 'leaf-right', 'leaf-left', closed=True)
        self.add_contour('vein', 'vein-1', 'vein-2')
        self.relate('connect', 'leaf', 'vein')
