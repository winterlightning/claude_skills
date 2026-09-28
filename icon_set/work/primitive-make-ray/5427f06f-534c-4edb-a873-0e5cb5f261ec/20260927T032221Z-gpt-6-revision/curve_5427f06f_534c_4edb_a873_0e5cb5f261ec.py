"""One smooth rising quarter curve, reconstructed from the diagram reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5427f06f-534c-4edb-a873-0e5cb5f261ec'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curve/20260927T032022Z-thuan-mac-1/reference/curve_5427f06f-534c-4edb-a873-0e5cb5f261ec.svg'
AUTHOR = "gpt-6"

class Curve(Solo48):
    icon_id = 'curve'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    categories = ('diagrams', 'primitives')
    aliases = ()
    keywords = ('curve', 'diagrams')

    def build(self):
        # One continuous quarter arc preserves the reference's smooth rise.
        self.add_arc('rising-curve', (6, 42), (42, 6), radius_x=36, sweep=True)
