"""Legal scale 2 (office), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bc123ee-6bde-4551-bf5e-c0a7f52704f1'
SOURCE_PATH = 'icons-json/office/legal scale 2_9bc123ee-6bde-4551-bf5e-c0a7f52704f1.json'
AUTHOR = 'json_to_solo'

class LegalScale2Office(Solo48):
    icon_id = 'legal-scale-2-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('legal', 'scale', 'office')

    def build(self):
        self.add_line('sym-e0', (24, 8), (24, 12))
        self.add_line('sym-e1', (24, 12), (24, 17))
        self.add_line('sym-e2', (7, 12), (11, 12))
        self.add_line('sym-e3', (11, 12), (24, 12))
        self.add_line('sym-e4', (24, 12), (37, 12))
        self.add_line('sym-e5', (37, 12), (41, 12))
        self.add_line('sym-e6', (18, 32), (11, 12))
        self.add_line('sym-e7', (11, 12), (5, 32))
        self.add_line('sym-e8', (5, 32), (18, 32))
        self.add_bezier('sym-e9', (18, 32), ((18.3, 32), (18.7, 32), (19, 32)))
        self.add_line('sym-e10', (19, 32), (19, 34))
        self.add_bezier('sym-e11', (19, 34), ((17.9, 37.03), (15.2, 40), (12, 40)))
        self.add_bezier('sym-e12', (12, 40), ((11.791, 40), (11.209, 40), (11, 40)))
        self.add_bezier('sym-e13', (11, 40), ((10.873, 40), (11.127, 40), (11, 40)))
        self.add_bezier('sym-e14', (11, 40), ((8.391, 40), (4, 37.13), (4, 34)))
        self.add_bezier('sym-e15', (4, 34), ((4, 33.88), (4, 33.13), (4, 33)))
        self.add_bezier('sym-e16', (4, 33), ((4, 32.78), (4, 33.22), (4, 33)))
        self.add_bezier('sym-e17', (4, 33), ((4, 32.8), (4, 32.21), (4, 32)))
        self.add_bezier('sym-e18', (4, 32), ((4, 31.99), (4.891, 32), (5, 32)))
        self.add_line('sym-e19', (30, 32), (37, 12))
        self.add_line('sym-e20', (37, 12), (43, 32))
        self.add_line('sym-e21', (43, 32), (30, 32))
        self.add_bezier('sym-e22', (30, 32), ((29.7, 32), (29.3, 32), (29, 32)))
        self.add_line('sym-e23', (29, 32), (29, 34))
        self.add_bezier('sym-e24', (29, 34), ((30.1, 37.03), (32.8, 40), (36, 40)))
        self.add_bezier('sym-e25', (36, 40), ((36.209, 40), (36.791, 40), (37, 40)))
        self.add_bezier('sym-e26', (37, 40), ((37.127, 40), (36.873, 40), (37, 40)))
        self.add_bezier('sym-e27', (37, 40), ((39.609, 40), (44, 37.13), (44, 34)))
        self.add_bezier('sym-e28', (44, 34), ((44, 33.88), (44, 33.13), (44, 33)))
        self.add_bezier('sym-e29', (44, 33), ((44, 32.78), (44, 33.22), (44, 33)))
        self.add_bezier('sym-e30', (44, 33), ((44, 32.8), (44, 32.21), (44, 32)))
        self.add_bezier('sym-e31', (44, 32), ((44, 31.99), (43.109, 32), (43, 32)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c3', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
