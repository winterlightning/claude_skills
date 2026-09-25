"""Independent 32px profile of shield.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0fa98a0f-6de4-4ade-b905-178ec453bc23'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/protection/shield_0fa98a0f-6de4-4ade-b905-178ec453bc23.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0fa98a0f-6de4-4ade-b905-178ec453bc23', 'pictographic-primitives/protection/shield_0fa98a0f-6de4-4ade-b905-178ec453bc23.svg'), ('8e1100ca-39fe-4e71-b978-93997ec5e7d8', 'pictographic-primitives/protection/shield_8e1100ca-39fe-4e71-b978-93997ec5e7d8.svg'), ('ba7b0c51-fe87-48cd-a5c0-eea81086a3a9', 'pictographic-primitives/protection/shield_ba7b0c51-fe87-48cd-a5c0-eea81086a3a9.svg'), ('ee28756e-a560-4166-b776-2aebcbfcabaa', 'pictographic-primitives/protection/shield_ee28756e-a560-4166-b776-2aebcbfcabaa.svg'))
PROFILE_SOURCE_KEYS = ('solo/shield', 'solo/shield-8e1100ca', 'solo/shield-ba7b0c51', 'solo/shield-ee28756e')
SOLO_SOURCE_ICON_IDS = ('shield', 'shield-8e1100ca', 'shield-ba7b0c51', 'shield-ee28756e')
REFERENCE_EXPORT_SHA256 = '764b4ffc339d83132ae16c761a39500cf8cd920b49f9ed3a98e90510c1b8d4d8'

class DrawingVariant2(Sub32):
    icon_id = 'shield-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'protection'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Symmetric curved shield with domed top and pointed lower tip. Construction reference: shield."""
        self.add_bezier('top-l', (4, 6), ((8, 4), (12, 2), (16, 2)))
        self.add_bezier('top-r', (16, 2), ((20, 2), (24, 4), (28, 6)))
        self.add_line('side-r', (28, 6), (28, 17))
        self.add_bezier('bottom-r', (28, 17), ((28, 24), (21, 29), (16, 30)))
        self.add_bezier('bottom-l', (16, 30), ((11, 29), (4, 24), (4, 17)))
        self.add_line('side-l', (4, 17), (4, 6))
        self.add_contour('shield', 'top-l', 'top-r', 'side-r', 'bottom-r', 'bottom-l', 'side-l', closed=True)

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
