"""Independent 32px profile of heart-pulse.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3ec61357-503d-46af-90a8-2fa210293e19'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/heart throb_3ec61357-503d-46af-90a8-2fa210293e19.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3ec61357-503d-46af-90a8-2fa210293e19', 'pictographic-primitives/symbol/heart throb_3ec61357-503d-46af-90a8-2fa210293e19.svg'), ('a9dc34df-bbc3-4ab4-a859-ebdb7d92a804', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/sports/heart rate_a9dc34df-bbc3-4ab4-a859-ebdb7d92a804.svg'), ('468beab8-6edf-4e7f-9ee2-0f23f5c3b360', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/sports/heart rate_468beab8-6edf-4e7f-9ee2-0f23f5c3b360.svg'), ('a954f676-1cce-4e19-81eb-ec067ec52edc', 'icon_set/dist/gallery/combination-originals/a954f676-1cce-4e19-81eb-ec067ec52edc.svg'))
PROFILE_SOURCE_KEYS = ('solo/heart-pulse',)
SOLO_SOURCE_ICON_IDS = ('heart-pulse',)
REFERENCE_EXPORT_SHA256 = 'a0e0a468015204b48ebba4e5778af58a1ff414247475f0f869116cff52877287'

class DrawingVariant2(Sub32):
    icon_id = 'heart-pulse-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Heart with two round lobes and complete four-turn pulse trace. Construction reference: heart-pulse."""
        self.add_arc('lobe-l', (2, 9), (16, 9), radius_x=7)
        self.add_arc('lobe-r', (16, 9), (30, 9), radius_x=7)
        self.add_bezier('side-r', (30, 9), ((30, 17), (22, 25), (16, 30)))
        self.add_bezier('side-l', (16, 30), ((10, 25), (2, 17), (2, 9)))
        self.add_contour('heart', 'lobe-l', 'lobe-r', 'side-r', 'side-l', closed=True)
        self.add_polyline('pulse', (5, 17), (8, 17), (10, 12), (17, 22), (20, 16), (23, 18), (26, 18))
        self.relate('connect', 'pulse', 'heart')

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
