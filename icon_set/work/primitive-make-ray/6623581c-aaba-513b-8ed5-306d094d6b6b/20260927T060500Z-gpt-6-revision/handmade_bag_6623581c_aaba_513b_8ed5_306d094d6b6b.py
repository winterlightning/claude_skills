"""Handmade bag (hobbies), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6623581c-aaba-513b-8ed5-306d094d6b6b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handmade-bag/20260927T060349Z-thuan-mac-1/reference/handmade bag_6623581c-aaba-513b-8ed5-306d094d6b6b.svg'
AUTHOR = "gpt-6"

class HandmadeBag(Solo48):
    icon_id = 'handmade-bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    categories = ('primitives', 'hobbies')
    aliases = ()
    keywords = ('handmade', 'bag', 'hobbies')

    def build(self):
        # The source body widens toward a rounded base, with a centered arch.
        self.add_line('top', (12,18), (36,18))
        self.add_line('right-slope', (36,18), (40,40))
        self.add_arc('bottom-right', (40,40), (36,44), radius_x=4)
        self.add_line('bottom', (36,44), (12,44))
        self.add_arc('bottom-left', (12,44), (8,40), radius_x=4)
        self.add_line('left-slope', (8,40), (12,18))
        self.add_contour('bag','top','right-slope','bottom-right','bottom',
                         'bottom-left','left-slope',closed=True)
        self.add_line('handle-left',(16,18),(16,12))
        self.add_arc('handle-arch',(16,12),(32,12),radius_x=8)
        self.add_line('handle-right',(32,12),(32,18))
        self.add_contour('handle','handle-left','handle-arch','handle-right')
        self.relate('connect','bag','handle')
