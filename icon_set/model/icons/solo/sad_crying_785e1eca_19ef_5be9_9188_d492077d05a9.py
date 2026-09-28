'sad-crying: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '785e1eca-19ef-5be9-9188-d492077d05a9'
SOURCE_PATH = 'pictographic-primitives/smileys/sad crying_785e1eca-19ef-5be9-9188-d492077d05a9.svg'
AUTHOR = 'gpt-6'

class SadCrying(Solo48):
    icon_id = 'sad-crying'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('sad', 'crying', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)

        # Tears are continuous with the drooping eyes, so no disconnected slivers remain.
        self.add_polyline('left-tear',(20,16),(15,18),(15,21))
        self.add_polyline('right-tear',(28,16),(33,18),(33,21))

        self.add_arc('mouth-top', (20,30), (28,30), radius_x=4, radius_y=4)
        self.add_arc('mouth-bottom', (28,30), (20,30), radius_x=4, radius_y=4)
        self.add_contour('mouth', 'mouth-top', 'mouth-bottom', closed=True)
