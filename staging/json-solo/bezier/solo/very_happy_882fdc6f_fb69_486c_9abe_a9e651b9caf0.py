"""Very happy (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '882fdc6f-fb69-486c-9abe-a9e651b9caf0'
SOURCE_PATH = 'icons-json/smileys/very happy_882fdc6f-fb69-486c-9abe-a9e651b9caf0.json'
AUTHOR = 'json_to_solo'

class VeryHappySmileys(Solo48):
    icon_id = 'very-happy-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('very', 'happy', 'smileys')

    def build(self):
        self.add_line('e0', (17, 28), (31, 28))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e2', (10, 19), ((10.191, 18.618), (10.691, 18.682), (10.945, 18.327)), ((12.491, 16.218), (16.082, 16.045), (17.791, 18.055)), ((18.155, 18.491), (18.782, 18.491), (19, 19)))
        self.add_bezier('e3', (29, 19), ((30.936, 15.282), (36.109, 15.236), (38, 19)))
        self.add_bezier('e4', (31, 28), ((31.173, 30.127), (31.009, 31.682), (29.709, 33.409)), ((27.145, 36.8), (21.4, 36.9), (18.582, 33.818)), ((17.009, 32.091), (16.982, 30.236), (17, 28)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e0', 'e4', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
