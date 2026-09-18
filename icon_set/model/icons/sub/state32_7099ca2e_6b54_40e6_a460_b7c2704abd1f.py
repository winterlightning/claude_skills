"""Independent 32px profile of state32-7099ca2e-6b54-40e6-a460-b7c2704abd1f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7099ca2e-6b54-40e6-a460-b7c2704abd1f'
SOURCE_PATH = 'icon_set/assets/combination-state32/7099ca2e-6b54-40e6-a460-b7c2704abd1f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7099ca2e-6b54-40e6-a460-b7c2704abd1f', 'icon_set/assets/combination-state32/7099ca2e-6b54-40e6-a460-b7c2704abd1f.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '8c82086ada377f1939677816cc94ee6e53c9a91b77de3dd46e177a0bf5e9141d'

class Drawing(Sub32):
    icon_id = 'state32-7099ca2e-6b54-40e6-a460-b7c2704abd1f'
    keyshape = Keyshape.HRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (20, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p1-r2-1', (14, 9), (20, 16))
        self.add_line('p1-r2-2', (20, 16), (14, 23))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.add_line('p2-r1-1', (22, 7), (30, 16))
        self.add_line('p2-r1-2', (30, 16), (22, 25))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p1-r2-1')
        self.relate("connect", 'p1-r1-1', 'p1-r2-2')
