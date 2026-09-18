"""Independent 32px profile of tilted-cctv-camera-facing-left.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5294275e-a650-44f6-a500-35cff69f1d2a'
SOURCE_PATH = 'pictographic-primitives/protection/surveillance cctv 1_5294275e-a650-44f6-a500-35cff69f1d2a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5294275e-a650-44f6-a500-35cff69f1d2a', 'pictographic-primitives/protection/surveillance cctv 1_5294275e-a650-44f6-a500-35cff69f1d2a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/tilted-cctv-camera-facing-left',)
SOLO_SOURCE_ICON_IDS = ('tilted-cctv-camera-facing-left',)
REFERENCE_EXPORT_SHA256 = 'c9f751e8d2093e41aeb84b03566b8b6f5c6e01a1ca620823906eebced1853faa'

class Drawing(Sub32):
    icon_id = 'tilted-cctv-camera-facing-left-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/protection'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 10), (26, 5))
        self.add_line('p1-r1-2', (26, 5), (30, 17))
        self.add_line('p1-r1-3', (30, 17), (22, 20))
        self.add_line('p1-r1-4', (22, 20), (13, 23))
        self.add_line('p1-r1-5', (13, 23), (9, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (2, 13), (5, 22))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 20), (22, 24))
        self.add_arc('p3-r1-2', (22, 24), (24, 27), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p3-r1-3', (24, 27), (30, 27))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
