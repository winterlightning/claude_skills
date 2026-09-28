"""A front-facing flower with eight rounded radial lobes. SQUARE extremes (6,6)-(42,42). Shallow petals make room for the eyes and smile.
Reduction: Removed the extra circular face border; retained eyes and curved smile.
Lucide construction: flower
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f439cc7d-8e34-5beb-ab1a-9677f1869dce'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-flower/20260927T133815Z-thuan-mac-1/reference/flower_f439cc7d-8e34-5beb-ab1a-9677f1869dce.svg'
AUTHOR = "gpt-6"


class SmilingFlower(Solo48):
    icon_id = 'smiling-flower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    categories = ("nature", "primitives")
    aliases = ()
    keywords = ('flower', 'smile', 'happy', 'face', 'petals', 'cheerful', 'kids', 'nature')

    def build(self) -> None:
        # Six broad mirrored petals around a single smiling face.
        top = (24, 6)
        right = [
            ((29, 6), (33, 8), (32, 12)),
            ((36, 10), (42, 11), (42, 16)),
            ((42, 20), (39, 22), (36, 24)),
            ((40, 26), (42, 29), (42, 32)),
            ((42, 37), (36, 39), (32, 36)),
            ((32, 40), (29, 42), (24, 42)),
        ]
        self.add_bezier('petals-right', top, *right)
        mirror = lambda point: (48 - point[0], point[1])
        nodes = [top] + [segment[2] for segment in right]
        left = [(mirror(segment[1]), mirror(segment[0]), mirror(nodes[index]))
                for index, segment in reversed(list(enumerate(right)))]
        self.add_bezier('petals-left', (24, 42), *left)
        self.add_contour('petals', 'petals-right', 'petals-left', closed=True)
        self.add_dot('eye-left', (19, 20))
        self.add_dot('eye-right', (29, 20))
        self.add_arc('smile', (27, 29), (21, 29), radius_x=5)
