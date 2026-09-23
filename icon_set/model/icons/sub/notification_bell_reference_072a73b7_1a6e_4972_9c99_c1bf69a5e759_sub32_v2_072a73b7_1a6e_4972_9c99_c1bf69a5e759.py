"""Independent 32px profile of notification-bell-reference-072a73b7-1a6e-4972-9c99-c1bf69a5e759.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '072a73b7-1a6e-4972-9c99-c1bf69a5e759'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/alarm bell_072a73b7-1a6e-4972-9c99-c1bf69a5e759.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('072a73b7-1a6e-4972-9c99-c1bf69a5e759', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/alarm bell_072a73b7-1a6e-4972-9c99-c1bf69a5e759.svg'), ('85384c6e-0df4-408f-bf41-58882794cc0a', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/alarm bell_85384c6e-0df4-408f-bf41-58882794cc0a.svg'))
PROFILE_SOURCE_KEYS = ('solo/notification-bell-reference-072a73b7-1a6e-4972-9c99-c1bf69a5e759', 'solo/notification-bell-reference-85384c6e-0df4-408f-bf41-58882794cc0a')
SOLO_SOURCE_ICON_IDS = ('notification-bell-reference-072a73b7-1a6e-4972-9c99-c1bf69a5e759', 'notification-bell-reference-85384c6e-0df4-408f-bf41-58882794cc0a')
REFERENCE_EXPORT_SHA256 = '0ef6b411da6b7386ef6749579636e81996fb3979e24ac16b1ff798c94f810608'

class DrawingVariant2(Sub32):
    icon_id = 'notification-bell-reference-072a73b7-1a6e-4972-9c99-c1bf69a5e759-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Bell canopy with pointed crown, flared hem and detached curved clapper. Construction reference: bell."""
        self.add_bezier('crown-l', (16, 2), ((13, 4), (7, 4), (7, 11)))
        self.add_bezier('skirt-l', (7, 11), ((7, 16), (5, 20), (2, 21)))
        self.add_line('hem', (2, 21), (30, 21))
        self.add_bezier('skirt-r', (30, 21), ((27, 20), (25, 16), (25, 11)))
        self.add_bezier('crown-r', (25, 11), ((25, 4), (19, 4), (16, 2)))
        self.add_contour('bell', 'crown-l', 'skirt-l', 'hem', 'skirt-r', 'crown-r', closed=True)
        self.add_arc('clapper', (12, 28), (20, 28), radius_x=5, sweep=False)

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
