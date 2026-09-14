"""Square play button (medias), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '08463876-5f43-4cd9-869b-34fbb81d9519'
SOURCE_PATH = 'icons-json/medias/square play button_08463876-5f43-4cd9-869b-34fbb81d9519.json'
AUTHOR = 'json_to_solo'

class SquarePlayButtonMedias(Solo48):
    icon_id = 'square-play-button-medias'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'medias'
    aliases = ()
    keywords = ('square', 'play', 'button', 'medias')

    def build(self):
        self.add_line('sym-e0', (41, 8), (7, 8))
        self.add_bezier('sym-e1', (7, 8), ((5.4, 8.573), (4.582, 9.518), (4, 11)))
        self.add_line('sym-e2', (4, 11), (4, 24))
        self.add_line('sym-e3', (4, 24), (4, 37))
        self.add_bezier('sym-e4', (4, 37), ((4.582, 38.482), (5.4, 39.427), (7, 40)))
        self.add_line('sym-e5', (7, 40), (41, 40))
        self.add_bezier('sym-e6', (41, 40), ((42.1, 39.621), (44, 38.322), (44, 37)))
        self.add_line('sym-e7', (44, 37), (44, 24))
        self.add_line('sym-e8', (44, 24), (44, 11))
        self.add_bezier('sym-e9', (44, 11), ((44, 9.678), (42.1, 8.379), (41, 8)))
        self.add_line('sym-e10', (30, 22), (19, 16))
        self.add_bezier('sym-e11', (19, 16), ((18.218, 16.177), (17.3, 17.183), (17, 18)))
        self.add_bezier('sym-e12', (17, 18), ((16.927, 18.202), (17.055, 17.806), (17, 18)))
        self.add_line('sym-e13', (17, 18), (17, 24))
        self.add_line('sym-e14', (17, 24), (17, 30))
        self.add_bezier('sym-e15', (17, 30), ((17.055, 30.194), (16.927, 29.798), (17, 30)))
        self.add_bezier('sym-e16', (17, 30), ((17.3, 30.817), (18.218, 31.823), (19, 32)))
        self.add_line('sym-e17', (19, 32), (30, 26))
        self.add_bezier('sym-e18', (30, 26), ((30.517, 25.745), (31.731, 24.722), (32, 24)))
        self.add_bezier('sym-e19', (32, 24), ((31.731, 23.278), (30.517, 22.255), (30, 22)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
