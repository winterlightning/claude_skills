'Three left-aligned outlined capsules shorten downwards. Source supplies capsule outlines; Lucide list-filter supplies decreasing-length rhythm. VRECT_L budgets three 8-high openings separated by8, requiring40 units height. Shared left edge, radius4, pitch16; no details omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7434e69-9d9e-4d19-85db-eb9250eb7ced'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/ascending sort 2_b7434e69-9d9e-4d19-85db-eb9250eb7ced.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'three-shortening-horizontal-capsules'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ['Descending Sort Horizontal Bars']
    keywords = ['bars', 'descending', 'sort', 'horizontal', 'capsules', 'stack', 'order']
    def build(self):
        for j,width in enumerate((32,24,16)):
            top=4+16*j; left=8; right=left+width
            self.add_line(f'bar-{j}-top',(left+4,top),(right-4,top))
            self.add_arc(f'bar-{j}-right',(right-4,top),(right-4,top+8),radius_x=4)
            self.add_line(f'bar-{j}-bottom',(right-4,top+8),(left+4,top+8))
            self.add_arc(f'bar-{j}-left',(left+4,top+8),(left+4,top),radius_x=4)
            self.add_contour(f'bar-{j}',*[f'bar-{j}-{s}' for s in ('top','right','bottom','left')],closed=True)
