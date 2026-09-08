"""An upright open hand encloses a broad palm below four rounded fingers.

User explicitly selected the container family for this subject.
VRECT_XL: visible (4,0)-(60,64), centerline extremes (6,2)-(58,62).
The tall keyshape fits the raised fingers and rounded palm. Lucide hand's
original and atomic-debug geometry inform semicircular fingertips, connected
finger creases and a coherent palm contour. The supplied batch_09 reference
sets the upright thumb, four finger heights and blank palm. All five digits
retained; no semantic detail removed. Thumb and staggered finger heights are
intentionally asymmetric. Authored directly on CONTAINER64.
Hosting measured with compose.py: plus passes, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class OpenHandPalm(Container64):
    icon_id = "open-hand-palm"
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ("raised-hand", "hand-palm-container")
    keywords = ("hand", "palm", "human", "greeting", "stop", "attention")

    def build(self) -> None:
        self.add_line('index-left', (18,38), (18,13))
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
        self.add_line('thumb-web', (16,36), (18,38))
        self.add_contour(
            'outline', 'index-left', 'index-tip', 'middle-left', 'middle-tip',
            'middle-right', 'ring-tip', 'ring-right', 'little-tip', 'palm-right',
            'palm-base-right', 'palm-base-left', 'thumb-side', 'thumb-heel',
            'thumb-tip', 'thumb-web', closed=True,
        )
        for x, top in ((28,13), (38,13), (48,23)):
            self.add_line(f'finger-crease-{x}', (x,top), (x,28))
            self.relate('connect', f'finger-crease-{x}', 'outline')
