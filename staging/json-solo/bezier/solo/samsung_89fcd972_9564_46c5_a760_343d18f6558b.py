"""Samsung (phones), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89fcd972-9564-46c5-a760-343d18f6558b'
SOURCE_PATH = 'icons-json/phones/samsung_89fcd972-9564-46c5-a760-343d18f6558b.json'
AUTHOR = 'json_to_solo'

class SamsungPhones(Solo48):
    icon_id = 'samsung-phones'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    aliases = ()
    keywords = ('samsung', 'phones')

    def build(self):
        self.add_line('sym-e0', (8, 34), (40, 34))
        self.add_line('sym-e1', (40, 34), (40, 8))
        self.add_bezier('sym-e2', (40, 8), ((40, 7.964), (40, 8.036), (40, 8)))
        self.add_bezier('sym-e3', (40, 8), ((40, 6.618), (37.54, 4), (36, 4)))
        self.add_bezier('sym-e4', (36, 4), ((35.93, 4), (36.07, 4.009), (36, 4)))
        self.add_line('sym-e5', (36, 4), (24, 4))
        self.add_line('sym-e6', (24, 4), (12, 4))
        self.add_bezier('sym-e7', (12, 4), ((11.93, 4.009), (12.07, 4), (12, 4)))
        self.add_bezier('sym-e8', (12, 4), ((10.46, 4), (8, 6.618), (8, 8)))
        self.add_bezier('sym-e9', (8, 8), ((8, 8.036), (8, 7.964), (8, 8)))
        self.add_line('sym-e10', (8, 8), (8, 34))
        self.add_line('sym-e11', (8, 34), (8, 40))
        self.add_bezier('sym-e12', (8, 40), ((8, 41.409), (10.41, 44), (12, 44)))
        self.add_bezier('sym-e13', (12, 44), ((12.04, 44), (11.96, 43.991), (12, 44)))
        self.add_line('sym-e14', (12, 44), (24, 44))
        self.add_line('sym-e15', (24, 44), (36, 44))
        self.add_bezier('sym-e16', (36, 44), ((36.04, 43.991), (35.96, 44), (36, 44)))
        self.add_bezier('sym-e17', (36, 44), ((37.59, 44), (40, 41.409), (40, 40)))
        self.add_line('sym-e18', (40, 40), (40, 34))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
