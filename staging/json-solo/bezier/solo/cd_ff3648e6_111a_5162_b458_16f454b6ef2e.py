"""Batch-04/cd (computers), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff3648e6-111a-5162-b458-16f454b6ef2e'
SOURCE_PATH = 'icons-json/computers/batch-04/cd_ff3648e6-111a-5162-b458-16f454b6ef2e.json'
AUTHOR = 'json_to_solo'

class Batch04Cd(Solo48):
    icon_id = 'batch-04-cd'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'cd', 'computers')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-top', (19, 24), (29, 24), radius_x=5)
        self.add_arc('e1-bottom', (29, 24), (19, 24), radius_x=5)
        self.add_bezier('e2', (29, 12), ((33.836, 14.045), (37.445, 17.764), (38, 23)))
        self.add_bezier('e3', (10, 24), ((10.091, 29.6), (14.036, 33.682), (19, 36)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
