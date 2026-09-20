"""Independent 32px profile of syringe.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '61c17587-0f1d-4e91-91d5-9bd53083e084'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/syringe_61c17587-0f1d-4e91-91d5-9bd53083e084.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('61c17587-0f1d-4e91-91d5-9bd53083e084', 'pictographic-primitives/symbol/syringe_61c17587-0f1d-4e91-91d5-9bd53083e084.svg'),)
PROFILE_SOURCE_KEYS = ('solo/syringe',)
SOLO_SOURCE_ICON_IDS = ('syringe',)
REFERENCE_EXPORT_SHA256 = 'efa2fcbd36912863a66e5123405fa1fceecf4ed585ed4ed196ff2bac591fd766'

class DrawingVariant2(Sub32):
    icon_id = 'syringe-sub32-v2'
    variant_of = 'syringe-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Diagonal syringe with rounded barrel, needle, plunger shaft and cap. Construction reference: syringe: rounded barrel and separate plunger."""
        self.add_polyline('barrel', (6, 18), (16, 8), (24, 16), (14, 26))
        self.add_bezier('nose-l', (14, 26), ((11, 29), (9, 29), (6, 26)))
        self.add_bezier('nose-r', (6, 26), ((3, 23), (3, 21), (6, 18)))
        self.add_contour('nose', 'nose-l', 'nose-r')
        self.relate('connect', 'nose', 'barrel')
        self.add_line('needle', (6, 26), (2, 30))
        self.relate('connect', 'needle', 'nose')
        self.add_line('plunger', (20, 12), (27, 5))
        self.relate('connect', 'plunger', 'barrel')
        self.add_line('cap', (24, 2), (30, 8))
        self.relate('connect', 'cap', 'plunger')

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
