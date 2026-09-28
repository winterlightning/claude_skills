"""Square envelope; repositioned both eyes equally between the mask curves and cheek outline.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1ad97e11-bd58-4d42-a0e0-51be7206e42e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sloth-face/20260927T093511Z-thuan-mac-1/reference/sloth_1ad97e11-bd58-4d42-a0e0-51be7206e42e.svg'
AUTHOR = "gpt-6"

class SlothFace(Solo48):
    icon_id = 'sloth-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('sloth', 'face', 'head', 'eyes', 'animal', 'slow', 'cute', 'wildlife')

    def build(self) -> None:
        self.add_arc('head0', (6, 24), (24, 6), radius_x=18, radius_y=18, sweep=True)
        self.add_arc('head1', (24, 6), (42, 24), radius_x=18, radius_y=18, sweep=True)
        self.add_arc('head2', (42, 24), (24, 42), radius_x=18, radius_y=18, sweep=True)
        self.add_arc('head3', (24, 42), (6, 24), radius_x=18, radius_y=18, sweep=True)
        self.add_contour('head', 'head0', 'head1', 'head2', 'head3', closed=True)
        self.add_arc('left-mask', (6, 24), (20, 18), radius_x=17, radius_y=10, sweep=False)
        self.add_dot('left-eye', (17, 30))
        self.add_arc('right-mask', (42, 24), (28, 18), radius_x=17, radius_y=10, sweep=True)
        self.add_dot('right-eye', (31, 30))
        self.relate('connect', 'head', 'left-mask')
        self.relate('connect', 'head', 'right-mask')
