"""Classical head behind an open book. SQUARE (2,2)-(46,46). Lucide book-open: paired pages and central spine. Removed text, ear and individual hair curls; left-facing profile is intentional."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8cdb2a8f-2d94-4ed2-9762-9b3c6ee9478d'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/greek mythology_8cdb2a8f-2d94-4ed2-9762-9b3c6ee9478d.svg'
AUTHOR = 'astra-chatgpt'


class ClassicalHeadWithBook(Solo48):
    icon_id = 'classical-head-with-book'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('mythology', 'greek', 'classical', 'book', 'reading', 'philosophy', 'study', 'literature')

    def build(self) -> None:
        self.add_arc('crown', (8,10), (32,10), radius_x=12, radius_y=8)
        self.add_arc('back-head', (32,10), (28,20), radius_x=14)
        self.add_line('face-1', (8, 10), (2, 20))
        self.add_line('face-2', (2, 20), (8, 20))
        self.add_line('face-3', (8, 20), (8, 26))
        self.add_line('face-4', (8, 26), (14, 26))
        self.add_line('face-5', (14, 26), (14, 30))
        self.add_arc('neck', (14,30), (8,36), radius_x=6)
        self.add_arc('shoulder', (8,36), (2,46), radius_x=12)
        self.add_contour('front', 'face-1','face-2','face-3','face-4','face-5','neck','shoulder')
        self.relate('connect', 'crown', 'front')
        self.relate('connect', 'crown', 'back-head')
        
        self.add_polyline('book', (22,26), (34,30), (46,26), (46,42), (34,46), (22,42), closed=True)
        self.add_line('spine', (34,30), (34,46))
        self.relate('connect', 'book', 'spine')
