"""A surgical face mask has ear loops and a central pleat. No useful exact Lucide match; use mirrored elliptical loops. Reduce two pleats to one."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ca479623-685a-50f7-b79c-95ae041dea54'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__surgical-face-mask/20260927T094403Z-thuan-mac-1/reference/protection mask_ca479623-685a-50f7-b79c-95ae041dea54.svg'
AUTHOR = "gpt-6"


class ProtectionIcon(Solo48):
    icon_id = 'surgical-face-mask'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    categories = ("protection", "primitives")
    aliases = ()
    keywords = ('face mask', 'surgical', 'medical', 'mask', 'health', 'hygiene', 'protection', 'virus')

    def build(self):
        # Flat upper seam, bowed lower fabric edge, paired loops, and one pleat.
        self.add_line('top', (10, 10), (38, 10))
        self.add_line('right-side', (38, 10), (38, 28))
        self.add_bezier('lower-right', (38, 28), ((38, 34), (31, 38), (24, 38)))
        self.add_bezier('lower-left', (24, 38), ((17, 38), (10, 34), (10, 28)))
        self.add_line('left-side', (10, 28), (10, 10))
        self.add_contour('panel', 'top', 'right-side', 'lower-right', 'lower-left', 'left-side', closed=True)
        self.add_arc('loop-left', (10, 12), (10, 28), radius_x=6, radius_y=8, sweep=False)
        self.add_arc('loop-right', (38, 28), (38, 12), radius_x=6, radius_y=8, sweep=False)
        self.relate('connect', 'loop-left', 'panel')
        self.relate('connect', 'loop-right', 'panel')
        self.add_line('pleat-upper', (19, 20), (29, 20))
        self.add_line('pleat-lower', (19, 28), (29, 28))
