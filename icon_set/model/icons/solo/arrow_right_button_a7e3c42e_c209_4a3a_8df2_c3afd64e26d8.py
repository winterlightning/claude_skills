"""Arrow right button (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7e3c42e-c209-4a3a-8df2-c3afd64e26d8'
SOURCE_PATH = 'icons-json/symbol/arrow right button_a7e3c42e-c209-4a3a-8df2-c3afd64e26d8.json'
AUTHOR = 'json_to_solo'

class ArrowRightButton(Solo48):
    icon_id = 'arrow-right-button'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'right', 'button', 'symbol')

    def build(self):
        self.add_line('sym-e0', (40, 24), (40, 24))
        self.add_arc('sym-e1', (40, 24), (38, 21), radius_x=4, sweep=False)
        self.add_line('sym-e2', (38, 21), (22, 5))
        self.add_line('sym-e3', (22, 5), (21, 4))
        self.add_arc('sym-e4', (21, 4), (20, 4), radius_x=55)
        self.add_arc('sym-e5', (20, 4), (19, 4), radius_x=50)
        self.add_line('sym-e6', (19, 4), (8, 4))
        self.add_line('sym-e7', (8, 4), (27, 23))
        self.add_arc('sym-e8', (27, 23), (27, 24), radius_x=1, sweep=False)
        self.add_arc('sym-e9', (27, 24), (27, 25), radius_x=1, sweep=False)
        self.add_line('sym-e10', (27, 25), (8, 44))
        self.add_line('sym-e11', (8, 44), (19, 44))
        self.add_line('sym-e12', (19, 44), (20, 44))
        self.add_arc('sym-e13', (20, 44), (21, 44), radius_x=26)
        self.add_line('sym-e14', (21, 44), (22, 43))
        self.add_line('sym-e15', (22, 43), (38, 27))
        self.add_arc('sym-e16', (38, 27), (40, 24), radius_x=4, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)
