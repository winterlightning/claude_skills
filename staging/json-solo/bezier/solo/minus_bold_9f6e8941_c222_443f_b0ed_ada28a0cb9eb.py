"""Minus bold (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f6e8941-c222-443f-b0ed-ada28a0cb9eb'
SOURCE_PATH = 'icons-json/symbol/minus bold_9f6e8941-c222-443f-b0ed-ada28a0cb9eb.json'
AUTHOR = 'json_to_solo'

class MinusBold9f6e8941(Solo48):
    icon_id = 'minus-bold-9f6e8941'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('minus', 'bold', 'symbol')

    def build(self):
        self.add_line('sym-e0', (40, 40), (24, 40))
        self.add_line('sym-e1', (24, 40), (8, 40))
        self.add_bezier('sym-e2', (8, 40), ((6.309, 38.94), (4, 36.44), (4, 32)))
        self.add_bezier('sym-e3', (4, 32), ((4, 31.82), (4.009, 31.2), (4, 31)))
        self.add_bezier('sym-e4', (4, 31), ((4, 30.34), (4, 29.68), (4, 29)))
        self.add_bezier('sym-e5', (4, 29), ((4, 27.698), (4, 26.305), (4, 25)))
        self.add_bezier('sym-e6', (4, 25), ((4, 24.61), (4, 24.391), (4, 24)))
        self.add_bezier('sym-e7', (4, 24), ((4, 23.609), (4, 23.39), (4, 23)))
        self.add_bezier('sym-e8', (4, 23), ((4, 21.695), (4, 20.302), (4, 19)))
        self.add_bezier('sym-e9', (4, 19), ((4, 18.32), (4, 17.66), (4, 17)))
        self.add_bezier('sym-e10', (4, 17), ((4.009, 16.8), (4, 16.18), (4, 16)))
        self.add_bezier('sym-e11', (4, 16), ((4, 11.56), (6.309, 9.06), (8, 8)))
        self.add_line('sym-e12', (8, 8), (24, 8))
        self.add_line('sym-e13', (24, 8), (40, 8))
        self.add_bezier('sym-e14', (40, 8), ((41.691, 9.06), (44, 11.56), (44, 16)))
        self.add_bezier('sym-e15', (44, 16), ((44, 16.18), (43.991, 16.8), (44, 17)))
        self.add_bezier('sym-e16', (44, 17), ((44, 17.66), (44, 18.32), (44, 19)))
        self.add_bezier('sym-e17', (44, 19), ((44, 20.302), (44, 21.695), (44, 23)))
        self.add_bezier('sym-e18', (44, 23), ((44, 23.39), (44, 23.609), (44, 24)))
        self.add_bezier('sym-e19', (44, 24), ((44, 24.391), (44, 24.61), (44, 25)))
        self.add_bezier('sym-e20', (44, 25), ((44, 26.305), (44, 27.698), (44, 29)))
        self.add_bezier('sym-e21', (44, 29), ((44, 29.68), (44, 30.34), (44, 31)))
        self.add_bezier('sym-e22', (44, 31), ((43.991, 31.2), (44, 31.82), (44, 32)))
        self.add_bezier('sym-e23', (44, 32), ((44, 36.44), (41.691, 38.94), (40, 40)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
