"""Move the glove cuff slightly left to follow the palm center and deepen the outer thumb bend; rebalance the wrist beneath the finger row.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '765f4935-d388-462f-ab4d-ad786a029631'
SOURCE_PATH = 'pictographic-primitives/sports/goalkeeper glove_765f4935-d388-462f-ab4d-ad786a029631.svg'
AUTHOR = 'gpt-6'

class GoalkeeperGloveSports(Solo48):
    icon_id = 'goalkeeper-glove-sports-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('goalkeeper', 'glove', 'soccer', 'football', 'hand', 'protection')

    def circle(self, name, x, y, r):
        self.add_arc(name + '-top', (x - r, y), (x + r, y), radius_x=r)
        self.add_arc(name + '-bottom', (x + r, y), (x - r, y), radius_x=r)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def skeleton(self, branches):
        parts = []
        for name, points in branches:
            members = []
            for index, (a, b) in enumerate(zip(points, points[1:])):
                key = f'{name}-{index}'
                members.append(key)
                self.add_line(key, a, b)
                parts.append((key, a, b))
            if len(members) > 1:
                self.add_contour(name, *members)
        for index, (a, p, q) in enumerate(parts):
            for b, r, s in parts[index + 1:]:
                if p in (r, s) or q in (r, s):
                    self.relate('connect', a, b)

    def rounded(self, name, x, y, w, h, r):
        pts = [(x + r, y), (x + w - r, y), (x + w, y + r), (x + w, y + h - r), (x + w - r, y + h), (x + r, y + h), (x, y + h - r), (x, y + r)]
        members = []
        for index, a in enumerate(pts):
            b = pts[(index + 1) % 8]
            key = f'{name}-{index}'
            members.append(key)
            if index % 2:
                self.add_arc(key, a, b, radius_x=r)
            else:
                self.add_line(key, a, b)
        self.add_contour(name, *members, closed=True)

    def weight(self, name, x, y, w, h, r):
        middle = y + h // 2
        pts = [(x + r, y), (x + w - r, y), (x + w, y + r), (x + w, middle), (x + w, y + h - r), (x + w - r, y + h), (x + r, y + h), (x, y + h - r), (x, middle), (x, y + r)]
        members = []
        for index, a in enumerate(pts):
            b = pts[(index + 1) % len(pts)]
            key = f'{name}-{index}'
            members.append(key)
            if index in [1, 4, 6, 9]:
                self.add_arc(key, a, b, radius_x=r)
            else:
                self.add_line(key, a, b)
        self.add_contour(name, *members, closed=True)

    def build(self):
        for i, x in enumerate([10, 18, 26, 34]):
            self.add_arc(f'finger-{i}', (x, 10), (x + 8, 10), radius_x=4)
        self.skeleton([('left', [(10, 10), (10, 22), (6, 22), (6, 26), (12, 34), (12, 42), (34, 42), (34, 34), (42, 26), (42, 10)]), ('cuff', [(12, 34), (34, 34)]), ('index-seam', [(18, 10), (18, 20)]), ('middle-seam', [(26, 10), (26, 20)]), ('ring-seam', [(34, 10), (34, 20)])])
        self.relate('connect', 'finger-0', 'left-0')
        self.relate('connect', 'finger-3', 'left-8')
        for i, n in enumerate(['index-seam', 'middle-seam', 'ring-seam']):
            for j in [i, i + 1]:
                self.relate('connect', n + '-0', f'finger-{j}')
        for i in range(3):
            self.relate('connect', f'finger-{i}', f'finger-{i + 1}')
    variant_of = 'goalkeeper-glove-sports'
    variant_label = 'Batch 01 centerline repair'
