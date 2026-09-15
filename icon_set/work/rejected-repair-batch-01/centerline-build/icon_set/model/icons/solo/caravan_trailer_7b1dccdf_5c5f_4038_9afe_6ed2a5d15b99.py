'Caravan: tangent rounded front, clear window margins and a round attached wheel; extend the tow bar to the horizontal envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b1dccdf-5c5f-4038-9afe-6ed2a5d15b99'
SOURCE_PATH = 'pictographic-primitives/transportation/trailer_7b1dccdf-5c5f-4038-9afe-6ed2a5d15b99.svg'
AUTHOR = 'gpt-6'


class CaravanTrailer(Solo48):
    icon_id = 'caravan-trailer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('caravan', 'trailer', 'camper', 'rv', 'travel', 'camping', 'tow', 'holiday')

    def build(self) -> None:
        self.add_line('roof',(4,8),(24,8))
        self.add_arc('front',(24,8),(34,18),radius_x=10)
        self.add_polyline('lower',(34,18),(34,32),(18,32),(4,32),(4,8))
        self.relate('connect','roof','front');self.relate('connect','front','lower');self.relate('connect','roof','lower')
        self.add_line('window',(13,20),(23,20))
        self.add_line('tow',(34,32),(44,32));self.relate('connect','tow','lower')

        self.add_arc('wheel-top', (14,36), (22,36), radius_x=4, radius_y=4)
        self.add_arc('wheel-bottom', (22,36), (14,36), radius_x=4, radius_y=4)
        self.add_contour('wheel', 'wheel-top', 'wheel-bottom', closed=True)
        self.relate('connect','wheel','lower')
