"""A diagonal wood saw with a rounded closed handle and circular grip aperture. Bounds (6,6)-(42,42); broad blade has two smooth tooth scallops.
Construction reference: Lucide wrench: diagonal tool balance; source waved blade and handle opening.
Omissions: Small oblong handle opening simplified to a circular aperture; fine teeth reduced to two scallops."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cca0b3cb-f738-5bd1-a400-e64072c4b7b1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wavy-tooth-wood-saw/20260927T140835Z-thuan-mac-1/reference/tools wood saw_cca0b3cb-f738-5bd1-a400-e64072c4b7b1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id='wavy-tooth-wood-saw'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases=()
    keywords=('tools', 'wood', 'saw')
    def build(self):
        # The small diamond loop is the grip opening itself. A long diagonal
        # blade and two broad teeth recover the source's saw silhouette.
        self.add_polyline('handle',(6,32),(14,24),(24,34),(16,42),closed=True)
        self.add_polyline('blade',(14,24),(36,6),(42,12),(38,16),(36,16),(36,22),(32,22),(32,28),(28,28),(24,34))
        self.relate('connect','handle','blade')
