'shout: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0170253f-5b18-54db-9549-084ab4e62b33'
SOURCE_PATH = 'pictographic-primitives/smileys/shout_0170253f-5b18-54db-9549-084ab4e62b33.svg'
AUTHOR = 'gpt-6'

class Shout(Solo48):
    icon_id = 'shout'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('shout', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_line('eye-left',(18,16),(18,19))
        self.add_line('eye-right',(30,16),(30,19))

        self.add_arc('mouth-top', (20,30), (28,30), radius_x=4, radius_y=4)
        self.add_arc('mouth-bottom', (28,30), (20,30), radius_x=4, radius_y=4)
        self.add_contour('mouth', 'mouth-top', 'mouth-bottom', closed=True)
