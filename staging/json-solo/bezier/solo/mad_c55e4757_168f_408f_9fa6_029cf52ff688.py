"""Mad (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c55e4757-168f-408f-9fa6-029cf52ff688'
SOURCE_PATH = 'icons-json/smileys/mad_c55e4757-168f-408f-9fa6-029cf52ff688.json'
AUTHOR = 'json_to_solo'

class MadSmileys(Solo48):
    icon_id = 'mad-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('mad', 'smileys')

    def build(self):
        self.add_line('e0', (12, 18), (19, 21))
        self.add_line('e1', (29, 21), (35, 18))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e3', (15, 35), ((15.336, 33.573), (15.718, 32.218), (16.645, 31.055)), ((21.764, 24.609), (31.118, 27.382), (33, 35)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e3')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
