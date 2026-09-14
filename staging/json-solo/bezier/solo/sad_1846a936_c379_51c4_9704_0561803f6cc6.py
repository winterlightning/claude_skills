"""Sad (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1846a936-c379-51c4-9704-0561803f6cc6'
SOURCE_PATH = 'icons-json/smileys/sad_1846a936-c379-51c4-9704-0561803f6cc6.json'
AUTHOR = 'json_to_solo'

class SadSmileys(Solo48):
    icon_id = 'sad-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('sad', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (15, 32), ((15.473, 31.282), (15.845, 30.682), (16.464, 30.073)), ((19.936, 26.627), (26.627, 26.355), (30.536, 29.218)), ((31.627, 30.018), (32.291, 30.873), (33, 32)))
        self.add_bezier('e2', (12, 22), ((14.982, 21.945), (17.427, 21.527), (19, 19)))
        self.add_bezier('e3', (29, 19), ((30.445, 21.282), (32.236, 21.782), (35, 22)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
