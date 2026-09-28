"""Text tool (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ba7d909-efcf-436b-aeaa-3e75eb3793f8'
SOURCE_PATH = 'pictographic-primitives/symbol/text tool_6ba7d909-efcf-436b-aeaa-3e75eb3793f8.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class TextTool(Solo48):
    icon_id = 'text-tool'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('text', 'tool', 'symbol')

    def build(self):
        self.add_line('e0', (8, 10), (8, 4))
        self.add_line('e1', (8, 4), (40, 4))
        self.add_line('e2', (40, 4), (40, 11))
        self.add_line('e3', (17, 44), (30, 44))
        self.add_line('e4', (24, 4), (24, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c1')
