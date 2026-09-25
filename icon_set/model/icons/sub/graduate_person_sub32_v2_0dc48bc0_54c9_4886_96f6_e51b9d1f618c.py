"""Independent 32px profile of graduate-person.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0dc48bc0-54c9-4886-96f6-e51b9d1f618c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/graduate_0dc48bc0-54c9-4886-96f6-e51b9d1f618c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0dc48bc0-54c9-4886-96f6-e51b9d1f618c', 'pictographic-primitives/symbol/graduate_0dc48bc0-54c9-4886-96f6-e51b9d1f618c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/graduate-person',)
SOLO_SOURCE_ICON_IDS = ('graduate-person',)
REFERENCE_EXPORT_SHA256 = '8d1fea01b8c18d2d3fe14f6b8546067d4bf88ae4270a9723e1c2645981901a39'

class DrawingVariant2(Sub32):
    icon_id = 'graduate-person-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Graduate mortarboard above a circular jaw and open shoulder bust. Construction reference: human_ref/user.svg: circular jaw and exact four-unit detached gap."""
        self.add_polyline('cap-top', (9, 11), (2, 8), (16, 2), (30, 8), (23, 11))
        self.add_arc('jaw', (23, 11), (9, 11), radius_x=7)
        self.relate('connect', 'cap-top', 'jaw')
        self.add_bezier('shoulder-left', (4, 30), ((4, 28), (9, 26), (16, 26)))
        self.add_bezier('shoulder-right', (16, 26), ((23, 26), (28, 28), (28, 30)))
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-right')

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
