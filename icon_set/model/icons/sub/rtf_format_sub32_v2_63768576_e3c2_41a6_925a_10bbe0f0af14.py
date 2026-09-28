"""Independent 32px profile of rtf-format.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '63768576-e3c2-41a6-925a-10bbe0f0af14'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/rtf format_63768576-e3c2-41a6-925a-10bbe0f0af14.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('63768576-e3c2-41a6-925a-10bbe0f0af14', 'pictographic-primitives/state/rtf format_63768576-e3c2-41a6-925a-10bbe0f0af14.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rtf-format',)
SOLO_SOURCE_ICON_IDS = ('rtf-format',)
REFERENCE_EXPORT_SHA256 = '8b8894e93c5ffd08941da3c860035b2d19a104b99c99902b0cae6acd230efb20'

class DrawingVariant2(Sub32):
    icon_id = 'rtf-format-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Clipped-corner page enclosing a separate rounded rectangular panel divided into two cells. Small-size treatment: Merged the nested panel into the page frame while retaining its two-cell division. Construction reference: file-spreadsheet: nested panel and horizontal divider."""
        self.add_polyline('page', (4, 30), (4, 2), (21, 2), (28, 9), (28, 30), (4, 30))
        self.add_line('divider', (4, 16), (28, 16))
        self.relate('connect', 'divider', 'page')

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
