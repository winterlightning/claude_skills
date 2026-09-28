'Apricot half: round fruit, symmetric pointed stone with smooth flanks; removed duplicate zero-length path.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22a874a8-34ca-5cfe-927b-6251ffbae66d'
SOURCE_PATH = 'pictographic-primitives/food/apricot slice_22a874a8-34ca-5cfe-927b-6251ffbae66d.svg'
AUTHOR = 'gpt-6'

class ApricotSlice(Solo48):
    icon_id = 'apricot-slice'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('apricot', 'slice', 'food')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)

        # Paired smooth seed flanks meet at top and bottom, leaving radial air around the pit.
        self.add_bezier('pit-right',(24,13),((28,16),(31,19),(31,24)),((31,29),(28,32),(24,35)))
        self.add_bezier('pit-left',(24,35),((20,32),(17,29),(17,24)),((17,19),(20,16),(24,13)))
        self.add_contour('pit','pit-right','pit-left',closed=True)
