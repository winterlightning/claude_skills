"""A broad single ski lens with a deep rounded nose notch; omit reflections.

Lucide construction: no useful exact match; paired quarter ellipses form the outline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc9fedbc-8058-5e3a-8a22-47f1828e3da5'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/glasses ski_dc9fedbc-8058-5e3a-8a22-47f1828e3da5.svg'
AUTHOR = 'astra-chatgpt'


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
        self.add_line('top', (8, 14), (40, 14))
        self.add_arc('tr', (40, 14), (46, 20), radius_x=6, radius_y=6, sweep=True)
        self.add_line('right', (46, 20), (46, 26))
        self.add_arc('br', (46, 26), (38, 34), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('nose-r-low', (38, 34), (31, 28), radius_x=7, radius_y=6, sweep=True)
        self.add_arc('nose-r-high', (31, 28), (24, 22), radius_x=7, radius_y=6, sweep=False)
        self.add_arc('nose-l-high', (24, 22), (17, 28), radius_x=7, radius_y=6, sweep=False)
        self.add_arc('nose-l-low', (17, 28), (10, 34), radius_x=7, radius_y=6, sweep=True)
        self.add_arc('bl', (10, 34), (2, 26), radius_x=8, radius_y=8, sweep=True)
        self.add_line('left', (2, 26), (2, 20))
        self.add_arc('tl', (2, 20), (8, 14), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('lens', 'top', 'tr', 'right', 'br', 'nose-r-low', 'nose-r-high', 'nose-l-high', 'nose-l-low', 'bl', 'left', 'tl', closed=True)
