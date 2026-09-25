"""An upright open hand encloses a broad palm below four rounded fingers.

The existing user-selected container family is retained. VRECT_XL fits raised
fingers and palm: ink (4,0)-(60,64), centerline (6,2)-(58,62).
Reference: supplied failed SVG; Lucide hand original and atomic-debug informed
rounded fingertips, connected finger creases and an open thumb web. All five
digits remain; staggered finger heights and the thumb are intentionally asymmetric.
Shared human reference inspected: icon_set/references/human_ref/full_body_ref.png;
this isolated hand has no head/body proportions or detached-head gap to measure.

Hosting (compose.py): heart valid; plus, check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'open-hand-palm'
SOURCE_PATH = 'icon_set/dist/failed/container64/open-hand-palm.svg'
AUTHOR = 'gpt-6'


class OpenHandPalm(Container64):
    icon_id = "open-hand-palm"
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ("raised-hand", "hand-palm-container")
    keywords = ("hand", "palm", "human", "greeting", "stop", "attention")

    def build(self) -> None:
        # Plan: rounded finger series above an open thumb web and broad palm.
        self.add_line('index-left', (18,28), (18,13))
        self.add_arc('index-tip', (18,13), (28,13), radius_x=5)
        self.add_line('middle-left', (28,13), (28,7))
        self.add_arc('middle-tip', (28,7), (38,7), radius_x=5)
        self.add_line('middle-right', (38,7), (38,13))
        self.add_arc('ring-tip', (38,13), (48,13), radius_x=5)
        self.add_line('ring-right', (48,13), (48,23))
        self.add_arc('little-tip', (48,23), (58,23), radius_x=5)
        self.add_line('palm-right', (58,23), (58,42))
        self.add_arc('palm-base-right', (58,42), (38,62), radius_x=20)
        # Circle centre (38,32), radius 30: the 3-4-5 point (14,50)
        # leaves the lower palm tangent to the thumb's diagonal side.
        self.add_arc('palm-base-left', (38,62), (14,50), radius_x=30)
        self.add_line('thumb-side', (14,50), (8,42))
        self.add_arc('thumb-heel', (8,42), (6,36), radius_x=10)
        self.add_arc('thumb-tip', (6,36), (16,36), radius_x=5)
        self.add_line('thumb-web', (16,36), (22,42))
        self.add_contour(
            'outline', 'index-left', 'index-tip', 'middle-left', 'middle-tip',
            'middle-right', 'ring-tip', 'ring-right', 'little-tip', 'palm-right',
            'palm-base-right', 'palm-base-left', 'thumb-side', 'thumb-heel',
            'thumb-tip', 'thumb-web', closed=False,
        )
        for x, top in ((28,13), (38,13), (48,23)):
            self.add_line(f'finger-crease-{x}', (x,top), (x,28))
            self.relate('connect', f'finger-crease-{x}', 'outline')
