'An upright glove has four rounded fingers of different heights and a thumb spreading diagonally right. The sides widen above a straight open cuff, with short divisions between the fingers.\n\nConstruction: Four rounded fingertips with shared eight-unit spacing and an outward thumb. Finger creases reduced to three straight seams; clapping reference reduced to its dominant raised hand. Bounds (6,6)-(42,42).\nLucide: hand: rounded fingertip arches and broad palm.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '71f146eb-120f-4812-b011-8e70a9d931ab'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__protective-glove/20260927T153803Z-thuan-mac-1/reference/gloves_71f146eb-120f-4812-b011-8e70a9d931ab.svg'
AUTHOR = "gpt-6"

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
        # A continuous rounded fingertip outline ends in an open straight cuff.
        self.add_line('cuff-left',(10,42),(10,32))
        self.add_line('palm-left',(10,32),(6,26))
        self.add_line('little-side',(6,26),(6,20))
        self.add_arc('little-tip',(6,20),(14,20),radius_x=4,sweep=True)
        self.add_line('ring-side',(14,20),(14,14))
        self.add_arc('ring-tip',(14,14),(22,14),radius_x=4,sweep=True)
        self.add_line('middle-side',(22,14),(22,10))
        self.add_arc('middle-tip',(22,10),(30,10),radius_x=4,sweep=True)
        self.add_line('index-side',(30,10),(30,14))
        self.add_arc('index-tip',(30,14),(38,14),radius_x=4,sweep=True)
        self.add_line('thumb-base',(38,14),(38,23))
        self.add_line('thumb-outer',(38,23),(42,27))
        self.add_line('thumb-inner',(42,27),(34,35))
        self.add_line('palm-right',(34,35),(34,42))
        self.add_contour('glove','cuff-left','palm-left','little-side','little-tip',
                         'ring-side','ring-tip','middle-side','middle-tip','index-side',
                         'index-tip','thumb-base','thumb-outer','thumb-inner','palm-right')
        for x,y in ((14,20),(22,14),(30,14)):
            self.add_line(f'finger-crease-{x}',(x,y),(x,26))
            self.relate('connect',f'finger-crease-{x}','glove')
