"""Microsoft visual studio logo 1 (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2d7127b-4a91-4f1f-9461-fcc33608bdcb'
SOURCE_PATH = 'icons-json/logos/microsoft visual studio logo 1_c2d7127b-4a91-4f1f-9461-fcc33608bdcb.json'
AUTHOR = 'json_to_solo'

class MicrosoftVisualStudioLogo1Logos(Solo48):
    icon_id = 'microsoft-visual-studio-logo-1-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('microsoft', 'visual', 'studio', 'logo', 'logos')

    def build(self):
        self.add_line('sym-e0', (24, 22), (29, 32))
        self.add_bezier('sym-e1', (29, 32), ((30.445, 35.04), (31.718, 38.12), (34, 39)))
        self.add_bezier('sym-e2', (34, 39), ((34.571, 39.218), (35.449, 40), (36, 40)))
        self.add_bezier('sym-e3', (36, 40), ((40.388, 40), (44, 33.103), (44, 25)))
        self.add_bezier('sym-e4', (44, 25), ((44, 24.872), (44, 25.128), (44, 25)))
        self.add_bezier('sym-e5', (44, 25), ((44, 24.568), (44, 23.432), (44, 23)))
        self.add_bezier('sym-e6', (44, 23), ((44, 14.82), (39.605, 8), (35, 8)))
        self.add_bezier('sym-e7', (35, 8), ((34.876, 8), (35.125, 8), (35, 8)))
        self.add_bezier('sym-e8', (35, 8), ((32.873, 8.176), (30.618, 10.76), (29, 13)))
        self.add_bezier('sym-e9', (29, 13), ((27.509, 15.048), (26.236, 17.456), (25, 20)))
        self.add_bezier('sym-e10', (25, 20), ((24.718, 20.592), (24.055, 22), (24, 22)))
        self.add_line('sym-e11', (24, 22), (19, 32))
        self.add_bezier('sym-e12', (19, 32), ((17.555, 35.04), (16.282, 38.12), (14, 39)))
        self.add_bezier('sym-e13', (14, 39), ((13.429, 39.218), (12.551, 40), (12, 40)))
        self.add_bezier('sym-e14', (12, 40), ((7.612, 40), (4, 33.103), (4, 25)))
        self.add_bezier('sym-e15', (4, 25), ((4, 24.872), (4, 25.128), (4, 25)))
        self.add_bezier('sym-e16', (4, 25), ((4, 24.568), (4, 23.432), (4, 23)))
        self.add_bezier('sym-e17', (4, 23), ((4, 14.82), (8.395, 8), (13, 8)))
        self.add_bezier('sym-e18', (13, 8), ((13.124, 8), (12.875, 8), (13, 8)))
        self.add_bezier('sym-e19', (13, 8), ((15.127, 8.176), (17.382, 10.76), (19, 13)))
        self.add_bezier('sym-e20', (19, 13), ((20.491, 15.048), (21.764, 17.456), (23, 20)))
        self.add_bezier('sym-e21', (23, 20), ((23.282, 20.592), (23.945, 22), (24, 22)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
