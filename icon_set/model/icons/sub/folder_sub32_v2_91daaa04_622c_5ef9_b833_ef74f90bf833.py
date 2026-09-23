# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of folder.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '91daaa04-622c-5ef9-b833-ef74f90bf833'
SOURCE_PATH = 'pictographic-primitives/folders/folder_91daaa04-622c-5ef9-b833-ef74f90bf833.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('91daaa04-622c-5ef9-b833-ef74f90bf833', 'pictographic-primitives/folders/folder_91daaa04-622c-5ef9-b833-ef74f90bf833.svg'),)
PROFILE_SOURCE_KEYS = ('solo/folder',)
SOLO_SOURCE_ICON_IDS = ('folder',)
REFERENCE_EXPORT_SHA256 = '4a807b621db1fea2576499246cd0fc5fe75dbeeb7402b88aff57f6daf5450154'

class DrawingVariant2(Sub32):
    icon_id = 'folder-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'folders'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Rounded folder body; coherent corner radii and deliberate tab corners.
        self.add_line('top-tab',(5,4),(11,4))
        self.add_line('tab-slope',(11,4),(16,8))
        self.add_line('top',(16,8),(27,8))
        self.add_arc('top-right',(27,8),(30,11),radius_x=3,radius_y=3,sweep=True)
        self.add_line('right',(30,11),(30,25))
        self.add_arc('bottom-right',(30,25),(27,28),radius_x=3,radius_y=3,sweep=True)
        self.add_line('bottom',(27,28),(5,28))
        self.add_arc('bottom-left',(5,28),(2,25),radius_x=3,radius_y=3,sweep=True)
        self.add_line('left',(2,25),(2,7))
        self.add_arc('top-left',(2,7),(5,4),radius_x=3,radius_y=3,sweep=True)
        self.add_contour('path-1-1','top-tab','tab-slope','top','top-right','right','bottom-right','bottom','bottom-left','left','top-left',closed=True)
