# Variant of three-bead-drop-earring; parent file remains unchanged.
"""Three-bead drop earring with larger circular end beads and an oval central bead to preserve spacing. VRECT_S retains the vertical stack."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '591f9997-10dd-5172-97f4-64f26187164d'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/earring_591f9997-10dd-5172-97f4-64f26187164d.svg'
AUTHOR = 'gpt-6'

class ThreeBeadDropEarringVariant2(Solo48):
    icon_id = 'three-bead-drop-earring-v2'
    variant_of = 'three-bead-drop-earring'
    variant_label = 'Larger end beads'
    keyshape = Keyshape.VRECT_S
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('earring', 'bead', 'drop', 'pearl', 'jewellery', 'jewelry', 'circle', 'accessory')

    def build(self) -> None:
        self.add_arc('stud-right', (24, 2), (24, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('stud-left', (24, 10), (24, 2), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('stud', 'stud-right', 'stud-left', closed=True)
        self.add_arc('main-right', (24, 17), (24, 31), radius_x=10, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('main-left', (24, 31), (24, 17), radius_x=10, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('main', 'main-right', 'main-left', closed=True)
        self.add_arc('drop-right', (24, 38), (24, 46), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('drop-left', (24, 46), (24, 38), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('drop', 'drop-right', 'drop-left', closed=True)
        self.add_line('upper-link', (24, 10), (24, 17))
        self.add_line('lower-link', (24, 31), (24, 38))
        self.relate('connect', 'stud', 'upper-link')
        self.relate('connect', 'main', 'upper-link')
        self.relate('connect', 'main', 'lower-link')
        self.relate('connect', 'drop', 'lower-link')
