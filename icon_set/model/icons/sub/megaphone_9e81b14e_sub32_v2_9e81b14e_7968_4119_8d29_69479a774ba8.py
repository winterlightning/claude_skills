"""Independent 32px profile of megaphone-9e81b14e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9e81b14e-7968-4119-8d29-69479a774ba8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/megaphone_9e81b14e-7968-4119-8d29-69479a774ba8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9e81b14e-7968-4119-8d29-69479a774ba8', 'pictographic-primitives/interface-essential/megaphone_9e81b14e-7968-4119-8d29-69479a774ba8.svg'), ('419cefd4-6e8d-4c3c-8b36-3566f3fa846b', 'pictographic-primitives/interface-essential/megaphone_419cefd4-6e8d-4c3c-8b36-3566f3fa846b.svg'))
PROFILE_SOURCE_KEYS = ('solo/megaphone-9e81b14e', 'solo/megaphone-interface-essential')
SOLO_SOURCE_ICON_IDS = ('megaphone-9e81b14e', 'megaphone-interface-essential')
REFERENCE_EXPORT_SHA256 = '0c17287a95bf13d28f521e0d9d93ccbfb1b446831e6760dfa4b90635ad542d26'

class DrawingVariant2(Sub32):
    icon_id = 'megaphone-9e81b14e-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded mouthpiece, tapered curved horn, divider and hanging grip. Construction reference: megaphone."""
        self.add_line('mouth-top', (6, 14), (12, 14))
        self.add_bezier('horn-top', (12, 14), ((18, 12), (22, 7), (26, 2)))
        self.add_line('rim', (26, 2), (30, 24))
        self.add_bezier('horn-bottom', (30, 24), ((24, 22), (18, 22), (12, 22)))
        self.add_line('mouth-bottom', (12, 22), (6, 22))
        self.add_arc('mouth-round', (6, 22), (6, 14), radius_x=4)
        self.add_contour('horn', 'mouth-top', 'horn-top', 'rim', 'horn-bottom', 'mouth-bottom', 'mouth-round', closed=True)
        self.add_line('divider', (12, 14), (12, 22))
        self.relate('connect', 'horn', 'divider')
        self.add_bezier('grip', (8, 22), ((12, 30), (12, 30), (17, 30)))
        self.relate('connect', 'grip', 'horn')

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
