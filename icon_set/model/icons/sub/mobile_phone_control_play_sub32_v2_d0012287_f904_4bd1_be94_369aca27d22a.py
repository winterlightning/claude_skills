"""Independent 32px profile of mobile-phone-control-play.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd0012287-f904-4bd1-be94-369aca27d22a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/mobile phone control play_d0012287-f904-4bd1-be94-369aca27d22a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d0012287-f904-4bd1-be94-369aca27d22a', 'pictographic-primitives/state/mobile phone control play_d0012287-f904-4bd1-be94-369aca27d22a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mobile-phone-control-play',)
SOLO_SOURCE_ICON_IDS = ('mobile-phone-control-play',)
REFERENCE_EXPORT_SHA256 = '8a6e70040bac9b1e07cb53acbab666753626bb3bb9e43c2bcd30a94088ff1387'

class DrawingVariant2(Sub32):
    icon_id = 'mobile-phone-control-play-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Closed phone frame, separate closed play triangle and footer divider. Small-size treatment: Removed the footer divider to give the closed play triangle a clear opening. Construction reference: smartphone: closed rounded enclosure and footer."""
        box(self, 'phone', 4, 2, 28, 30, 4)
        self.add_polyline('play', (12, 9), (21, 16), (12, 23), (12, 9))

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
