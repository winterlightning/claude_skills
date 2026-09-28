"""Star Magic Wand.

Symbol plan: Five-point star and a diagonal single-stroke wand; star silhouette preserves reference orientation. Lucide wand informs the simple shaft. Thin hollow handle omitted.
Keyshape: SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2239a15c-dd4c-44b5-99ff-7e5c0c02afee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/magic wand_2239a15c-dd4c-44b5-99ff-7e5c0c02afee.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'diagonal-star-wand-with-rounded-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/design"
    aliases = ()
    keywords = ('star', 'magic', 'wand')

    def build(self):
        self.add_polyline('star',(23,6),(32,12),(42,8),(39,20),(42,29),(31,28),(25,38),(21,27),(10,24),(21,17),closed=True)
        self.add_line('handle',(6,42),(21,27))
        self.relate('connect','handle','star')
