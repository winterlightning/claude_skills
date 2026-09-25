"""Independent 32px profile of user-profile-selection-cursor-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '742a102d-2547-4878-9ea9-c64ad681d52b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/cursor head_742a102d-2547-4878-9ea9-c64ad681d52b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('742a102d-2547-4878-9ea9-c64ad681d52b', 'pictographic-primitives/other/cursor head_742a102d-2547-4878-9ea9-c64ad681d52b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/user-profile-selection-cursor-solo',)
SOLO_SOURCE_ICON_IDS = ('user-profile-selection-cursor-solo',)
REFERENCE_EXPORT_SHA256 = 'bc3f3f367b641f5add882cfef713d7fd0ac4bb34d099939cf15333f1ab3625f5'

class DrawingVariant2(Sub32):
    icon_id = 'user-profile-selection-cursor-solo-profile32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Open circular profile with a complete selection pointer and diagonal tail. Construction reference: shared typeface / geometric source construction."""
        self.add_arc('profile', (20, 6), (6, 20), radius_x=10, large_arc=True, sweep=False)
        self.add_polyline('pointer', (13, 13), (30, 20), (23, 23), (20, 30), (13, 13))
        self.add_line('tail', (23, 23), (30, 30))
        self.relate('connect', 'tail', 'pointer')

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
