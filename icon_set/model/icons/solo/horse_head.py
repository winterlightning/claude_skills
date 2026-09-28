"""A left-facing horse head with a pricked ear and a single broad mane band."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c3f914af-7c9b-4941-8e99-c5be9d251a91'
SOURCE_PATH = 'pictographic-primitives/animals/zebra head_c3f914af-7c9b-4941-8e99-c5be9d251a91.svg'
AUTHOR = 'gpt-6'

class HorseHead(Solo48):
    icon_id = 'horse-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ('equine-head',)
    keywords = ('horse', 'head', 'profile', 'mane', 'equine', 'pony', 'zebra')

    def _circle(self, name, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r, radius_y=ry)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r, radius_y=ry)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def _path(self, name, start, parts, closed=False):
        ids = []
        p = start
        for j, s in enumerate(parts):
            i = f'{name}-{j}'
            q = s[1]
            if s[0] == 'L':
                self.add_line(i, p, q)
            else:
                self.add_arc(i, p, q, radius_x=s[2], radius_y=s[3], sweep=s[4])
            ids.append(i)
            p = q
        self.add_contour(name, *ids, closed=closed)

    def build(self):
        points = [(6, 28), (6, 26), (22, 12), (18, 8), (18, 6), (28, 8)]
        for j, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f'forehead-{j}', a, b)
        self.add_line('poll', (28, 8), (38, 12))
        self.add_arc('poll-back', (38, 12), (42, 20), radius_x=4, radius_y=8, sweep=True)
        self.add_arc('mane-back', (42, 20), (34, 42), radius_x=40, radius_y=40, sweep=True)
        self.add_line('neck-1', (34, 42), (29, 40))
        self.add_line('neck-mid', (29, 40), (24, 34))
        self.add_line('neck-2', (24, 34), (10, 36))
        self.add_arc('muzzle', (10, 36), (6, 28), radius_x=4, radius_y=8, sweep=True)
        self.add_contour('outline', *[f'forehead-{i}' for i in range(1, 6)], 'poll', 'poll-back', 'mane-back', 'neck-1', 'neck-mid', 'neck-2', 'muzzle', closed=True)
        self.add_arc('mane-inner', (38, 12), (29, 40), radius_x=30, radius_y=30, sweep=False)
        self.relate('connect', 'mane-inner', 'outline')
        self.add_dot('eye', (21, 24))
