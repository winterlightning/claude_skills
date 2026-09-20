"""Independent 32px profile of wifi.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9c4f27d2-9a43-4e9d-867c-e102edd9f1b9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/networks/wifi_9c4f27d2-9a43-4e9d-867c-e102edd9f1b9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9c4f27d2-9a43-4e9d-867c-e102edd9f1b9', 'pictographic-primitives/networks/wifi_9c4f27d2-9a43-4e9d-867c-e102edd9f1b9.svg'), ('b2468acd-4b50-4a65-911c-aee5076b1c7e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/electric waves_b2468acd-4b50-4a65-911c-aee5076b1c7e.svg'), ('f683dd0c-b161-414e-8816-ecfc56a54c18', 'pictographic-primitives/networks/wifi_f683dd0c-b161-414e-8816-ecfc56a54c18.svg'))
PROFILE_SOURCE_KEYS = ('solo/wifi', 'solo/wifi-f683dd0c')
SOLO_SOURCE_ICON_IDS = ('wifi', 'wifi-f683dd0c')
REFERENCE_EXPORT_SHA256 = '08e98cce167e74f1102bdab222a8ad6789a52d4b398fb8ced78a386741f8f524'

class DrawingVariant2(Sub32):
    icon_id = 'wifi-sub32-v2'
    variant_of = 'wifi-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'networks'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two smooth symmetric signal bands and one dot. Construction reference: wifi."""
        self.add_bezier('outer-left', (2, 11), ((6, 7), (10, 4), (16, 4)))
        self.add_bezier('outer-right', (16, 4), ((22, 4), (26, 7), (30, 11)))
        self.add_contour('outer', 'outer-left', 'outer-right')
        self.add_bezier('inner-left', (9, 19), ((11, 17), (13, 15), (16, 15)))
        self.add_bezier('inner-right', (16, 15), ((19, 15), (21, 17), (23, 19)))
        self.add_contour('inner', 'inner-left', 'inner-right')
        self.add_dot('point', (16, 28))

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
