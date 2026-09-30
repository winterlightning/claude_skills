"""A curved horizontal ribbon banner with folded, pointed tails at both lower sides. Exclude the star; preserve its top-overlap relationship in the later composition.

Plan: A bowed band and mirrored folded tails; band owns paired elliptical arches. Bounds (2,10)-(62,54).
Hosting at the standard slot: add-sub32: valid, heart-state-63: review, check-mark: valid.
Construction reference: No close Lucide subject; use simple connected contours.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (curved-ribbon-banner-container HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '3792f25a-9089-4cd6-9389-b22b47f0380b'
SOURCE_ICON_IDS = ('3792f25a-9089-4cd6-9389-b22b47f0380b',)
SOURCE_PATH = 'pictographic-primitives/rewards/ranking ribbon_3792f25a-9089-4cd6-9389-b22b47f0380b.svg'
AUTHOR = 'claude-opus-5-5'


class CurvedRibbonBannerContainer(Container64):
    icon_id = 'curved-ribbon-banner-container'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases = ()
    keywords = ('curved', 'ribbon', 'banner', 'container')

    def build(self) -> None:
        self.add_arc('band-top', (12, 21), (52, 21), radius_x=20, radius_y=9)
        self.add_line('band-right', (52, 21), (52, 39))
        self.add_bezier('band-bottom', (52, 39), ((49.3, 35.5), (45.7, 32.875), (43, 32)), ((39.333, 30.25), (35.667, 30.25), (32, 30.25)), ((28.333, 30.25), (24.667, 30.25), (21, 32)), ((18.3, 32.875), (14.7, 35.5), (12, 39)))
        self.add_line('band-left', (12, 39), (12, 21))
        self.add_line('left-1', (12, 39), (4, 43))
        self.add_line('left-2', (4, 43), (10, 45))
        self.add_line('left-3', (10, 45), (8, 52))
        self.add_line('left-4', (8, 52), (21, 45))
        self.add_line('left-5', (21, 45), (21, 32))
        self.add_line('right-1', (52, 39), (60, 43))
        self.add_line('right-2', (60, 43), (54, 45))
        self.add_line('right-3', (54, 45), (56, 52))
        self.add_line('right-4', (56, 52), (43, 45))
        self.add_line('right-5', (43, 45), (43, 32))
        self.add_contour('band', 'band-top', 'band-right', 'band-bottom', 'band-left', closed=True)
        self.add_contour('left', 'left-1', 'left-2', 'left-3', 'left-4', 'left-5')
        self.add_contour('right', 'right-1', 'right-2', 'right-3', 'right-4', 'right-5')
        self.relate('connect', 'left', 'band')
        self.relate('connect', 'right', 'band')
