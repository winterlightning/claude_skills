"""Independent 32px profile of heart-message-22-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2a3f04f0-a404-41db-90b7-a6ee5813413b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/messages bubble round heart_2a3f04f0-a404-41db-90b7-a6ee5813413b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2a3f04f0-a404-41db-90b7-a6ee5813413b', 'pictographic-primitives/symbol/messages bubble round heart_2a3f04f0-a404-41db-90b7-a6ee5813413b.svg'), ('147e6d81-0d21-49c9-8726-0fadea0fff54', 'pictographic-primitives/symbol/messages bubble with heart_147e6d81-0d21-49c9-8726-0fadea0fff54.svg'))
PROFILE_SOURCE_KEYS = ('solo/heart-message-22-solo', 'solo/heart-message-77-solo')
SOLO_SOURCE_ICON_IDS = ('heart-message-22-solo', 'heart-message-77-solo')
REFERENCE_EXPORT_SHA256 = '685847693ea0fd50c447b5ddb25d955415e53ba9e7894c68b3383fbb4da32c75'

class DrawingVariant2(Sub32):
    icon_id = 'heart-message-22-solo-profile32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Oval speech bubble, lower-left tail and closed heart; restore original oval enclosure. Construction reference: message-circle."""
        self.add_arc('bubble-top', (2, 14), (30, 14), radius_x=14, radius_y=12)
        self.add_bezier('bubble-br', (30, 14), ((30, 22), (22, 28), (12, 25)))
        self.add_polyline('tail', (12, 25), (4, 30), (7, 23))
        self.add_bezier('bubble-bl', (7, 23), ((4, 21), (2, 18), (2, 14)))
        self.add_contour('bubble', 'bubble-top', 'bubble-br')
        self.relate('connect', 'bubble', 'tail')
        self.relate('connect', 'tail', 'bubble-bl')
        self.relate('connect', 'bubble-bl', 'bubble')
        self.add_arc('heart-l', (10, 12), (16, 11), radius_x=4)
        self.add_arc('heart-r', (16, 11), (22, 12), radius_x=4)
        self.add_polyline('heart-tip', (22, 12), (16, 19), (10, 12))
        self.add_contour('heart-lobes', 'heart-l', 'heart-r')
        self.relate('connect', 'heart-lobes', 'heart-tip')

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
