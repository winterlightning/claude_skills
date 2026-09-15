'kiss-blush: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8bf97a21-ff13-5cb7-954c-403ce4978e36'
SOURCE_PATH = 'pictographic-primitives/smileys/kiss blush_8bf97a21-ff13-5cb7-954c-403ce4978e36.svg'
AUTHOR = 'gpt-6'

class KissBlush(Solo48):
    icon_id = 'kiss-blush'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('kiss', 'blush', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_dot('eye-left',(18,18))
        self.add_dot('eye-right',(30,18))
        self.add_bezier('mouth',(22,27),((28,27),(28,30),(23,30)),((28,30),(28,33),(22,33)))
