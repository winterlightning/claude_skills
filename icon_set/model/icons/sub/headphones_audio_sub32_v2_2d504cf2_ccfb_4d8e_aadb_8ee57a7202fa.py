"""Independent 32px profile of headphones-audio.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/audio/headphones_2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa', 'pictographic-primitives/audio/headphones_2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa.svg'),)
PROFILE_SOURCE_KEYS = ('solo/headphones-audio',)
SOLO_SOURCE_ICON_IDS = ('headphones-audio',)
REFERENCE_EXPORT_SHA256 = 'e2617c7a7bb7675b49c11b8b9de23adbf6bf8c7ab84629f7007d497252e869de'

class DrawingVariant2(Sub32):
    icon_id = 'headphones-audio-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'audio'
    categories = ('audio', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded headphone arch and two open rectangular ear cups. Construction reference: headphones."""
        self.add_arc('arch', (2, 16), (30, 16), radius_x=14)
        for side, x in [('left', 2), ('right', 30)]:
            self.add_line(side, (x, 16), (x, 22))
            self.relate('connect', side, 'arch')
        box(self, 'cup-l', 2, 20, 10, 30, 2)
        box(self, 'cup-r', 22, 20, 30, 30, 2)
        self.relate('connect', 'cup-l', 'left')
        self.relate('connect', 'cup-r', 'right')

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
