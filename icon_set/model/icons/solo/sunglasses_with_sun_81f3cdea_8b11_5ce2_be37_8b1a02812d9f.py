"""Rounded sunglasses with upper-right sun. SQUARE (2,2)-(46,46) makes space for both subjects. Lucide glasses informed equal lenses and bridge. Three widely spaced rays replace the dense halo; temples omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81f3cdea-8b11-5ce2-be37-8b1a02812d9f'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/glasses sun_81f3cdea-8b11-5ce2-be37-8b1a02812d9f.svg'
AUTHOR = 'astra-chatgpt'


class SunglassesWithSun(Solo48):
    icon_id = 'sunglasses-with-sun'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('sunglasses', 'sun', 'shades', 'summer', 'eyewear', 'glasses', 'holiday', 'beach')

    def build(self) -> None:
        self.add_line('lens-left0', (7, 30), (15, 30))
        self.add_arc('lens-left1', (15, 30), (20, 35), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('lens-left2', (20, 35), (20, 41))
        self.add_arc('lens-left3', (20, 41), (15, 46), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('lens-left4', (15, 46), (7, 46))
        self.add_arc('lens-left5', (7, 46), (2, 41), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('lens-left6', (2, 41), (2, 35))
        self.add_arc('lens-left7', (2, 35), (7, 30), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('lens-left', 'lens-left0', 'lens-left1', 'lens-left2', 'lens-left3', 'lens-left4', 'lens-left5', 'lens-left6', 'lens-left7', closed=True)
        self.add_line('lens-right0', (33, 30), (41, 30))
        self.add_arc('lens-right1', (41, 30), (46, 35), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('lens-right2', (46, 35), (46, 41))
        self.add_arc('lens-right3', (46, 41), (41, 46), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('lens-right4', (41, 46), (33, 46))
        self.add_arc('lens-right5', (33, 46), (28, 41), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('lens-right6', (28, 41), (28, 35))
        self.add_arc('lens-right7', (28, 35), (33, 30), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('lens-right', 'lens-right0', 'lens-right1', 'lens-right2', 'lens-right3', 'lens-right4', 'lens-right5', 'lens-right6', 'lens-right7', closed=True)
        self.add_line('bridge', (20, 35), (28, 35))
        self.relate("connect", 'lens-left', 'bridge')
        self.relate("connect", 'lens-right', 'bridge')
        self.add_arc('sun-right', (33, 10), (33, 16), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('sun-left', (33, 16), (33, 10), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('sun', 'sun-right', 'sun-left', closed=True)
        self.add_line('ray-top', (33, 2), (33, 3))
        self.add_line('ray-left', (22, 13), (23, 13))
        self.add_line('ray-right', (43, 13), (44, 13))
