"""Independent 32px profile of three-acupuncture-needles-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'c8865933-bab1-445f-94ab-65d5649059df'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/needles three_c8865933-bab1-445f-94ab-65d5649059df.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c8865933-bab1-445f-94ab-65d5649059df', 'pictographic-primitives/other/needles three_c8865933-bab1-445f-94ab-65d5649059df.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-acupuncture-needles-solo',)
SOLO_SOURCE_ICON_IDS = ('three-acupuncture-needles-solo',)
REFERENCE_EXPORT_SHA256 = '2d386e10d9b13b264798a4d70b7aec73fc7e9d497f0edc7260a52ce404fef020'

class DrawingVariant2(Sub32):
    icon_id = 'three-acupuncture-needles-solo-profile32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three acupuncture needles with open circular heads and distinct upward, horizontal and downward directions. Construction reference: syringe."""
        for name, x, y, a, b in [('top', 19, 5, (10, 10), (16, 5)), ('middle', 27, 16, (2, 16), (24, 16)), ('bottom', 19, 27, (2, 24), (16, 27))]:
            circle(self, name + '-head', x, y, 3)
            self.add_line(name + '-stem', a, b)
            self.relate('connect', name + '-head', name + '-stem')

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
