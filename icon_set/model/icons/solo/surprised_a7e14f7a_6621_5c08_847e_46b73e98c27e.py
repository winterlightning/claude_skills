'surprised: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7e14f7a-6621-5c08-847e-46b73e98c27e'
SOURCE_PATH = 'pictographic-primitives/smileys/surprised_a7e14f7a-6621-5c08-847e-46b73e98c27e.svg'
AUTHOR = 'gpt-6'

class Surprised(Solo48):
    icon_id = 'surprised'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('surprised', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_dot('eye-left',(18,18))
        self.add_dot('eye-right',(30,18))

        self.add_arc('mouth-top', (20,30), (28,30), radius_x=4, radius_y=4)
        self.add_arc('mouth-bottom', (28,30), (20,30), radius_x=4, radius_y=4)
        self.add_contour('mouth', 'mouth-top', 'mouth-bottom', closed=True)
