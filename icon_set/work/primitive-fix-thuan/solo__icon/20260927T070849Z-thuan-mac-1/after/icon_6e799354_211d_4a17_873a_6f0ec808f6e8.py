"""@ (state), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6e799354-211d-4a17-873a-6f0ec808f6e8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__icon/20260927T070849Z-thuan-mac-1/reference/@_6e799354-211d-4a17-873a-6f0ec808f6e8.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Icon(Solo48):
    icon_id = 'icon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('state',)

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (28, 41), (25, 42))
        self.add_line('e1', (34, 31), (32, 28))
        # Four coherent sweeps replace the sampled outer contour's tiny detours.
        self.add_bezier('e2', (25,42),
            ((14,42),(6,34),(6,24)),
            ((6,14),(14,6),(24,6)),
            ((34,6),(42,14),(42,24)),
            ((42,29),(39,32),(34,31)))
        self.add_bezier('e3', (32, 28), ((29.554, 30.651), (28.238, 32.223), (24.515, 32.313)), ((18.232, 32.468), (14.435, 26.062), (16.972, 20.506)), ((19.377, 15.221), (26.847, 14.411), (30.562, 18.764)), ((32.861, 21.455), (32.434, 24.727), (32, 28)))
        self.add_contour('c0', 'e0', 'e2', 'e1', closed=False)
        self.add_contour('c1', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
