'oops: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f00feae-aa12-5183-b688-b143212648de'
SOURCE_PATH = 'pictographic-primitives/smileys/oops_4f00feae-aa12-5183-b688-b143212648de.svg'
AUTHOR = 'gpt-6'

class Oops(Solo48):
    icon_id = 'oops'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('oops', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_polyline('eye-left',(16,16),(20,18),(16,20))
        self.add_polyline('eye-right',(32,16),(28,18),(32,20))

        self.add_arc('mouth-top', (20,30), (28,30), radius_x=4, radius_y=4)
        self.add_arc('mouth-bottom', (28,30), (20,30), radius_x=4, radius_y=4)
        self.add_contour('mouth', 'mouth-top', 'mouth-bottom', closed=True)
