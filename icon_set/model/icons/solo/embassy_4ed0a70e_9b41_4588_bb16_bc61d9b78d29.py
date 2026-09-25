"""embassy: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ed0a70e-9b41-4588-bb16-bc61d9b78d29'
SOURCE_PATH = 'pictographic-primitives/symbol/embassy_4ed0a70e-9b41-4588-bb16-bc61d9b78d29.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Embassy(Solo48):
    icon_id = 'embassy'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('embassy', 'symbol')

    def build(self):
        # Plan: HRECT_L; one symmetric elliptical dome and four equally spaced columns.
        # Reference: Geometric arch; no close embassy match.
        self.add_arc('dome',(7,24),(41,24),radius_x=17,radius_y=16)
        self.add_line('lintel',(41,24),(7,24))
        self.add_contour('roof','dome','lintel',closed=True)
        self.add_line('base',(4,40),(44,40))
        for i,x in enumerate((9,19,29,39)):
            self.add_line(f'column-{i}',(x,24),(x,40))
            self.relate('connect',f'column-{i}','roof')
            self.relate('connect',f'column-{i}','base')
