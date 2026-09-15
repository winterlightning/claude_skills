'A round hand fan with a smooth circular blade and diagonal handle. SQUARE extremes (6,6)-(42,42) preserve the diagonal pose. Unequal blade lobes are replaced by consistent circular radii, split at the handle junction. No useful local Lucide hand-fan match. The handle direction is intentional.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7be3733e-dd31-5735-a409-964d8f89d37b'
SOURCE_PATH = 'pictographic-primitives/animals/ray_7be3733e-dd31-5735-a409-964d8f89d37b.svg'
AUTHOR = 'gpt-6'

class RoundHandFan(Solo48):
    icon_id = 'round-hand-fan'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/household'
    aliases = ()
    keywords = ('fan', 'hand fan', 'uchiwa', 'handle', 'cooling', 'japanese', 'round', 'paddle')

    def build(self) -> None:
        # Circular blade arcs meet at the handle attachment; integer-grid split approximates the tangent.
        # SQUARE centerlines (6,6)-(42,42), with an intentional diagonal handle.
        self.add_arc('blade-top-left', (12, 19), (29, 6), radius_x=17, sweep=True)
        self.add_arc('blade-top-right', (29, 6), (42, 19), radius_x=17, sweep=True)
        self.add_arc('blade-bottom-right', (42, 19), (29, 36), radius_x=17, sweep=True)
        self.add_arc('blade-bottom-left', (29, 36), (17, 31), radius_x=17, sweep=True)
        self.add_arc('blade-left', (17, 31), (12, 19), radius_x=17, sweep=True)
        self.add_contour('blade', 'blade-top-left', 'blade-top-right', 'blade-bottom-right', 'blade-bottom-left', 'blade-left', closed=True)
        self.add_line('handle', (6, 42), (17, 31))
        self.add_line('rib', (17, 31), (30, 18))
        self.add_contour('shaft', 'handle', 'rib')
        self.relate('connect', 'shaft', 'blade')
