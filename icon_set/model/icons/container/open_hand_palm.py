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


v3 (2026-10-07): simplified to one outline so a container symbol has room (container-combination64): a symbol of 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

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
        # One simple outline: four finger arches of width 10 (tops 10, 4, 8, 14) over a broad palm 14..54 with a
        # small thumb bump on the left, and short creases between the fingers that stop at y 19. The palm holds a
        # symbol of 24 with a 4 px gap (was 15 with the long creases and inset thumb).
        self.add_line('index-left', (14, 38), (14, 15))
        self.add_arc('index-tip', (14, 15), (24, 15), radius_x=5)
        self.add_line('middle-left', (24, 15), (24, 9))
        self.add_arc('middle-tip', (24, 9), (34, 9), radius_x=5)
        self.add_line('middle-right', (34, 9), (34, 13))
        self.add_arc('ring-tip', (34, 13), (44, 13), radius_x=5)
        self.add_line('ring-right', (44, 13), (44, 19))
        self.add_arc('little-tip', (44, 19), (54, 19), radius_x=5)
        self.add_line('palm-right', (54, 19), (54, 44))
        self.add_bezier('palm-base', (54, 44), ((54, 54), (45, 60), (34, 60)))
        self.add_line('palm-bottom', (34, 60), (28, 60))
        self.add_bezier('heel', (28, 60), ((21, 60), (16, 56), (13, 50)))
        self.add_line('thumb-side', (13, 50), (10, 44))
        self.add_line('thumb-front', (10, 44), (10, 42))
        self.add_arc('thumb-tip', (10, 42), (14, 38), radius_x=4)
        self.add_line('crease-24', (24, 15), (24, 19))
        self.add_line('crease-34', (34, 13), (34, 19))
        self.add_contour('outline', 'index-left', 'index-tip', 'middle-left', 'middle-tip', 'middle-right', 'ring-tip', 'ring-right', 'little-tip', 'palm-right', 'palm-base', 'palm-bottom', 'heel', 'thumb-side', 'thumb-front', 'thumb-tip', closed=True)
        self.relate('connect', 'outline', 'crease-24')
        self.relate('connect', 'outline', 'crease-34')
