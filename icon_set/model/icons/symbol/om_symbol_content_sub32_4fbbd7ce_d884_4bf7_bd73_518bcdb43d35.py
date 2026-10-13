"""Independent 32px profile of om-symbol-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4fbbd7ce-d884-4bf7-bd73-518bcdb43d35'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/4fbbd7ce-d884-4bf7-bd73-518bcdb43d35.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4fbbd7ce-d884-4bf7-bd73-518bcdb43d35', 'icon_set/dist/gallery/combination-originals/4fbbd7ce-d884-4bf7-bd73-518bcdb43d35.svg'),)
PROFILE_SOURCE_KEYS = ('solo/om-symbol-content',)
SOLO_SOURCE_ICON_IDS = ('om-symbol-content',)
REFERENCE_EXPORT_SHA256 = '93af44473a066b32e680b67649ff5c8bbe5f82cf97564dbb8af86cae0ccb890e'

class Drawing(Sub32):
    icon_id = 'om-symbol-content-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Om: the 3-shaped body, its tail sweeping right, crescent with the dot above it.
        self.add_bezier('upper', (2, 6), ((2, 1), (13, 1), (12, 9)))
        self.add_line('upper-2', (12, 9), (8, 18))
        self.add_contour('body-top', 'upper', 'upper-2')
        self.add_bezier('lower', (8, 18), ((14, 22), (14, 30), (6, 30)))
        self.add_line('lower-2', (6, 30), (2, 27))
        self.add_contour('body-bottom', 'lower', 'lower-2')
        self.add_bezier('tail', (8, 18), ((16, 18), (26, 21), (30, 27)))
        self.add_line('tail-2', (30, 27), (27, 30))
        self.add_contour('tail-all', 'tail', 'tail-2')
        self.add_arc('crescent', (21, 9), (29, 9), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('dot', (25, 2), (25, 2))
        self.relate('connect', 'body-top', 'body-bottom')
        self.relate('connect', 'body-top', 'tail-all')
        self.relate('connect', 'body-bottom', 'tail-all')
