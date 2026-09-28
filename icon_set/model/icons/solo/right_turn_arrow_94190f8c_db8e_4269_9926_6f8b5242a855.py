from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94190f8c-db8e-4269-9926-6f8b5242a855'
SOURCE_PATH = 'pictographic-primitives/transportation/right curve ahead_94190f8c-db8e-4269-9926-6f8b5242a855.svg'
AUTHOR = 'gpt-6'

class RightTurnArrow(Solo48):
    icon_id = 'right-turn-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('right turn', 'turn', 'arrow', 'direction', 'road', 'navigation', 'curve', 'traffic')

    def build(self):
        self.add_line('lower',(6,42),(6,28))
        self.add_arc('bend',(6,28),(18,16),radius_x=12,sweep=True)
        self.add_line('upper',(18,16),(42,16))
        self.add_contour('shaft','lower','bend','upper')
        self.add_polyline('head',(32,6),(42,16),(32,26))
        self.relate('connect','shaft','head')
