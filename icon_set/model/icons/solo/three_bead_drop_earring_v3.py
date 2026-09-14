# Review candidate; original preserved.
"""Three-bead drop earring with larger circular end beads and an oval central bead to preserve spacing. VRECT_S retains the vertical stack."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '591f9997-10dd-5172-97f4-64f26187164d'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/earring_591f9997-10dd-5172-97f4-64f26187164d.svg'
AUTHOR = 'gpt-6'

class ThreeBeadDropEarringVariant3(Solo48):
    icon_id = 'three-bead-drop-earring-v3'
    variant_of = 'three-bead-drop-earring-v2'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.VRECT_S
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('earring', 'bead', 'drop', 'pearl', 'jewellery', 'jewelry', 'circle', 'accessory')

    def build(self) -> None:
        """Opening repair: Replaced visually solid end-bead slivers with clean solid strokes; preserved the open central oval and links."""
        self.add_arc('main-right', (24, 17), (24, 31), radius_x=10, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('main-left', (24, 31), (24, 17), radius_x=10, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('main', 'main-right', 'main-left', closed=True)
        self.add_line('upper-link', (24, 10), (24, 17))
        self.add_line('lower-link', (24, 31), (24, 38))
        self.relate('connect', 'main', 'upper-link')
        self.relate('connect', 'main', 'lower-link')
        self.add_line('stud', (24, 6), (24, 10))
        self.add_line('drop', (24, 38), (24, 42))
        self.relate('connect', 'stud', 'upper-link')
        self.relate('connect', 'drop', 'lower-link')
