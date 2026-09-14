"""Batch-02/group (decoration), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f11189f-b7d1-45bb-a32f-5ced4e76526a'
SOURCE_PATH = 'icons-json/decoration/batch-02/group_2f11189f-b7d1-45bb-a32f-5ced4e76526a.json'
AUTHOR = 'json_to_solo'

class Batch02Group(Solo48):
    icon_id = 'batch-02-group'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('batch', 'group', 'decoration')

    def build(self):
        self.add_line('e0', (8, 4), (40, 4))
        self.add_line('e1', (40, 4), (24, 24))
        self.add_line('e2', (24, 24), (39, 44))
        self.add_line('e3', (39, 44), (9, 44))
        self.add_line('e4', (9, 44), (24, 25))
        self.add_line('e5', (24, 25), (8, 4))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', closed=True)
