"""A heart flower and round bud sit in a tapered wrapper; minor wrapping folds omitted.

Construction references: Lucide rose, heart, gem and hand as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '96b4290c-87f0-48c0-8533-608fb681e5cb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wrapped-flower-bouquet/20260927T082307Z-thuan-mac-1/reference/flowers_96b4290c-87f0-48c0-8533-608fb681e5cb.svg'
AUTHOR = 'gpt-6'


class WrappedFlowerBouquet(Solo48):
    icon_id = 'wrapped-flower-bouquet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    categories = ("primitives", "romance")
    aliases = ()
    keywords = ('bouquet', 'flower', 'heart', 'wrapping', 'gift', 'romance')

    def build(self) -> None:
        self.add_arc('heart-l',(18,9),(8,9),radius_x=5,sweep=False)
        self.add_line('heart-tip-1',(8,9),(18,22))
        self.add_line('heart-tip-2',(18,22),(27,9))
        self.add_arc('heart-r',(27,9),(18,9),radius_x=5,sweep=False)
        self.add_contour('heart','heart-l','heart-tip-1','heart-tip-2','heart-r',closed=True)
        self.add_arc('bud-a',(40,14),(30,24),radius_x=10,sweep=False)
        self.add_arc('bud-b',(30,24),(40,14),radius_x=10,sweep=False)
        self.add_contour('bud','bud-a','bud-b',closed=True)
        self.add_polyline('wrapper-left',(8,26),(24,36))
        self.add_polyline('wrapper-right',(24,36),(40,32))
        self.add_line('lip-left',(8,26),(18,26))
        self.relate('connect','wrapper-left','wrapper-right')
        self.relate('connect','wrapper-left','lip-left')
        self.add_line('flower-stem',(18,22),(18,26))
        self.relate('connect','flower-stem','heart')
        self.relate('connect','flower-stem','lip-left')
        self.add_line('bud-stem',(30,24),(32,34))
        self.relate('connect','bud','bud-stem')
        self.relate('connect','wrapper-right','bud-stem')
        self.add_polyline('tail',(20,36),(28,36),(32,44),(16,44),closed=True)
        self.relate('connect','tail','wrapper-left')
        self.relate('connect','tail','wrapper-right')
