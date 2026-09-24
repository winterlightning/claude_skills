"""Independent 32px profile of circle-skip-forward-button-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7de072ea-141a-4a2a-9bfe-5d555c9500af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/circle button next_7de072ea-141a-4a2a-9bfe-5d555c9500af.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7de072ea-141a-4a2a-9bfe-5d555c9500af', 'pictographic-primitives/other/circle button next_7de072ea-141a-4a2a-9bfe-5d555c9500af.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-skip-forward-button-solo',)
SOLO_SOURCE_ICON_IDS = ('circle-skip-forward-button-solo',)
REFERENCE_EXPORT_SHA256 = 'fcfe0047f537e4f077d475f573800958eeecd1d46c71a2f89e0f24f45a8b6d2a'

class DrawingVariant2(Sub32):
    icon_id = 'circle-skip-forward-button-solo-profile32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circular frame, separate closed right-pointing triangle and vertical stop bar. Small-size treatment: Removed the circular enclosure; retained the closed play triangle and separate stop bar. Construction reference: circle-skip-forward: full frame and two distinct controls."""
        self.add_polyline('triangle', (2, 2), (22, 16), (2, 30), (2, 2))
        self.add_line('stop', (30, 2), (30, 30))

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
