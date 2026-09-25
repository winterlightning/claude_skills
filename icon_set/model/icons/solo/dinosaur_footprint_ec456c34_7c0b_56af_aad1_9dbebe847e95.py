"""A three-toed dinosaur track with a broad rounded heel."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ec456c34-7c0b-56af-aad1-9dbebe847e95'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur footprint_ec456c34-7c0b-56af-aad1-9dbebe847e95.svg'
AUTHOR = 'gpt-6'

class DinosaurFootprint(Solo48):
    icon_id = 'dinosaur-footprint'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('dinosaur', 'footprint', 'track', 'claw', 'three-toed', 'prehistoric', 'trace', 'fossil')

    def build(self):
        # Three pointed toes and one elliptical heel, mirrored about x=24. Lucide footprints informs the simple single-contour footprint, not human toe anatomy.
        self.add_line('toes-1', (10, 32), (6, 10))
        self.add_line('toes-2', (6, 10), (17, 22))
        self.add_line('toes-3', (17, 22), (24, 6))
        self.add_line('toes-4', (24, 6), (31, 22))
        self.add_line('toes-5', (31, 22), (42, 10))
        self.add_line('toes-6', (42, 10), (38, 32))
        self.add_arc('heel-right', (38, 32), (24, 42), radius_x=14, radius_y=10, sweep=True)
        self.add_arc('heel-left', (24, 42), (10, 32), radius_x=14, radius_y=10, sweep=True)
        self.add_contour('track', 'toes-1', 'toes-2', 'toes-3', 'toes-4', 'toes-5', 'toes-6', 'heel-right', 'heel-left', closed=True)
