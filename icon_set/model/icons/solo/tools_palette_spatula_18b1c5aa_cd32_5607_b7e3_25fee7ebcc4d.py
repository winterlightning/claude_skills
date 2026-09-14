"""Tools palette spatula (tools), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18b1c5aa-cd32-5607-b7e3-25fee7ebcc4d'
SOURCE_PATH = 'icons-json/tools/tools palette spatula_18b1c5aa-cd32-5607-b7e3-25fee7ebcc4d.json'
AUTHOR = 'json_to_solo'

class ToolsPaletteSpatula(Solo48):
    icon_id = 'tools-palette-spatula'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('tools', 'palette', 'spatula')

    def build(self):
        self.add_line('sym-e0', (36, 19), (12, 19))
        self.add_line('sym-e2', (24, 44), (20, 43))
        self.add_arc('sym-e3', (20, 43), (19, 37), radius_x=4)
        self.add_line('sym-e4', (19, 37), (20, 29))
        self.add_arc('sym-e5-1', (20, 29), (19, 27), radius_x=2, sweep=False)
        self.add_arc('sym-e5-2', (19, 27), (14, 24), radius_x=10, sweep=False)
        self.add_line('sym-e6', (14, 24), (12, 20))
        self.add_line('sym-e7', (12, 20), (8, 6))
        self.add_line('sym-e8', (8, 6), (8, 5))
        self.add_arc('sym-e9', (8, 5), (9, 4), radius_x=1)
        self.add_line('sym-e10', (9, 4), (10, 4))
        self.add_line('sym-e11', (10, 4), (12, 4))
        self.add_line('sym-e12', (12, 4), (24, 4))
        self.add_line('sym-e13', (24, 4), (36, 4))
        self.add_line('sym-e14', (36, 4), (38, 4))
        self.add_line('sym-e15', (38, 4), (39, 4))
        self.add_arc('sym-e16', (39, 4), (40, 5), radius_x=1)
        self.add_arc('sym-e17', (40, 5), (40, 6), radius_x=21, sweep=False)
        self.add_line('sym-e18', (40, 6), (36, 20))
        self.add_line('sym-e19', (36, 20), (34, 24))
        self.add_arc('sym-e20-1', (34, 24), (29, 27), radius_x=10, sweep=False)
        self.add_arc('sym-e20-2', (29, 27), (28, 29), radius_x=2, sweep=False)
        self.add_line('sym-e21', (28, 29), (29, 37))
        self.add_arc('sym-e22', (29, 37), (28, 43), radius_x=4)
        self.add_line('sym-e23', (28, 43), (24, 44))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5-1', 'sym-e5-2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20-1', 'sym-e20-2', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
