"""Independent 32px profile of chicken-face.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7443f092-4834-4d07-9b5b-1b7914777905'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/animals/chicken_7443f092-4834-4d07-9b5b-1b7914777905.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7443f092-4834-4d07-9b5b-1b7914777905', 'pictographic-primitives/animals/chicken_7443f092-4834-4d07-9b5b-1b7914777905.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chicken-face',)
SOLO_SOURCE_ICON_IDS = ('chicken-face',)
REFERENCE_EXPORT_SHA256 = '9bbc5a9688cae7020358725b5ea130c8ae8e847164c2006b396f805bd598484b'

class DrawingVariant4(Sub32):
    icon_id = 'chicken-face-sub32-v4'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'animals'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Open chicken head, closed arched comb, two eye dots and a closed diamond beak. Small-size treatment: Merged the comb into the outer head outline, removing only the tiny dividing line; kept both eyes and the closed diamond beak. Construction reference: egg / original source: smooth bilateral head and closed comb opening."""
        self.add_line('head-left', (2, 30), (2, 24))
        self.add_bezier('head-tl', (2, 24), ((2, 16), (6, 8), (12, 8)))
        self.add_arc('comb', (12, 8), (20, 8), radius_x=4, radius_y=6)
        self.add_bezier('head-tr', (20, 8), ((26, 8), (30, 16), (30, 24)))
        self.add_line('head-right', (30, 24), (30, 30))
        self.add_contour('head', 'head-left', 'head-tl', 'comb', 'head-tr', 'head-right')
        self.add_line('eye-left', (11, 16), (11, 16))
        self.add_line('eye-right', (21, 16), (21, 16))
        self.add_polyline('beak', (16, 20), (23, 25), (16, 30), (9, 25), (16, 20))

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
