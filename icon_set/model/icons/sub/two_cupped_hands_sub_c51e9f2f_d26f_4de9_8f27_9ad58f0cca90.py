"""Two mirrored open cupped hands facing inward/upward, with thumb and finger contours and open wrists. Keep the pair together as one offering/protection gesture.

Plan: Mirrored cupped hands share contour dimensions about x16; open wrists and inner thumb strokes. Bounds (2,4)-(30,28).
Construction reference: Lucide hand-heart: coherent open hand contour and thumb bend; original supplies mirrored pair."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c51e9f2f-d26f-4de9-8f27-9ad58f0cca90'
SOURCE_PATH = 'pictographic-primitives/state/hand holding_c51e9f2f-d26f-4de9-8f27-9ad58f0cca90.svg'
SOURCE_ICON_IDS = ('c51e9f2f-d26f-4de9-8f27-9ad58f0cca90',)
AUTHOR = 'gpt-6'

class TwoCuppedHandsSub(Sub32):
    icon_id = 'two-cupped-hands-sub'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('two', 'cupped', 'hands', 'sub')

    def build(self) -> None:
        for sign,name in ((1,'left'),(-1,'right')):
            def pt(x,y):return (16+sign*(x-16),y)
            self.add_bezier(name+'-outer',pt(6,28),(pt(6,25),pt(2,21),pt(2,15)),(pt(2,12),pt(2,7),pt(3,4)))
            self.add_bezier(name+'-fingers',pt(3,4),(pt(6,4),pt(5,13),pt(6,15)))
            self.add_bezier(name+'-thumb',pt(6,15),(pt(7,12),pt(9,12),pt(10,14)),(pt(13,17),pt(13,20),pt(13,28)))
            self.add_contour(name,name+'-outer',name+'-fingers',name+'-thumb')
