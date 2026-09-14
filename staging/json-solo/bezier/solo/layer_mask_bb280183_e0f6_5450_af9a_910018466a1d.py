"""Layer mask (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb280183-e0f6-5450-af9a-910018466a1d'
SOURCE_PATH = 'icons-json/design/layer mask_bb280183-e0f6-5450-af9a-910018466a1d.json'
AUTHOR = 'json_to_solo'

class LayerMaskDesign(Solo48):
    icon_id = 'layer-mask-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('layer', 'mask', 'design')

    def build(self):
        self.add_arc('sym-e0', (14, 24), (34, 24), radius_x=10)
        self.add_arc('sym-e1', (34, 24), (14, 24), radius_x=10)
        self.add_bezier('sym-e2', (12, 6), ((9.316, 6), (6.589, 8.537), (6, 11)))
        self.add_bezier('sym-e3', (6, 11), ((6, 11.47), (6, 12.503), (6, 13)))
        self.add_bezier('sym-e4', (6, 13), ((6, 13.117), (6, 12.888), (6, 13)))
        self.add_bezier('sym-e5', (6, 13), ((6, 13.45), (6, 13.558), (6, 14)))
        self.add_line('sym-e6', (6, 14), (6, 24))
        self.add_line('sym-e7', (6, 24), (6, 34))
        self.add_bezier('sym-e8', (6, 34), ((6, 34.442), (6, 34.55), (6, 35)))
        self.add_bezier('sym-e9', (6, 35), ((6, 35.112), (6, 34.883), (6, 35)))
        self.add_bezier('sym-e10', (6, 35), ((6, 35.497), (6, 36.53), (6, 37)))
        self.add_bezier('sym-e11', (6, 37), ((6.589, 39.463), (9.316, 42), (12, 42)))
        self.add_line('sym-e12', (12, 42), (24, 42))
        self.add_line('sym-e13', (24, 42), (36, 42))
        self.add_bezier('sym-e14', (36, 42), ((38.684, 42), (41.411, 39.463), (42, 37)))
        self.add_bezier('sym-e15', (42, 37), ((42, 36.53), (42, 35.497), (42, 35)))
        self.add_bezier('sym-e16', (42, 35), ((42, 34.883), (42, 35.112), (42, 35)))
        self.add_bezier('sym-e17', (42, 35), ((42, 34.55), (42, 34.442), (42, 34)))
        self.add_line('sym-e18', (42, 34), (42, 24))
        self.add_line('sym-e19', (42, 24), (42, 14))
        self.add_bezier('sym-e20', (42, 14), ((42, 13.558), (42, 13.45), (42, 13)))
        self.add_bezier('sym-e21', (42, 13), ((42, 12.888), (42, 13.117), (42, 13)))
        self.add_bezier('sym-e22', (42, 13), ((42, 12.503), (42, 11.47), (42, 11)))
        self.add_bezier('sym-e23', (42, 11), ((41.411, 8.537), (38.684, 6), (36, 6)))
        self.add_line('sym-e24', (36, 6), (24, 6))
        self.add_line('sym-e25', (24, 6), (12, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
