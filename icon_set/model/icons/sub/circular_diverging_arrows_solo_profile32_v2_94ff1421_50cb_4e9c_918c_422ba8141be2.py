"""Independent 32px profile of circular-diverging-arrows-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '94ff1421-50cb-4e9c-918c-422ba8141be2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/circle split arrow_94ff1421-50cb-4e9c-918c-422ba8141be2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('94ff1421-50cb-4e9c-918c-422ba8141be2', 'pictographic-primitives/other/circle split arrow_94ff1421-50cb-4e9c-918c-422ba8141be2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circular-diverging-arrows-solo',)
SOLO_SOURCE_ICON_IDS = ('circular-diverging-arrows-solo',)
REFERENCE_EXPORT_SHA256 = '27474575b3eee891d07b569f1a61abaf62fc2fa68cd225fb37edf54f84cd86ec'

class DrawingVariant2(Sub32):
    icon_id = 'circular-diverging-arrows-solo-profile32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Enclosing circle and two upward diverging curved arrows sharing a bottom origin. Construction reference: split."""
        circle(self, 'frame', 16, 16, 14)
        for name, end, c1, c2, pts in [('left', (10, 12), (16, 18), (13, 15), ((10, 16), (10, 12), (13, 12))), ('right', (22, 12), (16, 18), (19, 15), ((19, 12), (22, 12), (22, 16)))]:
            self.add_bezier(name, (16, 23), (c1, c2, end))
            self.add_polyline(name + '-head', *pts)
            self.relate('connect', name, name + '-head')
        self.relate('connect', 'left', 'right')

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
