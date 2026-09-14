"""Ceramic (hobbies), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9b91a34-6703-4faf-a865-315e9a81c798'
SOURCE_PATH = 'icons-json/hobbies/ceramic_d9b91a34-6703-4faf-a865-315e9a81c798.json'
AUTHOR = 'json_to_solo'

class CeramicHobbies(Solo48):
    icon_id = 'ceramic-hobbies'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('ceramic', 'hobbies')

    def build(self):
        self.add_line('sym-e0', (24, 44), (15, 44))
        self.add_bezier('sym-e1', (15, 44), ((15.07, 41.664), (15.39, 39.1), (14, 37)))
        self.add_line('sym-e2', (14, 37), (11, 32))
        self.add_bezier('sym-e3', (11, 32), ((9.48, 29.691), (8, 25.709), (8, 23)))
        self.add_bezier('sym-e4', (8, 23), ((8, 22.818), (8, 22.173), (8, 22)))
        self.add_bezier('sym-e5', (8, 22), ((8, 21.818), (8, 22.182), (8, 22)))
        self.add_bezier('sym-e6', (8, 22), ((8, 20.055), (8.81, 17.618), (10, 16)))
        self.add_line('sym-e7', (10, 16), (14, 10))
        self.add_bezier('sym-e8', (14, 10), ((15.46, 8.009), (15.04, 6.236), (15, 4)))
        self.add_line('sym-e9', (15, 4), (24, 4))
        self.add_line('sym-e10', (24, 4), (33, 4))
        self.add_bezier('sym-e11', (33, 4), ((32.96, 6.236), (32.54, 8.009), (34, 10)))
        self.add_line('sym-e12', (34, 10), (38, 16))
        self.add_bezier('sym-e13', (38, 16), ((39.19, 17.618), (40, 20.055), (40, 22)))
        self.add_bezier('sym-e14', (40, 22), ((40, 22.182), (40, 21.818), (40, 22)))
        self.add_bezier('sym-e15', (40, 22), ((40, 22.173), (40, 22.818), (40, 23)))
        self.add_bezier('sym-e16', (40, 23), ((40, 25.709), (38.52, 29.691), (37, 32)))
        self.add_line('sym-e17', (37, 32), (34, 37))
        self.add_bezier('sym-e18', (34, 37), ((32.61, 39.1), (32.93, 41.664), (33, 44)))
        self.add_line('sym-e19', (33, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
