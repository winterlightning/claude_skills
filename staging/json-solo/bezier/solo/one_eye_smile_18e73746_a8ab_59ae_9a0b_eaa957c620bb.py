"""One eye smile (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18e73746-a8ab-59ae-9a0b-eaa957c620bb'
SOURCE_PATH = 'icons-json/smileys/one eye smile_18e73746-a8ab-59ae-9a0b-eaa957c620bb.json'
AUTHOR = 'json_to_solo'

class OneEyeSmileSmileys(Solo48):
    icon_id = 'one-eye-smile-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('one', 'eye', 'smile', 'smileys')

    def build(self):
        self.add_line('e0', (33, 18), (29, 20))
        self.add_line('e1', (29, 20), (33, 23))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e3', (15, 29), ((15.255, 29.7), (15.409, 29.964), (15.773, 30.618)), ((18.536, 35.491), (25.382, 36.909), (29.791, 33.409)), ((31.4, 32.136), (32.318, 30.909), (33, 29)))
        self.add_bezier('e4', (20, 21), ((19.718, 21.355), (19.864, 22.018), (19.5, 22.309)), ((19.191, 22.564), (18.691, 22.682), (18.309, 22.764)), ((15.755, 23.291), (14.682, 19.891), (15.491, 17.991)), ((16.355, 15.982), (18.964, 15.673), (20.182, 17.482)), ((20.982, 18.655), (20.391, 19.745), (20, 21)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e0', 'e1')
        self.add_contour('c2', 'e4', closed=True)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
