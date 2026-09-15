'Play control: round rim and triangular play mark with balanced radial clearance.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '866bf46c-f592-44ca-a741-a14f2c7f0394'
SOURCE_PATH = 'pictographic-primitives/mobile/carplay connect_866bf46c-f592-44ca-a741-a14f2c7f0394.svg'
AUTHOR = 'gpt-6'

class CarplayConnect(Solo48):
    icon_id = 'carplay-connect'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('carplay', 'connect', 'mobile')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_polyline('play',(19,15),(32,24),(19,33),closed=True)
