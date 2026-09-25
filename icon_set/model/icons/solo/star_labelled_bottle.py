"""Enlarge the bottle neck opening vertically and horizontally, shorten the shoulders, and center the simple star within the lower body. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e0f7f6c1-f633-5b90-9f71-aac0f4ec1dce'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/decoration bottle_e0f7f6c1-f633-5b90-9f71-aac0f4ec1dce.svg'
AUTHOR = 'gpt-6'

class StarLabelledBottle(Solo48):
    icon_id = 'star-labelled-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()

    def build(self) -> None:
        """Symbol plan: Enlarge the bottle neck opening vertically and horizontally, shorten the shoulders, and center the simple star within the lower body. Reference: inspected current parent; no useful exact Lucide match selected."""
        left, top, right, bottom, radius = (8, 18, 40, 44, 4)
        self.add_line('body-top', (left + radius, top), (right - radius, top))
        self.add_arc('body-tr', (right - radius, top), (right, top + radius), radius_x=radius)
        self.add_line('body-right', (right, top + radius), (right, bottom - radius))
        self.add_arc('body-br', (right, bottom - radius), (right - radius, bottom), radius_x=radius)
        self.add_line('body-bottom', (right - radius, bottom), (left + radius, bottom))
        self.add_arc('body-bl', (left + radius, bottom), (left, bottom - radius), radius_x=radius)
        self.add_line('body-left', (left, bottom - radius), (left, top + radius))
        self.add_arc('body-tl', (left, top + radius), (left + radius, top), radius_x=radius)
        self.add_contour('body', *('body-' + part for part in ('top', 'tr', 'right', 'br', 'bottom', 'bl', 'left', 'tl')), closed=True)
        self.add_polyline('neck', (14, 18), (14, 4), (34, 4), (34, 18))
        self.relate('connect', 'neck', 'body')
        tips = ((24, 27), (30, 30), (28, 35), (20, 35), (18, 30))
        for i, tip in enumerate(tips):
            self.add_line(f'star-{i}', (24, 32), tip)
            for j in range(i):
                self.relate('connect', f'star-{i}', f'star-{j}')
