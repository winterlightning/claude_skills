"""End point none (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e11d44d3-4fd3-5274-9254-93508d8a5542'
SOURCE_PATH = 'pictographic-primitives/design/end point none_e11d44d3-4fd3-5274-9254-93508d8a5542.svg'
AUTHOR = 'gpt-6'

class EndPointNone(Solo48):
    icon_id = 'end-point-none'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('end', 'point', 'none', 'design')

    def build(self):
        self.add_line('e0', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
