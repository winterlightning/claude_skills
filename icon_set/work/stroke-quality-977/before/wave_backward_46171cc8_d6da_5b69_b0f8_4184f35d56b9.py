"""Wave backward (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46171cc8-d6da-5b69-b0f8-4184f35d56b9'
SOURCE_PATH = 'pictographic-primitives/interface-essential/wave backward_46171cc8-d6da-5b69-b0f8-4184f35d56b9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class WaveBackward(Solo48):
    icon_id = 'wave-backward'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('wave', 'backward', 'interface-essential')

    def build(self):
        self.add_bezier('sym-e0', (22, 4), ((13.804, 9.145), (8, 16.236), (8, 23)))
        self.add_bezier('sym-e1', (8, 23), ((8, 23.2), (8, 23.8), (8, 24)))
        self.add_bezier('sym-e2', (8, 24), ((8, 24.164), (8, 23.836), (8, 24)))
        self.add_bezier('sym-e3', (8, 24), ((8, 24.164), (8, 23.836), (8, 24)))
        self.add_bezier('sym-e4', (8, 24), ((8, 24.2), (8, 24.8), (8, 25)))
        self.add_bezier('sym-e5', (8, 25), ((8, 31.764), (13.804, 38.855), (22, 44)))
        self.add_bezier('sym-e6', (30, 24), ((30, 19.177), (33.249, 13.988), (40, 10)))
        self.add_bezier('sym-e7', (30, 24), ((30, 28.823), (33.249, 34.012), (40, 38)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7')
        self.relate('connect', 'sym-c1', 'sym-c2')
