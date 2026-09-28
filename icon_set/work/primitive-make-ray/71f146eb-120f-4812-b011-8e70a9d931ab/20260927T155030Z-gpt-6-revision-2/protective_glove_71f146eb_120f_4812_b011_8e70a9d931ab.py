'An upright glove has four rounded fingers of different heights and a thumb spreading diagonally right. The sides widen above a straight open cuff, with short divisions between the fingers.\n\nConstruction: Four rounded fingertips with shared eight-unit spacing and an outward thumb. Finger creases reduced to three straight seams; clapping reference reduced to its dominant raised hand. Bounds (6,6)-(42,42).\nLucide: hand: rounded fingertip arches and broad palm.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '71f146eb-120f-4812-b011-8e70a9d931ab'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__protective-glove/20260927T153803Z-thuan-mac-1/reference/gloves_71f146eb-120f-4812-b011-8e70a9d931ab.svg'
AUTHOR = 'gpt-6'

class ProtectiveGlove(Solo48):
    icon_id = 'protective-glove'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('glove', 'hand', 'protection', 'cleaning', 'fingers', 'cuff')

    def build(self):
        # Open cuff and four staggered fingers, retaining the thumb at right.
        self.add_polyline('glove',(10,42),(10,32),(6,26),(6,20),(10,16),
                          (14,20),(14,14),(18,10),(22,14),(22,10),
                          (26,6),(30,10),(30,14),(34,10),(38,14),
                          (38,23),(42,27),(34,35),(34,42))
        for x,y in ((14,20),(22,14),(30,14)):
            self.add_line(f'finger-crease-{x}',(x,y),(x,26))
            self.relate('connect',f'finger-crease-{x}','glove')
