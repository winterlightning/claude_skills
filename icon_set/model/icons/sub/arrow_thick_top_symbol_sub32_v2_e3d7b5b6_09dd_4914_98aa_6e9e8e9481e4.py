# Independent repair; parent preserved.
"""Independent 32px profile of arrow-thick-top-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e3d7b5b6-09dd-4914-98aa-6e9e8e9481e4'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow thick top_e3d7b5b6-09dd-4914-98aa-6e9e8e9481e4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3d7b5b6-09dd-4914-98aa-6e9e8e9481e4', 'pictographic-primitives/symbol/arrow thick top_e3d7b5b6-09dd-4914-98aa-6e9e8e9481e4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-thick-top-symbol',)
SOLO_SOURCE_ICON_IDS = ('arrow-thick-top-symbol',)
REFERENCE_EXPORT_SHA256 = '7690b702c11ba7e4cb38754a98175ca6e2d7343c3152d11919603615570f48ae'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'arrow-thick-top-symbol-sub32-v2'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        axis = 16
        half_stem = 6
        half_head = 12
        self.add_polyline('arrow', (axis - half_head, 16), (axis, 2), (axis + half_head, 16), (axis + half_stem, 16), (axis + half_stem, 30), (axis - half_stem, 30), (axis - half_stem, 16), closed=True)

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
REPAIR_PLAN = 'Up arrow; common axis and mirrored shoulders, constant-width stem.'
CONSTRUCTION_REFERENCE = 'arrow-big-up'
