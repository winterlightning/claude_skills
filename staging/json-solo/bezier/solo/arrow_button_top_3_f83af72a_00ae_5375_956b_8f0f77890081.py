"""Arrow button top 3 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f83af72a-00ae-5375-956b-8f0f77890081'
SOURCE_PATH = 'icons-json/arrows/arrow button top 3_f83af72a-00ae-5375-956b-8f0f77890081.json'
AUTHOR = 'json_to_solo'

class ArrowButtonTop3Arrows(Solo48):
    icon_id = 'arrow-button-top-3-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'button', 'top', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 8), (24, 8))
        self.add_bezier('sym-e1', (24, 8), ((22.776, 8), (21.738, 9.275), (21, 10)))
        self.add_line('sym-e2', (21, 10), (5, 26))
        self.add_bezier('sym-e3', (5, 26), ((4.573, 26.413), (4, 26.402), (4, 27)))
        self.add_bezier('sym-e4', (4, 27), ((4, 27.059), (4, 27.941), (4, 28)))
        self.add_bezier('sym-e5', (4, 28), ((4, 28.505), (4, 28.495), (4, 29)))
        self.add_line('sym-e6', (4, 29), (4, 40))
        self.add_line('sym-e7', (4, 40), (23, 21))
        self.add_bezier('sym-e8', (23, 21), ((23.308, 20.702), (23.698, 21), (24, 21)))
        self.add_bezier('sym-e9', (24, 21), ((24.302, 21), (24.692, 20.702), (25, 21)))
        self.add_line('sym-e10', (25, 21), (44, 40))
        self.add_line('sym-e11', (44, 40), (44, 29))
        self.add_bezier('sym-e12', (44, 29), ((44, 28.495), (44, 28.505), (44, 28)))
        self.add_bezier('sym-e13', (44, 28), ((44, 27.941), (44, 27.059), (44, 27)))
        self.add_bezier('sym-e14', (44, 27), ((44, 26.402), (43.427, 26.413), (43, 26)))
        self.add_line('sym-e15', (43, 26), (27, 10))
        self.add_bezier('sym-e16', (27, 10), ((26.262, 9.275), (25.224, 8), (24, 8)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)
