"""Independent 32px profile of two-button-mouse.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '74af51b8-794a-4a67-b95c-616f408607d0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/computers/batch-03/mouse_74af51b8-794a-4a67-b95c-616f408607d0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('74af51b8-794a-4a67-b95c-616f408607d0', 'pictographic-primitives/computers/batch-03/mouse_74af51b8-794a-4a67-b95c-616f408607d0.svg'), ('dd2baaa6-8560-4803-ae47-3542cfdb8b76', 'pictographic-primitives/computers/batch-03/mouse_dd2baaa6-8560-4803-ae47-3542cfdb8b76.svg'))
PROFILE_SOURCE_KEYS = ('solo/two-button-mouse',)
SOLO_SOURCE_ICON_IDS = ('two-button-mouse',)
REFERENCE_EXPORT_SHA256 = '8e57f7ae41910079c91ec9c7f09868705317070d8afec6731494ae80db8a5244'

class DrawingVariant2(Sub32):
    icon_id = 'two-button-mouse-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'computers'
    categories = ('computers', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Mouse with round cap and bowl, horizontal button split and central upper divider. Construction reference: mouse."""
        self.add_arc('top', (4, 14), (28, 14), radius_x=12)
        self.add_line('right', (28, 14), (28, 18))
        self.add_arc('bottom', (28, 18), (4, 18), radius_x=12)
        self.add_line('left', (4, 18), (4, 14))
        self.add_contour('shell', 'top', 'right', 'bottom', 'left', closed=True)
        self.add_line('buttons', (4, 14), (28, 14))
        self.add_line('split', (16, 2), (16, 14))
        self.relate('connect', 'buttons', 'shell')
        self.relate('connect', 'split', 'shell')
        self.relate('connect', 'split', 'buttons')

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
