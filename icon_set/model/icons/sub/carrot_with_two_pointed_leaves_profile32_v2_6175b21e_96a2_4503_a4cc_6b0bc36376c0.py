"""Independent 32px profile of carrot-with-two-pointed-leaves.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '6175b21e-96a2-4503-a4cc-6b0bc36376c0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6175b21e-96a2-4503-a4cc-6b0bc36376c0', 'pictographic-primitives/food/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/carrot-with-two-pointed-leaves',)
SOLO_SOURCE_ICON_IDS = ('carrot-with-two-pointed-leaves',)
REFERENCE_EXPORT_SHA256 = 'b7c0515f7de3002b2ccc1c0c1222bbb9273c75f4f852db578b954aba04270a0d'

class DrawingVariant2(Sub32):
    icon_id = 'carrot-with-two-pointed-leaves-profile32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'food'
    categories = ('food', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Tapered carrot with two upright leaf strokes and one short texture mark. Construction reference: carrot: tapered body and upright leaves."""
        self.add_arc('shoulder', (8, 14), (24, 14), radius_x=8, radius_y=5)
        self.add_line('right', (24, 14), (20, 28))
        self.add_bezier('tip-right', (20, 28), ((18, 30), (18, 30), (16, 30)))
        self.add_bezier('tip-left', (16, 30), ((14, 30), (14, 30), (12, 28)))
        self.add_line('left', (12, 28), (8, 14))
        self.add_contour('carrot', 'shoulder', 'right', 'tip-right', 'tip-left', 'left', closed=True)
        self.add_polyline('leaves', (10, 2), (16, 9), (22, 2))
        self.relate('connect', 'leaves', 'carrot')
        self.add_line('mark', (10, 21), (15, 21))
        self.relate('connect', 'mark', 'carrot')

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
