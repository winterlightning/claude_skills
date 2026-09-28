"""Independent 32px profile of vr-headset-video-games.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '427e8988-7e0f-4f0e-930b-42ce7a00bd27'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/vr headset_427e8988-7e0f-4f0e-930b-42ce7a00bd27.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('427e8988-7e0f-4f0e-930b-42ce7a00bd27', 'pictographic-primitives/video-games/vr headset_427e8988-7e0f-4f0e-930b-42ce7a00bd27.svg'),)
PROFILE_SOURCE_KEYS = ('solo/vr-headset-video-games',)
SOLO_SOURCE_ICON_IDS = ('vr-headset-video-games',)
REFERENCE_EXPORT_SHA256 = '8b696ecad104c8d91f8c3d2c8f79cfaa09bc696a421c41c38fc45e3fe12f67e5'

class DrawingVariant2(Sub32):
    icon_id = 'vr-headset-video-games-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'video-games'
    categories = ('video-games', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """VR goggles with gently domed top, round outer corners and central nose recess. Construction reference: none."""
        self.add_bezier('top-l', (2, 12), ((2, 5), (8, 4), (16, 4)))
        self.add_bezier('top-r', (16, 4), ((24, 4), (30, 5), (30, 12)))
        self.add_line('right', (30, 12), (30, 21))
        self.add_arc('br', (30, 21), (23, 28), radius_x=7)
        self.add_bezier('nose-r', (23, 28), ((20, 28), (19, 22), (16, 22)))
        self.add_bezier('nose-l', (16, 22), ((13, 22), (12, 28), (9, 28)))
        self.add_arc('bl', (9, 28), (2, 21), radius_x=7)
        self.add_line('left', (2, 21), (2, 12))
        self.add_contour('goggles', 'top-l', 'top-r', 'right', 'br', 'nose-r', 'nose-l', 'bl', 'left', closed=True)

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
