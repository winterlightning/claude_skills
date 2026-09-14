"""Rectangle remove (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '104467b1-f804-420a-a178-c7d9d6634b03'
SOURCE_PATH = 'icons-json/state/rectangle remove_104467b1-f804-420a-a178-c7d9d6634b03.json'
AUTHOR = 'json_to_solo'

class RectangleRemove(Solo48):
    icon_id = 'rectangle-remove'
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
        self.add_arc('sym-e4', (7, 40), (6, 40), radius_x=20, sweep=False)
        self.add_line('sym-e5-1', (6, 40), (4, 39))
        self.add_line('sym-e5-2', (4, 39), (4, 37))
        self.add_line('sym-e8', (4, 37), (4, 11))
        self.add_line('sym-e10-1', (4, 11), (4, 9))
        self.add_line('sym-e10-2', (4, 9), (6, 8))
        self.add_line('sym-e11', (6, 8), (7, 8))
        self.add_line('sym-e12', (7, 8), (24, 8))
        self.add_line('sym-e13', (24, 8), (41, 8))
        self.add_line('sym-e14', (41, 8), (42, 8))
        self.add_line('sym-e15-1', (42, 8), (44, 9))
        self.add_arc('sym-e15-2', (44, 9), (44, 11), radius_x=4, sweep=False)
        self.add_line('sym-e17', (44, 11), (44, 37))
        self.add_line('sym-e20-1', (44, 37), (44, 39))
        self.add_line('sym-e20-2', (44, 39), (42, 40))
        self.add_arc('sym-e21', (42, 40), (41, 40), radius_x=41, sweep=False)
        self.add_line('sym-e22', (41, 40), (24, 40))
        self.add_line('sym-e23', (28, 18), (24, 24))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5-1', 'sym-e5-2', 'sym-e8', 'sym-e10-1', 'sym-e10-2', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15-1', 'sym-e15-2', 'sym-e17', 'sym-e20-1', 'sym-e20-2', 'sym-e21', 'sym-e22', closed=True)
        self.add_contour('sym-c3', 'sym-e23')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
