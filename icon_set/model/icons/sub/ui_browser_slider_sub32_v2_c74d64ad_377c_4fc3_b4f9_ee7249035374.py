"""Independent 32px profile of ui-browser-slider.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'c74d64ad-377c-4fc3-b4f9-ee7249035374'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/websites/ui browser slider_c74d64ad-377c-4fc3-b4f9-ee7249035374.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c74d64ad-377c-4fc3-b4f9-ee7249035374', 'pictographic-primitives/websites/ui browser slider_c74d64ad-377c-4fc3-b4f9-ee7249035374.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ui-browser-slider',)
SOLO_SOURCE_ICON_IDS = ('ui-browser-slider',)
REFERENCE_EXPORT_SHA256 = 'bbe7abdff89bedf4b8c61d744d73c876ac3b916406f0ec2fb57f99bad9da4ebe'

class DrawingVariant2(Sub32):
    icon_id = 'ui-browser-slider-sub32-v2'
    variant_of = 'ui-browser-slider-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'websites'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded browser frame with complete header divider and one shorter content line. Construction reference: app-window."""
        box(self, 'window', 2, 2, 30, 30, 4)
        self.add_line('header', (2, 10), (30, 10))
        self.relate('connect', 'header', 'window')
        self.add_line('content', (10, 20), (22, 20))

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
