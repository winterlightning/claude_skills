"""Independent 32px profile of rising-candlestick-chart-batch-023-03.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0baca945-4ec6-4025-95ae-cd2fad5c8bac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/trading_0baca945-4ec6-4025-95ae-cd2fad5c8bac.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0baca945-4ec6-4025-95ae-cd2fad5c8bac', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/trading_0baca945-4ec6-4025-95ae-cd2fad5c8bac.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rising-candlestick-chart-batch-023-03',)
SOLO_SOURCE_ICON_IDS = ('rising-candlestick-chart-batch-023-03',)
REFERENCE_EXPORT_SHA256 = 'd77513dca53491b44f429393093095e9266932f9596acf15e72b9f4e464ca7be'

class DrawingVariant2(Sub32):
    icon_id = 'rising-candlestick-chart-batch-023-03-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three ascending closed candlestick bodies, each retaining an upper and lower wick. Small-size treatment: Reduced three candlesticks to two while retaining their ascending placement and all four wicks. Construction reference: chart-candlestick: repeated rounded bodies and paired stems."""
        for i, (x, top) in enumerate(((2, 19), (22, 5))):
            box(self, f'body-{i}', x, top, x + 8, top + 8, 2)
            self.add_line(f'wick-top-{i}', (x + 4, top - 3), (x + 4, top))
            self.relate('connect', f'wick-top-{i}', f'body-{i}')
            self.add_line(f'wick-bottom-{i}', (x + 4, top + 8), (x + 4, top + 11))
            self.relate('connect', f'wick-bottom-{i}', f'body-{i}')

def box(s, n, l, t, r, b, k=3):
    if k == 0:
        s.add_polyline(n, (l, t), (r, t), (r, b), (l, b), (l, t))
        return
    points = [(l + k, t), (r - k, t), (r, t + k), (r, b - k), (r - k, b), (l + k, b), (l, b - k), (l, t + k)]
    members = []
    for i, p in enumerate(points):
        q = points[(i + 1) % 8]
        name = f'{n}-{i}'
        if i % 2:
            s.add_arc(name, p, q, radius_x=k)
        else:
            s.add_line(name, p, q)
        members.append(name)
    s.add_contour(n, *members, closed=True)

def circle(s, n, cx, cy, r):
    s.add_arc(n + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
    s.add_arc(n + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
    s.add_contour(n, n + '-top', n + '-bottom', closed=True)
