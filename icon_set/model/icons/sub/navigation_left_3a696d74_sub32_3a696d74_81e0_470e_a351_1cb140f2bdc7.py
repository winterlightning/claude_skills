"""Independent 32px profile of navigation-left-3a696d74.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3a696d74-81e0-470e-a351-1cb140f2bdc7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation left_3a696d74-81e0-470e-a351-1cb140f2bdc7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3a696d74-81e0-470e-a351-1cb140f2bdc7', 'pictographic-primitives/interface-essential/navigation left_3a696d74-81e0-470e-a351-1cb140f2bdc7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/navigation-left-3a696d74',)
SOLO_SOURCE_ICON_IDS = ('navigation-left-3a696d74',)
REFERENCE_EXPORT_SHA256 = '51a7c02b32d3e42a453c96a2be87fcf4e1acb3c7866cb14e3dde1d075a65fcb9'

class Drawing(Sub32):
    icon_id = 'navigation-left-3a696d74-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 16), ((8, 12), (11, 10), (17, 10)))
        self.add_bezier('p1-r1-2', (17, 10), ((26, 10), (30, 18), (30, 27)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (9, 5), (2, 16))
        self.add_line('p2-r1-2', (2, 16), (12, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
