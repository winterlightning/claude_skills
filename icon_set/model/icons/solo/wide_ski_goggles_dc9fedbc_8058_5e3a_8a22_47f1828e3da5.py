"""A broad single ski lens with a deep rounded nose notch; omit reflections.

Lucide construction: no useful exact match; paired quarter ellipses form the outline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc9fedbc-8058-5e3a-8a22-47f1828e3da5'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/glasses ski_dc9fedbc-8058-5e3a-8a22-47f1828e3da5.svg'
AUTHOR = 'gpt-6'


class WideSkiGoggles(Solo48):
    icon_id = 'wide-ski-goggles'
    keyshape = Keyshape.HRECT_S
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('goggles', 'ski goggles', 'snow', 'ski', 'eyewear', 'winter', 'sports', 'visor')

    def build(self) -> None:
        # Exact keyshape envelope: (0, 12, 48, 36).
        self.add_line('top', (8, 8), (40, 8))
        self.add_arc('tr', (40, 8), (44, 14), radius_x=4, radius_y=6, sweep=True)
        self.add_line('right', (44, 14), (44, 32))
        self.add_arc('br', (44, 32), (38, 40), radius_x=6, radius_y=8, sweep=True)
        self.add_arc('nose-r-low', (38, 40), (31, 34), radius_x=7, radius_y=6, sweep=True)
        self.add_arc('nose-r-high', (31, 34), (24, 26), radius_x=7, radius_y=8, sweep=False)
        self.add_arc('nose-l-high', (24, 26), (17, 34), radius_x=7, radius_y=8, sweep=False)
        self.add_arc('nose-l-low', (17, 34), (10, 40), radius_x=7, radius_y=6, sweep=True)
        self.add_arc('bl', (10, 40), (4, 32), radius_x=6, radius_y=8, sweep=True)
        self.add_line('left', (4, 32), (4, 14))
        self.add_arc('tl', (4, 14), (8, 8), radius_x=4, radius_y=6, sweep=True)
        self.add_contour('lens', 'top', 'tr', 'right', 'br', 'nose-r-low', 'nose-r-high', 'nose-l-high', 'nose-l-low', 'bl', 'left', 'tl', closed=True)
