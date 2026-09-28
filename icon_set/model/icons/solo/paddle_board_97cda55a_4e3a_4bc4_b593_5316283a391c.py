'Paddleboard: smooth upright board and a narrower paddle blade preserve the subject while opening the separating gap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97cda55a-4e3a-4bc4-b593-5316283a391c'
SOURCE_PATH = 'pictographic-primitives/outdoors/paddle board_97cda55a-4e3a-4bc4-b593-5316283a391c.svg'
AUTHOR = 'gpt-6'

class PaddleBoard(Solo48):
    icon_id = 'paddle-board'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('paddle', 'board', 'outdoors')

    def build(self) -> None:
        self.add_bezier('board',(16,4),((12,8),(8,17),(8,26)),((8,38),(11,44),(16,44)),((21,44),(23,38),(23,26)),((23,17),(20,8),(16,4)))
        self.add_line('shaft',(35,4),(35,28))
        self.add_polyline('grip',(31,4),(35,4),(39,4))
        self.add_bezier('blade',(35,28),((32,32),(31,36),(31,40)),((31,44),(40,44),(40,40)),((40,36),(38,31),(35,28)))
        self.relate('connect','shaft','grip');self.relate('connect','shaft','blade')
