"""Three round beads and short links. VRECT_S (14,2)-(34,46) retains a vertical stack. Small top and bottom circles use the existing circular-hole exception; all three beads retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '591f9997-10dd-5172-97f4-64f26187164d'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/earring_591f9997-10dd-5172-97f4-64f26187164d.svg'
AUTHOR = 'astra-chatgpt'


class ThreeBeadDropEarring(Solo48):
    icon_id = 'three-bead-drop-earring'
    keyshape = Keyshape.VRECT_S
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('earring', 'bead', 'drop', 'pearl', 'jewellery', 'jewelry', 'circle', 'accessory')

    def build(self) -> None:
        self.add_arc('stud-right', (24, 2), (24, 8), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('stud-left', (24, 8), (24, 2), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('stud', 'stud-right', 'stud-left', closed=True)
        self.add_arc('main-right', (24, 14), (24, 34), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('main-left', (24, 34), (24, 14), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_contour('main', 'main-right', 'main-left', closed=True)
        self.add_arc('drop-right', (24, 40), (24, 46), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('drop-left', (24, 46), (24, 40), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('drop', 'drop-right', 'drop-left', closed=True)
        self.add_line('upper-link', (24, 8), (24, 14))
        self.add_line('lower-link', (24, 34), (24, 40))
        self.relate("connect", 'stud', 'upper-link')
        self.relate("connect", 'main', 'upper-link')
        self.relate("connect", 'main', 'lower-link')
        self.relate("connect", 'drop', 'lower-link')
