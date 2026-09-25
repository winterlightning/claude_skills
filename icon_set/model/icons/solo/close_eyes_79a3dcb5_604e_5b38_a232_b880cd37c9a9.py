'Closed eye: smooth mirrored lid and three separated lashes replace the crowded fringe.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79a3dcb5-604e-5b38-a232-b880cd37c9a9'
SOURCE_PATH = 'pictographic-primitives/interface-essential/close eyes_79a3dcb5-604e-5b38-a232-b880cd37c9a9.svg'
AUTHOR = 'gpt-6'

class CloseEyes(Solo48):
    icon_id = 'close-eyes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('close', 'eyes', 'interface-essential')

    def build(self) -> None:
        self.add_bezier('upper',(4,21),((10,12),(17,8),(24,8)),((31,8),(38,12),(44,21)))
        self.add_bezier('lower',(44,21),((42,23),(40,26),(38,27)),((33,30),(29,32),(24,32)),((19,32),(15,30),(10,27)),((8,26),(6,23),(4,21)))
        self.add_contour('lid','upper','lower',closed=True)
        # Three well-spaced lashes keep the closed-eye reading without crowded fringes.
        self.add_line('lash-middle',(24,32),(24,40));self.relate('connect','lash-middle','lid')
        self.add_line('lash-left',(10,27),(7,34));self.relate('connect','lash-left','lid')
        self.add_line('lash-right',(38,27),(41,34));self.relate('connect','lash-right','lid')
