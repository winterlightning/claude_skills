"""Segmented bamboo with right-growing leaf. VRECT_XL extremes 8,4–40,44. Lucide sprout informs paired leaf arcs. Natural asymmetry; retain one large leaf, omit small secondary leaf."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24d5cd60-39af-5c05-8539-a177110b1852'
SOURCE_PATH = 'pictographic-primitives/spas/spa bamboo_24d5cd60-39af-5c05-8539-a177110b1852.svg'
AUTHOR = 'gpt-6'

class BambooStalkWithLeaves(Solo48):
    icon_id = 'bamboo-stalk-with-leaves'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/wellness"
    aliases = ()
    keywords = ('spa', 'wellness', 'bamboo-stalk-with-leaves')

    def build(self):
        self.add_polyline('stalk', (8,44), (8,4), (20,4), (20,32), (20,44))
        for y in (17,32):
            self.add_line(f'node-{y}', (8,y), (20,y))
            self.relate('connect', 'stalk', f'node-{y}')
        self.add_line('branch', (20,32), (26,26))
        self.add_arc('leaf-top', (26,26), (40,12), radius_x=14)
        self.add_arc('leaf-bottom', (40,12), (26,26), radius_x=14)
        self.add_contour('leaf', 'leaf-top', 'leaf-bottom', closed=True)
        self.relate('connect', 'branch', 'stalk')
        self.relate('connect', 'branch', 'leaf')
