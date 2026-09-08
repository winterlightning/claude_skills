"""Classical head and shoulders on a plinth. VRECT_XL (5,2)-(43,46). Simplified curls and pedestal seams. Left-facing anatomical asymmetry retained; no useful direct Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1bafc453-5bc6-415b-bdab-800770f2d87b'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/greek statue_1bafc453-5bc6-415b-bdab-800770f2d87b.svg'
AUTHOR = 'astra-chatgpt'


class ClassicalStatueBust(Solo48):
    icon_id = 'classical-statue-bust'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('statue', 'bust', 'greek', 'classical', 'sculpture', 'marble', 'museum', 'antiquity')

    def build(self) -> None:
        self.add_arc('crown', (11,10), (35,10), radius_x=12, radius_y=8)
        self.add_arc('back-head', (35,10), (31,22), radius_x=14)
        self.add_line('back-neck-1', (31, 22), (31, 28))
        self.add_line('back-neck-2', (31, 28), (37, 30))
        self.add_arc('right-shoulder', (37,30), (43,38), radius_x=10)
        self.add_line('chest-base', (43,38), (5,38))
        self.add_arc('left-shoulder', (5,38), (11,30), radius_x=10)
        self.add_line('face-neck-1', (11, 30), (19, 28))
        self.add_line('face-neck-2', (19, 28), (19, 24))
        self.add_line('face-neck-3', (19, 24), (11, 24))
        self.add_line('face-neck-4', (11, 24), (11, 18))
        self.add_line('face-neck-5', (11, 18), (5, 18))
        self.add_line('face-neck-6', (5, 18), (11, 10))
        self.add_contour('bust','crown','back-head','back-neck-1','back-neck-2','right-shoulder','chest-base','left-shoulder','face-neck-1','face-neck-2','face-neck-3','face-neck-4','face-neck-5','face-neck-6', closed=True)
        self.add_line('plinth', (11,46), (37,46))
