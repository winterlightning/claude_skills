"""Independent 32px profile of pie-chart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '27b9bc66-43e0-4dee-990c-b6f75f57c869'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/pie chart_27b9bc66-43e0-4dee-990c-b6f75f57c869.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('27b9bc66-43e0-4dee-990c-b6f75f57c869', 'pictographic-primitives/symbol/pie chart_27b9bc66-43e0-4dee-990c-b6f75f57c869.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pie-chart',)
SOLO_SOURCE_ICON_IDS = ('pie-chart',)
REFERENCE_EXPORT_SHA256 = 'a0c09bf05742b71400843abb583206d049ca056fc746145d89210265019c0594'

class DrawingVariant2(Sub32):
    icon_id = 'pie-chart-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Round pie chart divided into three sectors with one common center. Construction reference: chart-pie."""
        circle(self, 'pie', 16, 16, 14)
        for n, p in [('top', (16, 2)), ('left', (7, 26)), ('right', (25, 26))]:
            self.add_line(n, (16, 16), p)
            self.relate('connect', n, 'pie')
        for a, b in [('top', 'left'), ('top', 'right'), ('left', 'right')]:
            self.relate('connect', a, b)

def box(s, n, l, t, r, b, k=3):
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
