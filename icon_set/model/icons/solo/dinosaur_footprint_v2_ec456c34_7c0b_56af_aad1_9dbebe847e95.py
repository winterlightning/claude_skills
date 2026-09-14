# Variant of dinosaur-footprint; parent file remains unchanged.
"""A three-toed dinosaur track with a broad rounded heel."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ec456c34-7c0b-56af-aad1-9dbebe847e95'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur footprint_ec456c34-7c0b-56af-aad1-9dbebe847e95.svg'
AUTHOR = 'gpt-6'

class DinosaurFootprintVariant2(Solo48):
    icon_id = 'dinosaur-footprint-v2'
    variant_of = 'dinosaur-footprint'
    variant_label = 'Design rules: exact bounds and open spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('dinosaur', 'footprint', 'track', 'claw', 'three-toed', 'prehistoric', 'trace', 'fossil')

    def build(self):
        # Three pointed toes and one elliptical heel, mirrored about x=24. Lucide footprints informs the simple single-contour footprint, not human toe anatomy.
        self.add_polyline('toes', (6, 28), (6, 6), (17, 20), (24, 6), (31, 20), (42, 6), (42, 28), closed=False)
        self.add_arc('heel-right', (42, 28), (24, 42), radius_x=18, radius_y=14, sweep=True)
        self.add_arc('heel-left', (24, 42), (6, 28), radius_x=18, radius_y=14, sweep=True)
        self.add_contour('track', 'toes-1', 'toes-2', 'toes-3', 'toes-4', 'toes-5', 'toes-6', 'heel-right', 'heel-left', closed=True)
