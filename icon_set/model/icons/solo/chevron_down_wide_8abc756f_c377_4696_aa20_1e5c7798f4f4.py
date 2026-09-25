'Broad downward chevron. Shared axis x=24 and one continuous two-segment contour; HRECT_M provides widest permitted rectangular proportion. Lucide chevron-down supplies the unbroken rounded join principle; source supplies direction and symmetry. No details omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8abc756f-c377-4696-aa20-1e5c7798f4f4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/chevron down_8abc756f-c377-4696-aa20-1e5c7798f4f4.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'chevron-down-wide'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Wide Downward Chevron',)
    keywords = ('chevron', 'down', 'direction', 'angle', 'lines', 'symbol', 'navigation')
    def build(self):
        self.add_polyline('chevron',(4,10),(24,38),(44,10))
