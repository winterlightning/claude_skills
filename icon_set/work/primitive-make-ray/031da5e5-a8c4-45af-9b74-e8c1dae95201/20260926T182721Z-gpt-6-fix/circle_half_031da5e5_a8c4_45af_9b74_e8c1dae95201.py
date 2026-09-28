"""Circle half (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '031da5e5-a8c4-45af-9b74-e8c1dae95201'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__circle-half-symbol/20260926T182517Z-thuan-mac-1/reference/circle half_031da5e5-a8c4-45af-9b74-e8c1dae95201.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class CircleHalfSymbol(Solo48):
    icon_id = 'circle-half-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('circle', 'half', 'symbol')

    def build(self):
        # One exact half-ellipse and its diameter keep the left curve smooth.
        self.add_arc('semicircle', (40, 4), (40, 44), radius_x=32, radius_y=20, sweep=False)
        self.add_line('diameter', (40, 44), (40, 4))
        self.add_contour('half-circle', 'semicircle', 'diameter', closed=True)
