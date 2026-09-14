"""A heavy boxing bag hangs from a short suspension beneath a beam.

Replaced the tiny triangular hanger with a beam and short chain to retain a tall, recognizable bag within the live keyshape.
Source establishes a hanging heavy bag; geometric capsule and shared vertical axis, with no useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9e7027bc-55fb-5645-8aae-23b189e7f236'
SOURCE_PATH = 'pictographic-primitives/sports/boxing bag hanging_9e7027bc-55fb-5645-8aae-23b189e7f236.svg'
AUTHOR = 'gpt-6'

class HangingBoxingBagVariant2(Solo48):
    icon_id = 'hanging-boxing-bag-v2'
    variant_of = 'hanging-boxing-bag'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('hanging', 'boxing', 'bag')

    def circle(self, name, x, y, radius):
        self.add_arc(name + '-top', (x - radius, y), (x + radius, y), radius_x=radius)
        self.add_arc(name + '-bottom', (x + radius, y), (x - radius, y), radius_x=radius)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def skeleton(self, branches):
        segments = []
        for name, points in branches:
            for index, (a, b) in enumerate(zip(points, points[1:])):
                key = f'{name}-{index}'
                self.add_line(key, a, b)
                segments.append((key, a, b))
            if len(points) > 2:
                self.add_contour(name, *[f'{name}-{i}' for i in range(len(points) - 1)])
        for index, (a, p, q) in enumerate(segments):
            for b, r, s in segments[index + 1:]:
                if p in (r, s) or q in (r, s):
                    self.relate('connect', a, b)

    def oval(self, name, x, y, rx, ry):
        self.add_arc(name + '-top', (x - rx, y), (x + rx, y), radius_x=rx, radius_y=ry)
        self.add_arc(name + '-bottom', (x + rx, y), (x - rx, y), radius_x=rx, radius_y=ry)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def build(self):
        self.skeleton([('beam', [(8, 4), (24, 4), (40, 4)]), ('chain', [(24, 4), (24, 16)])])
        self.add_line('bag-top-left', (20, 16), (24, 16))
        self.add_line('bag-top-right', (24, 16), (28, 16))
        self.add_arc('bag-tr', (28, 16), (34, 22), radius_x=6)
        self.add_line('bag-right', (34, 22), (34, 34))
        self.add_arc('bag-bottom', (34, 34), (14, 34), radius_x=10)
        self.add_line('bag-left', (14, 34), (14, 22))
        self.add_arc('bag-tl', (14, 22), (20, 16), radius_x=6)
        self.add_contour('bag', 'bag-top-left', 'bag-top-right', 'bag-tr', 'bag-right', 'bag-bottom', 'bag-left', 'bag-tl', closed=True)
        for part in ['bag-top-left', 'bag-top-right']:
            self.relate('connect', 'chain-0', part)
