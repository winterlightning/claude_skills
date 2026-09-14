"""Square play button (medias), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e1', (7, 8), (4, 11), radius_x=3, sweep=False)
        self.add_line('sym-e2', (4, 11), (4, 24))
        self.add_line('sym-e3', (4, 24), (4, 37))
        self.add_arc('sym-e4', (4, 37), (7, 40), radius_x=3, sweep=False)
        self.add_line('sym-e5', (7, 40), (41, 40))
        self.add_arc('sym-e6', (41, 40), (44, 37), radius_x=3, sweep=False)
        self.add_line('sym-e7', (44, 37), (44, 24))
        self.add_line('sym-e8', (44, 24), (44, 11))
        self.add_arc('sym-e9', (44, 11), (41, 8), radius_x=3, sweep=False)
        self.add_line('sym-e10', (30, 22), (19, 16))
        self.add_arc('sym-e11', (19, 16), (17, 18), radius_x=2, sweep=False)
        self.add_line('sym-e13', (17, 18), (17, 24))
        self.add_line('sym-e14', (17, 24), (17, 30))
        self.add_arc('sym-e16', (17, 30), (19, 32), radius_x=2, sweep=False)
        self.add_line('sym-e17', (19, 32), (30, 26))
        self.add_line('sym-e18', (30, 26), (32, 24))
        self.add_line('sym-e19', (32, 24), (30, 22))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
