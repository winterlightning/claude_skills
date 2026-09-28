"""Independent 32px profile of smart-car-wi-fi-connection-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f59286ba-b86a-4e53-9fe0-93f931efec10'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/car wifi_f59286ba-b86a-4e53-9fe0-93f931efec10.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f59286ba-b86a-4e53-9fe0-93f931efec10', 'pictographic-primitives/other/car wifi_f59286ba-b86a-4e53-9fe0-93f931efec10.svg'),)
PROFILE_SOURCE_KEYS = ('solo/smart-car-wi-fi-connection-solo',)
SOLO_SOURCE_ICON_IDS = ('smart-car-wi-fi-connection-solo',)
REFERENCE_EXPORT_SHA256 = '83330e909c95140182b492c4da83a49c167d67240f89ba29d0bc9c5c1f8618af'

class DrawingVariant2(Sub32):
    icon_id = 'smart-car-wi-fi-connection-solo-profile32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Connected car with wireless arc, windshield silhouette and two wheel stems. Construction reference: car / wifi: one clear wireless arc above the car."""
        self.add_arc('wireless', (8, 6), (24, 6), radius_x=8, radius_y=4)
        self.add_polyline('car', (2, 26), (2, 18), (7, 18), (10, 12), (22, 12), (25, 18), (30, 18), (30, 26), (2, 26))
        for n, x in [('left', 6), ('right', 26)]:
            self.add_line(n + '-wheel', (x, 26), (x, 30))
            self.relate('connect', n + '-wheel', 'car')

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
