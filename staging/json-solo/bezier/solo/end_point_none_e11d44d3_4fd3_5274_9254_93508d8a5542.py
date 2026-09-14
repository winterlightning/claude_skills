"""End point none (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e11d44d3-4fd3-5274-9254-93508d8a5542'
SOURCE_PATH = 'icons-json/design/end point none_e11d44d3-4fd3-5274-9254-93508d8a5542.json'
AUTHOR = 'json_to_solo'

class EndPointNoneDesign(Solo48):
    icon_id = 'end-point-none-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('end', 'point', 'none', 'design')

    def build(self):
        self.add_line('e0', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
