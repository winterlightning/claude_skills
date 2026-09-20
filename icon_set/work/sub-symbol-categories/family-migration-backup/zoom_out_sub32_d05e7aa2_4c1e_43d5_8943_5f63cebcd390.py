"""Independent 32px profile of zoom-out.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd05e7aa2-4c1e-43d5-8943-5f63cebcd390'
SOURCE_PATH = 'pictographic-primitives/interface-essential/zoom out_d05e7aa2-4c1e-43d5-8943-5f63cebcd390.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d05e7aa2-4c1e-43d5-8943-5f63cebcd390', 'pictographic-primitives/interface-essential/zoom out_d05e7aa2-4c1e-43d5-8943-5f63cebcd390.svg'), ('94d79c2a-5cc5-4d30-a216-d020b553a665', 'icon_set/dist/gallery/combination-originals/94d79c2a-5cc5-4d30-a216-d020b553a665.svg'))
PROFILE_SOURCE_KEYS = ('solo/zoom-out',)
SOLO_SOURCE_ICON_IDS = ('zoom-out',)
REFERENCE_EXPORT_SHA256 = '361d622b8d10c120cd0e13b34371ecd04a62ce9e8063f8ae754759ff7269b548'

class Drawing(Sub32):
    icon_id = 'zoom-out-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 14), (25, 14), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (25, 14), (23, 21), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (23, 21), (2, 14), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (9, 14), (18, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (23, 21), (30, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
