"""A heart flower and round bud sit in a tapered wrapper; minor wrapping folds omitted.

Construction references: Lucide rose, heart, gem and hand as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96b4290c-87f0-48c0-8533-608fb681e5cb'
SOURCE_PATH = 'pictographic-primitives/romance/flowers_96b4290c-87f0-48c0-8533-608fb681e5cb.svg'
AUTHOR = 'gpt-6'


class WrappedFlowerBouquet(Solo48):
    icon_id = 'wrapped-flower-bouquet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('bouquet', 'flower', 'heart', 'wrapping', 'gift', 'romance')

    def build(self) -> None:
        self.add_arc('heart-l',(18,9),(8,9),radius_x=5,sweep=False)
        self.add_line('heart-tip-1',(8,9),(18,22))
        self.add_line('heart-tip-2',(18,22),(28,9))
        self.add_arc('heart-r',(28,9),(18,9),radius_x=5,sweep=False)
        self.add_contour('heart','heart-l','heart-tip-1','heart-tip-2','heart-r',closed=True)
        self.add_arc('bud-a',(40,14),(28,26),radius_x=12,sweep=False)
        self.add_arc('bud-b',(28,26),(40,14),radius_x=12,sweep=False)
        self.add_contour('bud','bud-a','bud-b',closed=True)
        self.add_polyline('wrapper',(8,26),(24,36),(40,26),(8,26))
        self.add_line('flower-stem',(18,22),(18,26))
        self.relate('connect','flower-stem','heart')
        self.relate('connect','flower-stem','wrapper')
        self.relate('connect','bud','wrapper')
        self.add_polyline('tail',(16,44),(24,36),(32,44),closed=True)
        self.relate('connect','tail','wrapper')
