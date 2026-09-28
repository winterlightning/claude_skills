"""A wide gavel striking block with four softly rounded corners."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c48a60eb-d543-4958-b02f-1af524f7b1a0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gavel-block/20260927T055616Z-thuan-mac-1/reference/gavel block_c48a60eb-d543-4958-b02f-1af524f7b1a0.svg'
AUTHOR = "gpt-6"

class GavelBlock(Solo48):
    icon_id = 'gavel-block'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('gavel', 'block', 'state')

    def build(self):
        # The widest permitted horizontal envelope and matched corner radii
        # restore the source block's soft, long rectangular outline.
        self.add_line('top', (8, 10), (40, 10))
        self.add_arc('top-right', (40, 10), (44, 14), radius_x=4)
        self.add_line('right', (44, 14), (44, 34))
        self.add_arc('bottom-right', (44, 34), (40, 38), radius_x=4)
        self.add_line('bottom', (40, 38), (8, 38))
        self.add_arc('bottom-left', (8, 38), (4, 34), radius_x=4)
        self.add_line('left', (4, 34), (4, 14))
        self.add_arc('top-left', (4, 14), (8, 10), radius_x=4)
        self.add_contour('block', 'top', 'top-right', 'right', 'bottom-right',
                         'bottom', 'bottom-left', 'left', 'top-left', closed=True)
