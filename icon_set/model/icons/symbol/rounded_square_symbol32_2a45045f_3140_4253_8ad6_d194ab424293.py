"""Simple Rounded Square Frame on SYMBOL32.

Plan: One rounded square owns side length and the four equal corner radii. Lucide square supplies tangent quarter-circle corners.
Centerline extremes use the SQUARE contract; all coordinates are authored at 32px.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '2a45045f-3140-4253-8ad6-d194ab424293'
SOURCE_PATH = 'published/gallery/combination-originals/2a45045f-3140-4253-8ad6-d194ab424293.svg'
AUTHOR = 'gpt-6'


class Drawing(Symbol32):
    icon_id = 'rounded-square-symbol32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ('Simple Rounded Square Frame',)
    keywords = ('symbol', 'container content')

    def build(self):

        low, high, radius = 2, 30, 4
        points = [(low + radius, low), (high - radius, low), (high, low + radius),
                  (high, high - radius), (high - radius, high), (low + radius, high),
                  (low, high - radius), (low, low + radius)]
        members = []
        for index, start in enumerate(points):
            end = points[(index + 1) % len(points)]
            name = f'edge-{index}'
            if index % 2:
                self.add_arc(name, start, end, radius_x=radius)
            else:
                self.add_line(name, start, end)
            members.append(name)
        self.add_contour('outline', *members, closed=True)
