"""Independent 32px profile of slice.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a004a57a-6eea-490b-8683-cc169050a26a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/slice_a004a57a-6eea-490b-8683-cc169050a26a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a004a57a-6eea-490b-8683-cc169050a26a', 'pictographic-primitives/state/slice_a004a57a-6eea-490b-8683-cc169050a26a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/slice',)
SOLO_SOURCE_ICON_IDS = ('slice',)
REFERENCE_EXPORT_SHA256 = 'a13683073eeb717d606c2c545962d1d8c742beafe9328b8885f14906bba3639e'

class DrawingVariant2(Sub32):
    icon_id = 'slice-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circle containing three separated curved fragments of an inner ring. Construction reference: none."""
        circle(self, 'outer', 16, 16, 14)
        self.add_bezier('inner-a', (10, 12), ((11, 10), (13, 9), (15, 9)))
        self.add_bezier('inner-b', (22, 13), ((24, 15), (24, 17), (22, 19)))
        self.add_bezier('inner-c', (15, 23), ((12, 23), (11, 22), (10, 19)))

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
