"""Use a horizontal rectangle, straight walls, matching corner radii and centered chevron. User explicitly authorized the complete framed icon. Lucide construction: straight runs, mirrored chevrons, tangent equal-radius corners."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6b8a720f-0633-555e-8c23-fb7b13dda012'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow rectangle left_6b8a720f-0633-555e-8c23-fb7b13dda012.svg'
AUTHOR = 'gpt-6'

class ArrowRectangleLeftArrows(Solo48):
    icon_id = 'arrow-rectangle-left-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'rectangle', 'left', 'arrows')

    def build(self):
        left, top, right, bottom, radius = (4, 8, 44, 40, 4)
        self.add_line('top', (left + radius, top), (right - radius, top))
        self.add_arc('top-right', (right - radius, top), (right, top + radius), radius_x=radius)
        self.add_line('right', (right, top + radius), (right, bottom - radius))
        self.add_arc('bottom-right', (right, bottom - radius), (right - radius, bottom), radius_x=radius)
        self.add_line('bottom', (right - radius, bottom), (left + radius, bottom))
        self.add_arc('bottom-left', (left + radius, bottom), (left, bottom - radius), radius_x=radius)
        self.add_line('left', (left, bottom - radius), (left, top + radius))
        self.add_arc('top-left', (left, top + radius), (left + radius, top), radius_x=radius)
        self.add_contour('frame', 'top', 'top-right', 'right', 'bottom-right', 'bottom', 'bottom-left', 'left', 'top-left', closed=True)
        rotation = 1

        def point(x, y):
            for _ in range(rotation):
                x, y = (48 - y, x)
            return (x, y)
        a, tip, b = [point(x, y) for x, y in [(17, 20), (24, 28), (31, 20)]]
        self.add_line('head-a', a, tip)
        self.add_line('head-b', tip, b)
        self.add_contour('chevron', 'head-a', 'head-b')
