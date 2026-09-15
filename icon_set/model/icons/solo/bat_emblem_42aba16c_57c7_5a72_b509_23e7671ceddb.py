"""Curve the outer wing shoulders and keep the paired lower scallops symmetric. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '42aba16c-57c7-5a72-b509-23e7671ceddb'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/batman_42aba16c-57c7-5a72-b509-23e7671ceddb.svg'
AUTHOR = 'gpt-6'

class BatEmblem(Solo48):
    icon_id = 'bat-emblem'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/gaming'
    aliases = ()
    keywords = ('batman', 'bat', 'emblem', 'superhero', 'logo', 'comic', 'hero', 'dc')

    def build(self):
        """Symbol plan: Curve the outer wing shoulders and keep the paired lower scallops symmetric. Reference: inspected current parent; no useful exact Lucide match selected."""

        def circle(name, x, y, r):
            self.add_arc(name + '-a', (x, y - r), (x, y + r), radius_x=r)
            self.add_arc(name + '-b', (x, y + r), (x, y - r), radius_x=r)
            self.add_contour(name, name + '-a', name + '-b', closed=True)

        def arc(name, a, b, r, ry=None, sweep=True):
            self.add_arc(name, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)

        def poly(name, *pts):
            for i, (a, b) in enumerate(zip(pts, pts[1:]), 1):
                self.add_line(f'{name}-{i}', a, b)
        self.add_bezier('crown-1', (4, 26), ((4, 20), (7, 13), (9, 8)))
        self.add_bezier('crown-2', (9, 8), ((9, 14), (11, 18), (14, 18)))
        poly('middle', (14, 18), (19, 18), (20, 10), (24, 14), (28, 10), (29, 18), (34, 18))
        self.add_bezier('crown-9', (34, 18), ((37, 18), (39, 14), (39, 8)))
        self.add_bezier('crown-10', (39, 8), ((41, 13), (44, 20), (44, 26)))
        arc('right-lower', (44, 26), (38, 35), 10)
        arc('right-scallop', (38, 35), (28, 31), 8, sweep=False)
        poly('tail', (28, 31), (24, 40), (20, 31))
        arc('left-scallop', (20, 31), (10, 35), 8, sweep=False)
        arc('left-lower', (10, 35), (4, 26), 10)
        self.add_contour('bat', 'crown-1', 'crown-2', *[f'middle-{i}' for i in range(1, 7)], 'crown-9', 'crown-10', 'right-lower', 'right-scallop', 'tail-1', 'tail-2', 'left-scallop', 'left-lower', closed=True)
