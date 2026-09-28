'A horizontal cigarette has a short filter section at the left and a narrow tip at the right. A single curling trail of smoke floats above its long body.\n\nConstruction: Wide cigarette, one continuous smoke curl; omitted narrow tip band. Centerline bounds (4,8)-(44,40).\nLucide: cigarette: rectangular body, filter divider and detached smoke.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ccd24e2a-130d-576a-bc75-21e383df8791'
SOURCE_PATH = 'pictographic-primitives/wayfinding/allowances smoking_ccd24e2a-130d-576a-bc75-21e383df8791.svg'
AUTHOR = 'gpt-6'

class SmokingCigarette(Solo48):
    icon_id = 'smoking-cigarette'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('cigarette', 'smoking', 'tobacco', 'smoke', 'filter', 'wayfinding')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('body-1', (14, 29), (44, 29))
        self.add_line('body-2', (44, 29), (44, 40))
        self.add_line('body-3', (44, 40), (14, 40))
        self.add_line('body-4', (14, 40), (4, 40))
        self.add_line('body-5', (4, 40), (4, 29))
        self.add_line('body-6', (4, 29), (14, 29))
        self.add_line('body-7', (14, 29), (14, 29))
        self.add_line('filter', (14, 29), (14, 40))
        self.add_arc('smoke-turn', (20, 8), (26, 14), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('smoke-run', (26, 14), (38, 14))
        self.add_arc('smoke-end', (38, 14), (44, 20), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_contour('smoke', 'smoke-turn', 'smoke-run', 'smoke-end', closed=False)
        self.relate('connect', 'filter', 'body')
