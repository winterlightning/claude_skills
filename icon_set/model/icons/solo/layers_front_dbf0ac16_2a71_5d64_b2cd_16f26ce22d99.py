"""Two overlapping rounded squares, with the lower-right layer in front. Repaired in place from bad-stroke feedback."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dbf0ac16-2a71-5d64-b2cd-16f26ce22d99'
SOURCE_PATH = 'pictographic-primitives/design/layers front_dbf0ac16-2a71-5d64-b2cd-16f26ce22d99.svg'
AUTHOR = 'gpt-6'

class LayersFront(Solo48):
    icon_id = 'layers-front'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('layers', 'front', 'design')

    def build(self) -> None:
        # Two equal rounded squares offset by 10, with the rear square occluded.
        # Lucide copy informs consistent radii and a clean uninterrupted front.
        # SQUARE centerline extremes: (6, 6)-(42, 42).
        radius, size, offset = 4, 26, 10
        left, top = 6 + offset, 6 + offset
        right, bottom = left + size, top + size
        self.add_line('front-top-a', (left + radius, top), (32, top))
        self.add_line('front-top-b', (32, top), (right - radius, top))
        self.add_arc('front-tr', (right - radius, top), (right, top + radius), radius_x=radius)
        self.add_line('front-right', (right, top + radius), (right, bottom - radius))
        self.add_arc('front-br', (right, bottom - radius), (right - radius, bottom), radius_x=radius)
        self.add_line('front-bottom', (right - radius, bottom), (left + radius, bottom))
        self.add_arc('front-bl', (left + radius, bottom), (left, bottom - radius), radius_x=radius)
        self.add_line('front-left-a', (left, bottom - radius), (left, 32))
        self.add_line('front-left-b', (left, 32), (left, top + radius))
        self.add_arc('front-tl', (left, top + radius), (left + radius, top), radius_x=radius)
        self.add_contour('front', 'front-top-a', 'front-top-b', 'front-tr', 'front-right', 'front-br',
                         'front-bottom', 'front-bl', 'front-left-a', 'front-left-b', 'front-tl', closed=True)
        self.add_line('back-right', (32, 16), (32, 10))
        self.add_arc('back-tr', (32, 10), (28, 6), radius_x=radius, sweep=False)
        self.add_line('back-top', (28, 6), (10, 6))
        self.add_arc('back-tl', (10, 6), (6, 10), radius_x=radius, sweep=False)
        self.add_line('back-left', (6, 10), (6, 28))
        self.add_arc('back-bl', (6, 28), (10, 32), radius_x=radius, sweep=False)
        self.add_line('back-bottom', (10, 32), (16, 32))
        self.add_contour('back', 'back-right', 'back-tr', 'back-top', 'back-tl',
                         'back-left', 'back-bl', 'back-bottom')
        self.relate('connect', 'back', 'front')
