"""Web form radio button (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a1e482d-90ce-5a26-9c57-00d6c73669c1'
SOURCE_PATH = 'pictographic-primitives/interface-essential/web form radio button_4a1e482d-90ce-5a26-9c57-00d6c73669c1.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class WebFormRadioButton(Solo48):
    icon_id = 'web-form-radio-button'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('web', 'form', 'radio', 'button', 'interface-essential')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-top', (16, 24), (32, 24), radius_x=8)
        self.add_arc('e1-bottom', (32, 24), (16, 24), radius_x=8)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
