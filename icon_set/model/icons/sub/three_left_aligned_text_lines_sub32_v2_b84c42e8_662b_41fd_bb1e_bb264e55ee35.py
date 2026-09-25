"""Independent 32px profile of three-left-aligned-text-lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b84c42e8-662b-41fd-bb1e-bb264e55ee35'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/three lines_b84c42e8-662b-41fd-bb1e-bb264e55ee35.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b84c42e8-662b-41fd-bb1e-bb264e55ee35', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/three lines_b84c42e8-662b-41fd-bb1e-bb264e55ee35.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-left-aligned-text-lines',)
SOLO_SOURCE_ICON_IDS = ('three-left-aligned-text-lines',)
REFERENCE_EXPORT_SHA256 = 'a32e3d57b7b2b0d6664541bae3ee86e82daae4b865304bb80ec38ae9f2ddf730'

class DrawingVariant2(Sub32):
    icon_id = 'three-left-aligned-text-lines-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three left-aligned lines, progressively shorter from top to bottom. Construction reference: none."""
        for i, (y, end) in enumerate(((4, 30), (16, 23), (28, 16))):
            self.add_line(f'line-{i}', (2, y), (end, y))

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
