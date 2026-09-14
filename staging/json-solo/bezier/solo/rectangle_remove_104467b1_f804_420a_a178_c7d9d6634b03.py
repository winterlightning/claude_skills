"""Rectangle remove (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '104467b1-f804-420a-a178-c7d9d6634b03'
SOURCE_PATH = 'icons-json/state/rectangle remove_104467b1-f804-420a-a178-c7d9d6634b03.json'
AUTHOR = 'json_to_solo'

class RectangleRemove104467b1(Solo48):
    icon_id = 'rectangle-remove-104467b1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('rectangle', 'remove', 'state')

    def build(self):
        self.add_line('sym-e0', (24, 24), (20, 30))
        self.add_line('sym-e1', (20, 18), (24, 24))
        self.add_line('sym-e2', (24, 24), (28, 30))
        self.add_line('sym-e3', (24, 40), (7, 40))
        self.add_bezier('sym-e4', (7, 40), ((6.7, 40), (6.3, 40), (6, 40)))
        self.add_bezier('sym-e5', (6, 40), ((5.273, 40), (4, 38.472), (4, 37)))
        self.add_bezier('sym-e6', (4, 37), ((4, 36.888), (4, 37.128), (4, 37)))
        self.add_bezier('sym-e7', (4, 37), ((4, 36.888), (4, 37.112), (4, 37)))
        self.add_line('sym-e8', (4, 37), (4, 11))
        self.add_bezier('sym-e9', (4, 11), ((4, 10.824), (4, 11.176), (4, 11)))
        self.add_bezier('sym-e10', (4, 11), ((4, 9.112), (5.036, 8), (6, 8)))
        self.add_bezier('sym-e11', (6, 8), ((6.282, 8), (6.718, 8), (7, 8)))
        self.add_line('sym-e12', (7, 8), (24, 8))
        self.add_line('sym-e13', (24, 8), (41, 8))
        self.add_bezier('sym-e14', (41, 8), ((41.282, 8), (41.718, 8), (42, 8)))
        self.add_bezier('sym-e15', (42, 8), ((42.964, 8), (44, 9.112), (44, 11)))
        self.add_bezier('sym-e16', (44, 11), ((44, 11.176), (44, 10.824), (44, 11)))
        self.add_line('sym-e17', (44, 11), (44, 37))
        self.add_bezier('sym-e18', (44, 37), ((44, 37.112), (44, 36.888), (44, 37)))
        self.add_bezier('sym-e19', (44, 37), ((44, 37.128), (44, 36.888), (44, 37)))
        self.add_bezier('sym-e20', (44, 37), ((44, 38.472), (42.727, 40), (42, 40)))
        self.add_bezier('sym-e21', (42, 40), ((41.7, 40), (41.3, 40), (41, 40)))
        self.add_line('sym-e22', (41, 40), (24, 40))
        self.add_line('sym-e23', (28, 18), (24, 24))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', closed=True)
        self.add_contour('sym-c3', 'sym-e23')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
