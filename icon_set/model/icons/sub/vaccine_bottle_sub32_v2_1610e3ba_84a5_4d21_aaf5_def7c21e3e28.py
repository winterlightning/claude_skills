"""Independent 32px profile of vaccine-bottle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1610e3ba-84a5-4d21-aaf5-def7c21e3e28'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/health/vaccine bottle_1610e3ba-84a5-4d21-aaf5-def7c21e3e28.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1610e3ba-84a5-4d21-aaf5-def7c21e3e28', 'pictographic-primitives/health/vaccine bottle_1610e3ba-84a5-4d21-aaf5-def7c21e3e28.svg'),)
PROFILE_SOURCE_KEYS = ('solo/vaccine-bottle',)
SOLO_SOURCE_ICON_IDS = ('vaccine-bottle',)
REFERENCE_EXPORT_SHA256 = 'c6e4bdc903938d4765736868d41653f30a8474b79ef2b52f8f2160dbca68d697'

class DrawingVariant2(Sub32):
    icon_id = 'vaccine-bottle-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    categories = ('health', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Vaccine vial with projecting lip, narrow neck, rounded shoulders, flat rounded base and liquid wave. Construction reference: none."""
        self.add_line('lip', (10, 2), (22, 2))
        self.add_line('neck-l', (12, 2), (12, 6))
        self.add_bezier('shoulder-l', (12, 6), ((12, 9), (4, 9), (4, 15)))
        self.add_line('side-l', (4, 15), (4, 26))
        self.add_arc('bl', (4, 26), (8, 30), radius_x=4, sweep=False)
        self.add_line('base', (8, 30), (24, 30))
        self.add_arc('br', (24, 30), (28, 26), radius_x=4, sweep=False)
        self.add_line('side-r', (28, 26), (28, 15))
        self.add_bezier('shoulder-r', (28, 15), ((28, 9), (20, 9), (20, 6)))
        self.add_line('neck-r', (20, 6), (20, 2))
        self.add_contour('bottle', 'neck-l', 'shoulder-l', 'side-l', 'bl', 'base', 'br', 'side-r', 'shoulder-r', 'neck-r')
        self.relate('connect', 'bottle', 'lip')
        self.add_bezier('liquid-a', (4, 20), ((8, 18), (12, 18), (16, 20)))
        self.add_bezier('liquid-b', (16, 20), ((20, 22), (24, 22), (28, 20)))
        self.add_contour('liquid', 'liquid-a', 'liquid-b')
        self.relate('connect', 'liquid', 'bottle')

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
