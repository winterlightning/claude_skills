"""Independent 32px profile of checklist-document-for-tasks-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3b7aa072-22e2-420b-a990-9a6447b66ea3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/task list_3b7aa072-22e2-420b-a990-9a6447b66ea3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3b7aa072-22e2-420b-a990-9a6447b66ea3', 'pictographic-primitives/symbol/task list_3b7aa072-22e2-420b-a990-9a6447b66ea3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/checklist-document-for-tasks-solo',)
SOLO_SOURCE_ICON_IDS = ('checklist-document-for-tasks-solo',)
REFERENCE_EXPORT_SHA256 = 'a92e3d237ac9f07d637fcb3d2107e46eb57e4a77a671e826758be4a06a2f3fcf'

class DrawingVariant2(Sub32):
    icon_id = 'checklist-document-for-tasks-solo-profile32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Checklist document with two separate square checkboxes and two horizontal content lines. Small-size treatment: Replaced small empty checkbox outlines with readable check strokes; kept two rows and their text marks. Construction reference: list-check: paired rows, complete source boxes."""
        box(self, 'page', 2, 2, 30, 30, 3)
        for i, y in enumerate((11, 21)):
            self.add_polyline(f'check-{i}', (9, y), (11, y + 2), (14, y - 2))
            self.add_line(f'text-{i}', (21, y), (23, y))

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
