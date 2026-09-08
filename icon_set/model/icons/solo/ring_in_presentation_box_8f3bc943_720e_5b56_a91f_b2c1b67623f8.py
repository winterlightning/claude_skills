"""Ring in open presentation case. VRECT_XL extremes (5,2)-(43,46). Rounded case and clear gem silhouette; facets omitted to preserve space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f3bc943-720e-5b56-a91f-b2c1b67623f8'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/ring in case_8f3bc943-720e-5b56-a91f-b2c1b67623f8.svg'
AUTHOR = 'astra-chatgpt'


class RingInPresentationBox(Solo48):
    icon_id = 'ring-in-presentation-box'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('ring', 'engagement ring', 'box', 'case', 'proposal', 'jewellery', 'jewelry', 'diamond', 'gift')

    def build(self) -> None:
        self.add_line('case-0', (11, 2), (37, 2))
        self.add_arc('case-1', (37, 2), (43, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_line('case-2-attach-0', (43, 8), (43, 35))
        self.add_line('case-2-attach-1', (43, 35), (43, 40))
        self.add_arc('case-3', (43, 40), (37, 46), radius_x=6, radius_y=6, sweep=True)
        self.add_line('case-4', (37, 46), (11, 46))
        self.add_arc('case-5', (11, 46), (5, 40), radius_x=6, radius_y=6, sweep=True)
        self.add_line('case-6-attach-0', (5, 40), (5, 35))
        self.add_line('case-6-attach-1', (5, 35), (5, 8))
        self.add_arc('case-7', (5, 8), (11, 2), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('case', 'case-0', 'case-1', 'case-2-attach-0', 'case-2-attach-1', 'case-3', 'case-4', 'case-5', 'case-6-attach-0', 'case-6-attach-1', 'case-7', closed=True)
        self.add_line('tray-attach-0', (5, 35), (15, 35))
        self.add_line('tray-attach-1', (15, 35), (33, 35))
        self.add_line('tray-attach-2', (33, 35), (43, 35))
        self.add_contour('tray', 'tray-attach-0', 'tray-attach-1', 'tray-attach-2')
        self.relate("connect", 'case', 'tray')
        self.add_arc('ring-left', (15, 35), (24, 25), radius_x=9, radius_y=10, sweep=True)
        self.add_arc('ring-right', (24, 25), (33, 35), radius_x=9, radius_y=10, sweep=True)
        self.add_contour('ring', 'ring-left', 'ring-right', closed=False)
        self.add_line('gem-1', (24, 25), (16, 17))
        self.add_line('gem-2', (16, 17), (20, 11))
        self.add_line('gem-3', (20, 11), (28, 11))
        self.add_line('gem-4', (28, 11), (32, 17))
        self.add_line('gem-5', (32, 17), (24, 25))
        self.add_contour('gem', 'gem-1', 'gem-2', 'gem-3', 'gem-4', 'gem-5', closed=True)
        self.relate("connect", 'gem', 'ring')
        self.relate("connect", 'ring', 'tray')
