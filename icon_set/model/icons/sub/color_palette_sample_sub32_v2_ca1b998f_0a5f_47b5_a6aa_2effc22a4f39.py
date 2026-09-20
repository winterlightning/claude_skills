"""Independent 32px profile of color-palette-sample.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ca1b998f-0a5f-47b5-a6aa-2effc22a4f39'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/design/color palette sample_ca1b998f-0a5f-47b5-a6aa-2effc22a4f39.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ca1b998f-0a5f-47b5-a6aa-2effc22a4f39', 'pictographic-primitives/design/color palette sample_ca1b998f-0a5f-47b5-a6aa-2effc22a4f39.svg'),)
PROFILE_SOURCE_KEYS = ('solo/color-palette-sample',)
SOLO_SOURCE_ICON_IDS = ('color-palette-sample',)
REFERENCE_EXPORT_SHA256 = '014a3ec9066be4d14fb7a8b18f1004b9ffa2a5a8a4d81fd2dbc539e87faabac2'

class DrawingVariant2(Sub32):
    icon_id = 'color-palette-sample-sub32-v2'
    variant_of = 'color-palette-sample-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Asymmetric painter palette with three short separate paint marks. Construction reference: palette."""
        self.add_bezier('top-l', (4, 19), ((4, 10), (9, 2), (17, 2)))
        self.add_bezier('top-r', (17, 2), ((23, 2), (28, 6), (28, 10)))
        self.add_bezier('notch-top', (28, 10), ((28, 15), (22, 15), (22, 20)))
        self.add_bezier('notch-base', (22, 20), ((22, 24), (25, 30), (16, 30)))
        self.add_bezier('bottom-l', (16, 30), ((8, 30), (4, 26), (4, 19)))
        self.add_contour('palette', 'top-l', 'top-r', 'notch-top', 'notch-base', 'bottom-l', closed=True)
        self.add_line('paint-top', (18, 9), (18, 10))
        self.add_line('paint-left', (11, 15), (12, 16))
        self.add_line('paint-bottom', (12, 23), (14, 23))

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
