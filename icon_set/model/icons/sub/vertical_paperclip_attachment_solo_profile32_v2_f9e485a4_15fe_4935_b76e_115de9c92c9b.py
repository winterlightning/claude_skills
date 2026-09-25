"""Independent 32px profile of vertical-paperclip-attachment-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f9e485a4-15fe-4935-b76e-115de9c92c9b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/attachment vertical_f9e485a4-15fe-4935-b76e-115de9c92c9b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f9e485a4-15fe-4935-b76e-115de9c92c9b', 'pictographic-primitives/other/attachment vertical_f9e485a4-15fe-4935-b76e-115de9c92c9b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/vertical-paperclip-attachment-solo',)
SOLO_SOURCE_ICON_IDS = ('vertical-paperclip-attachment-solo',)
REFERENCE_EXPORT_SHA256 = '78f02281fd34b2f90f08f0c33d7d81c8d2f8fa650498e209d2ec760487ecfeec'

class DrawingVariant2(Sub32):
    icon_id = 'vertical-paperclip-attachment-solo-profile32-v2'
    variant_of = 'vertical-paperclip-attachment-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Vertical paperclip formed by an outer upper arch, lower return and inner hook. Construction reference: paperclip."""
        self.add_arc('outer-top', (4, 14), (28, 14), radius_x=12)
        self.add_line('outer-r', (28, 14), (28, 22))
        self.add_arc('bottom', (28, 22), (12, 22), radius_x=8)
        self.add_line('inner-l', (12, 22), (12, 16))
        self.add_arc('hook', (12, 16), (20, 16), radius_x=4)
        self.add_line('end', (20, 16), (20, 22))
        self.add_contour('clip', 'outer-top', 'outer-r', 'bottom', 'inner-l', 'hook', 'end')

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
