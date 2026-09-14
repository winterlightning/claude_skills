"""Arrow button right 3 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '732e7ae2-2b2f-534d-9cc2-234d01911fed'
SOURCE_PATH = 'icons-json/arrows/arrow button right 3_732e7ae2-2b2f-534d-9cc2-234d01911fed.json'
AUTHOR = 'json_to_solo'

class ArrowButtonRight3Arrows(Solo48):
    icon_id = 'arrow-button-right-3-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'button', 'right', 'arrows')

    def build(self):
        self.add_line('sym-e0', (40, 24), (40, 24))
        self.add_bezier('sym-e1', (40, 24), ((40, 22.776), (38.725, 21.738), (38, 21)))
        self.add_line('sym-e2', (38, 21), (22, 5))
        self.add_bezier('sym-e3', (22, 5), ((21.587, 4.573), (21.598, 4), (21, 4)))
        self.add_bezier('sym-e4', (21, 4), ((20.941, 4), (20.059, 4), (20, 4)))
        self.add_bezier('sym-e5', (20, 4), ((19.495, 4), (19.505, 4), (19, 4)))
        self.add_line('sym-e6', (19, 4), (8, 4))
        self.add_line('sym-e7', (8, 4), (27, 23))
        self.add_bezier('sym-e8', (27, 23), ((27.298, 23.308), (27, 23.698), (27, 24)))
        self.add_bezier('sym-e9', (27, 24), ((27, 24.302), (27.298, 24.692), (27, 25)))
        self.add_line('sym-e10', (27, 25), (8, 44))
        self.add_line('sym-e11', (8, 44), (19, 44))
        self.add_bezier('sym-e12', (19, 44), ((19.505, 44), (19.495, 44), (20, 44)))
        self.add_bezier('sym-e13', (20, 44), ((20.059, 44), (20.941, 44), (21, 44)))
        self.add_bezier('sym-e14', (21, 44), ((21.598, 44), (21.587, 43.427), (22, 43)))
        self.add_line('sym-e15', (22, 43), (38, 27))
        self.add_bezier('sym-e16', (38, 27), ((38.725, 26.262), (40, 25.224), (40, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)
