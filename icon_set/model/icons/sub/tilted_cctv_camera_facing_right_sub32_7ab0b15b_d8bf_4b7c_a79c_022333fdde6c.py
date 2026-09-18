"""Independent 32px profile of tilted-cctv-camera-facing-right.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7ab0b15b-d8bf-4b7c-a79c-022333fdde6c'
SOURCE_PATH = 'pictographic-primitives/protection/surveillance cctv_7ab0b15b-d8bf-4b7c-a79c-022333fdde6c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7ab0b15b-d8bf-4b7c-a79c-022333fdde6c', 'pictographic-primitives/protection/surveillance cctv_7ab0b15b-d8bf-4b7c-a79c-022333fdde6c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/tilted-cctv-camera-facing-right',)
SOLO_SOURCE_ICON_IDS = ('tilted-cctv-camera-facing-right',)
REFERENCE_EXPORT_SHA256 = '8aff0258405f85a8d935136eb394e179a0d49f0e6525e6b038c023d54897b435'

class Drawing(Sub32):
    icon_id = 'tilted-cctv-camera-facing-right-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/protection'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (23, 10), (6, 5))
        self.add_line('p1-r1-2', (6, 5), (2, 17))
        self.add_line('p1-r1-3', (2, 17), (10, 20))
        self.add_line('p1-r1-4', (10, 20), (19, 23))
        self.add_line('p1-r1-5', (19, 23), (23, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (30, 13), (27, 22))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, 20), (10, 24))
        self.add_arc('p3-r1-2', (10, 24), (8, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (8, 27), (2, 27))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
