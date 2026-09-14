# Review candidate; original preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ac736fb4-930d-5099-ae75-efdc2b2a7f88'
SOURCE_PATH = 'pictographic-primitives/animals/snail shell_ac736fb4-930d-5099-ae75-efdc2b2a7f88.svg'
AUTHOR = 'gpt-6'

class SnailShellSpiralVariant2(Solo48):
    icon_id = 'snail-shell-spiral-v2'
    variant_of = 'snail-shell-spiral'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('snail', 'shell', 'spiral', 'swirl', 'coil', 'whorl', 'mollusc', 'curl')

    def build(self) -> None:
        """Opening repair: Rebuilt the whorl from tangent half-ellipses with wider turn spacing and exact square bounds."""
        self.add_arc('outer-upper', (6, 24), (42, 24), radius_x=18)
        self.add_arc('outer-lower', (42, 24), (16, 24), radius_x=13, radius_y=18)
        self.add_arc('middle-upper', (16, 24), (32, 24), radius_x=8, radius_y=8)
        self.add_arc('inner-lower', (32, 24), (26, 24), radius_x=3, radius_y=3)
        self.add_contour('spiral', 'outer-upper', 'outer-lower', 'middle-upper', 'inner-lower')
