"""Independent 32px profile of two-prong-electrical-plug.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0a5f79fb-077b-4a74-b852-967b66a0f12e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/plug_0a5f79fb-077b-4a74-b852-967b66a0f12e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0a5f79fb-077b-4a74-b852-967b66a0f12e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/plug_0a5f79fb-077b-4a74-b852-967b66a0f12e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/two-prong-electrical-plug',)
SOLO_SOURCE_ICON_IDS = ('two-prong-electrical-plug',)
REFERENCE_EXPORT_SHA256 = 'adbf25caff4acf5316d860bc89ebf43d1cfe8d54f54064296d0f68768e881e1a'

class DrawingVariant2(Sub32):
    icon_id = 'two-prong-electrical-plug-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two pins, flat rim, rounded plug bowl and bottom wire. Construction reference: plug."""
        self.add_line('rim', (4, 12), (28, 12))
        self.add_line('side-r', (28, 12), (28, 16))
        self.add_arc('bowl', (28, 16), (4, 16), radius_x=12, radius_y=8)
        self.add_line('side-l', (4, 16), (4, 12))
        self.add_contour('body', 'rim', 'side-r', 'bowl', 'side-l', closed=True)
        for x in (10, 22):
            self.add_line(f'pin-{x}', (x, 2), (x, 12))
            self.relate('connect', f'pin-{x}', 'body')
        self.add_line('wire', (16, 24), (16, 30))
        self.relate('connect', 'wire', 'body')

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
