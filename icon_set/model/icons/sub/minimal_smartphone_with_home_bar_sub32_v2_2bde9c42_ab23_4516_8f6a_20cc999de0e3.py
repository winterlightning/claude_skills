"""Independent 32px profile of minimal-smartphone-with-home-bar.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2bde9c42-ab23-4516-8f6a-20cc999de0e3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/phones/mobile phone_2bde9c42-ab23-4516-8f6a-20cc999de0e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2bde9c42-ab23-4516-8f6a-20cc999de0e3', 'pictographic-primitives/phones/mobile phone_2bde9c42-ab23-4516-8f6a-20cc999de0e3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/minimal-smartphone-with-home-bar',)
SOLO_SOURCE_ICON_IDS = ('minimal-smartphone-with-home-bar',)
REFERENCE_EXPORT_SHA256 = 'a13cff8651224a9182505adaacf2df57762e4b544a4f778d3645d779e17d9023'

class DrawingVariant2(Sub32):
    icon_id = 'minimal-smartphone-with-home-bar-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'phones'
    categories = ('phones', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded smartphone with separate horizontal home bar. Construction reference: smartphone."""
        box(self, 'phone', 4, 2, 28, 30, 4)
        self.add_line('home', (14, 22), (18, 22))

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
