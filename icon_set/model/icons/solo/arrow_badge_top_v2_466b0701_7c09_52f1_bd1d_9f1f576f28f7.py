# Variant of arrow-badge-top; parent file remains unchanged.
"""Balanced arrow badge with straight edges and matching rear corner arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '466b0701-7c09-52f1-bd1d-9f1f576f28f7'
SOURCE_PATH = 'icons-json/arrows/arrow badge top_466b0701-7c09-52f1-bd1d-9f1f576f28f7.json'
AUTHOR = 'gpt-6'

class ArrowBadgeTopVariant2(Solo48):
    icon_id = 'arrow-badge-top-v2'
    variant_of = 'arrow-badge-top'
    variant_label = 'Straight edges and balanced outline'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'top', 'arrows')

    def build(self):
        # One closed badge, mirrored about x=24, then quarter-turned as a unit.
        # VRECT_L ink extremes (6,2)-(42,46); rear corners share radius 2.
        # Lucide bookmark informs straight walls and tangent circular corners.
        axis, half_width, back, shoulder, tip, radius = 24, 16, 4, 32, 44, 2
        left, right = axis - half_width, axis + half_width
        def point(x, y):
            return (48 - x, 48 - y)
        nodes = [point(left + radius, back), point(right - radius, back),
                 point(right, back + radius), point(right, shoulder),
                 point(axis, tip), point(left, shoulder),
                 point(left, back + radius)]
        self.add_line('back', nodes[0], nodes[1])
        self.add_arc('rear-right', nodes[1], nodes[2], radius_x=radius, sweep=True)
        self.add_line('right-side', nodes[2], nodes[3])
        self.add_line('right-tip', nodes[3], nodes[4])
        self.add_line('left-tip', nodes[4], nodes[5])
        self.add_line('left-side', nodes[5], nodes[6])
        self.add_arc('rear-left', nodes[6], nodes[0], radius_x=radius, sweep=True)
        self.add_contour('outline', 'back', 'rear-right', 'right-side',
                         'right-tip', 'left-tip', 'left-side', 'rear-left', closed=True)
