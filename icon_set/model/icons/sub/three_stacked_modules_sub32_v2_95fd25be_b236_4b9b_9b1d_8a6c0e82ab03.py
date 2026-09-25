"""Independent 32px profile of three-stacked-modules.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '95fd25be-b236-4b9b-9b1d-8a6c0e82ab03'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/programing/module three_95fd25be-b236-4b9b-9b1d-8a6c0e82ab03.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('95fd25be-b236-4b9b-9b1d-8a6c0e82ab03', 'pictographic-primitives/programing/module three_95fd25be-b236-4b9b-9b1d-8a6c0e82ab03.svg'), ('f9fae231-69ce-40f3-ac89-7b4fb7c79dfe', 'pictographic-primitives/programing/module three_f9fae231-69ce-40f3-ac89-7b4fb7c79dfe.svg'))
PROFILE_SOURCE_KEYS = ('solo/three-stacked-modules',)
SOLO_SOURCE_ICON_IDS = ('three-stacked-modules',)
REFERENCE_EXPORT_SHA256 = 'd2571284419ee4ff1bbc5566eece5a2a9217a5fdfe927300e17ef8de9d684884'

class DrawingVariant2(Sub32):
    icon_id = 'three-stacked-modules-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'programing'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three rounded squares: one above two equal lower modules. Construction reference: none."""
        for name, l, t in [('top', 11, 2), ('left', 2, 20), ('right', 20, 20)]:
            box(self, name, l, t, l + 10, t + 10, 2)

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
