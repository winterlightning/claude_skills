"""Independent 32px profile of hryvnia-sign.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5afaf6ee-841d-4918-940a-7de550ac7754'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/hryvnia sign_5afaf6ee-841d-4918-940a-7de550ac7754.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5afaf6ee-841d-4918-940a-7de550ac7754', 'pictographic-primitives/symbol/hryvnia sign_5afaf6ee-841d-4918-940a-7de550ac7754.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hryvnia-sign',)
SOLO_SOURCE_ICON_IDS = ('hryvnia-sign',)
REFERENCE_EXPORT_SHA256 = 'b9e1434df29b434468c4b6ea403b86c765d4f5b0fa3c6b4c140ac39778b8f14c'

class DrawingVariant3(Sub32):
    icon_id = 'hryvnia-sign-sub32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Hryvnia: reverse-S with two crossbars and a smooth diagonal middle. Construction reference: source composition; shared small-size character construction."""
        from icon_set.typeface.sub32 import draw_hryvnia
        draw_hryvnia(self)

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
TYPEFACE_GLYPH_IDS = ('symbol-hryvnia',)

TYPEFACE_PROFILE_VARIANTS = ('symbol-hryvnia-compact32',)
