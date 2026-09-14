"""Nasty (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b1706a3-e496-488f-ac2b-2aeeeed700fd'
SOURCE_PATH = 'icons-json/smileys/nasty_9b1706a3-e496-488f-ac2b-2aeeeed700fd.json'
AUTHOR = 'json_to_solo'

class NastySmileys(Solo48):
    icon_id = 'nasty-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('nasty', 'smileys')

    def build(self):
        self.add_line('e0', (12, 17), (19, 20))
        self.add_line('e1', (29, 20), (36, 17))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e3', (15, 33), ((20.064, 27.627), (27.9, 27.764), (33, 33)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e3')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
