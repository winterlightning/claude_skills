"""An upright open hand encloses a broad palm below four rounded fingers.

The existing user-selected container family is retained. VRECT_XL fits raised
fingers and palm: ink (4,0)-(60,64), centerline (6,2)-(58,62).
Reference: supplied failed SVG; Lucide hand original and atomic-debug informed
rounded fingertips, connected finger creases and an open thumb web. All five
digits remain; staggered finger heights and the thumb are intentionally asymmetric.
Shared human reference inspected: icon_set/references/human_ref/full_body_ref.png;
this isolated hand has no head/body proportions or detached-head gap to measure.

Hosting (compose.py): heart valid; plus, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (open-hand-palm VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'open-hand-palm'
SOURCE_PATH = 'icon_set/dist/failed/container64/open-hand-palm.svg'
AUTHOR = 'claude-opus-5-5'


class OpenHandPalm(Container64):
    icon_id = 'open-hand-palm'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('raised-hand', 'hand-palm-container')
    keywords = ('hand', 'palm', 'human', 'greeting', 'stop', 'attention')

    def build(self) -> None:
        self.add_line('index-left', (21, 28), (21, 13))
        self.add_arc('index-tip', (21, 13), (29, 13), radius_x=4)
        self.add_line('middle-left', (29, 13), (29, 8))
        self.add_arc('middle-tip', (29, 8), (37, 8), radius_x=4)
        self.add_line('middle-right', (37, 8), (37, 13))
        self.add_arc('ring-tip', (37, 13), (45, 13), radius_x=4)
        self.add_line('ring-right', (45, 13), (44, 23))
        self.add_arc('little-tip', (44, 23), (54, 23), radius_x=5)
        self.add_line('palm-right', (54, 23), (54, 42))
        self.add_arc('palm-base-right', (54, 42), (37, 60), radius_x=17, radius_y=18)
        self.add_arc('palm-base-left', (37, 60), (17, 50), radius_x=25)
        self.add_line('thumb-side', (17, 50), (12, 42))
        self.add_arc('thumb-heel', (12, 42), (10, 36), radius_x=10)
        self.add_arc('thumb-tip', (10, 36), (20, 36), radius_x=5)
        self.add_line('thumb-web', (20, 36), (24, 42))
        self.add_line('finger-crease-28', (29, 13), (29, 28))
        self.add_line('finger-crease-38', (37, 13), (37, 28))
        self.add_line('finger-crease-48', (44, 23), (45, 28))
        self.add_contour('outline', 'index-left', 'index-tip', 'middle-left', 'middle-tip', 'middle-right', 'ring-tip', 'ring-right', 'little-tip', 'palm-right', 'palm-base-right', 'palm-base-left', 'thumb-side', 'thumb-heel', 'thumb-tip', 'thumb-web')
        self.relate('connect', 'finger-crease-28', 'outline')
        self.relate('connect', 'finger-crease-38', 'outline')
        self.relate('connect', 'finger-crease-48', 'outline')
