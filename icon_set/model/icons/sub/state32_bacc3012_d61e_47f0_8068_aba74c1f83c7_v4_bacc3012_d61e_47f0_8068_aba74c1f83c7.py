"""Independent 32px profile of state32-bacc3012-d61e-47f0-8068-aba74c1f83c7.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'bacc3012-d61e-47f0-8068-aba74c1f83c7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/circle R_bacc3012-d61e-47f0-8068-aba74c1f83c7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bacc3012-d61e-47f0-8068-aba74c1f83c7', 'pictographic-primitives/state/circle R_bacc3012-d61e-47f0-8068-aba74c1f83c7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-r',)
SOLO_SOURCE_ICON_IDS = ('circle-r',)
REFERENCE_EXPORT_SHA256 = '38a11656f54ee6ff5d6eee39c65dc436947790c4d57343173b90260348bce589'

class DrawingVariant4(Sub32):
    icon_id = 'state32-bacc3012-d61e-47f0-8068-aba74c1f83c7-v4'
    variant_of = 'state32-bacc3012-d61e-47f0-8068-aba74c1f83c7-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Registered trademark: complete circular outline, original R bowl, stem and long diagonal leg. Construction reference: Original source composition; clean contour construction."""
        circle(self, 'ring', 16, 16, 14)
        from icon_set.typeface.sub32 import draw_registered_r
        draw_registered_r(self)

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
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase',)

TYPEFACE_PROFILE_VARIANTS = ('letter-r-registered32',)
