"""Arrow left button (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a74099d0-c11f-40f0-b7ad-8f5a80bb9351'
SOURCE_PATH = 'icons-json/symbol/arrow left button_a74099d0-c11f-40f0-b7ad-8f5a80bb9351.json'
AUTHOR = 'json_to_solo'

class ArrowLeftButtonSymbol(Solo48):
    icon_id = 'arrow-left-button-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'left', 'button', 'symbol')

    def build(self):
        self.add_line('sym-e0', (8, 24), (8, 24))
        self.add_bezier('sym-e1', (8, 24), ((8, 25.224), (9.275, 26.262), (10, 27)))
        self.add_line('sym-e2', (10, 27), (26, 43))
        self.add_bezier('sym-e3', (26, 43), ((26.413, 43.427), (26.402, 44), (27, 44)))
        self.add_bezier('sym-e4', (27, 44), ((27.059, 44), (27.941, 44), (28, 44)))
        self.add_bezier('sym-e5', (28, 44), ((28.505, 44), (28.495, 44), (29, 44)))
        self.add_line('sym-e6', (29, 44), (40, 44))
        self.add_line('sym-e7', (40, 44), (21, 25))
        self.add_bezier('sym-e8', (21, 25), ((20.702, 24.692), (21, 24.302), (21, 24)))
        self.add_bezier('sym-e9', (21, 24), ((21, 23.698), (20.702, 23.308), (21, 23)))
        self.add_line('sym-e10', (21, 23), (40, 4))
        self.add_line('sym-e11', (40, 4), (29, 4))
        self.add_bezier('sym-e12', (29, 4), ((28.495, 4), (28.505, 4), (28, 4)))
        self.add_bezier('sym-e13', (28, 4), ((27.941, 4), (27.059, 4), (27, 4)))
        self.add_bezier('sym-e14', (27, 4), ((26.402, 4), (26.413, 4.573), (26, 5)))
        self.add_line('sym-e15', (26, 5), (10, 21))
        self.add_bezier('sym-e16', (10, 21), ((9.275, 21.738), (8, 22.776), (8, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)
