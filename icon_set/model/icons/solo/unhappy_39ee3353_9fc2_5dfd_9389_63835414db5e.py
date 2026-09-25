'unhappy: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39ee3353-9fc2-5dfd-9389-63835414db5e'
SOURCE_PATH = 'pictographic-primitives/smileys/unhappy_39ee3353-9fc2-5dfd-9389-63835414db5e.svg'
AUTHOR = 'gpt-6'

class Unhappy(Solo48):
    icon_id = 'unhappy'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('unhappy', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_arc('eye-left',(15,18),(19,16),radius_x=6,sweep=False)
        self.add_arc('eye-right',(29,16),(33,18),radius_x=6,sweep=False)
        self.add_arc('mouth',(17,32),(31,32),radius_x=7,radius_y=4)
