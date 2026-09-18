# Variant of file-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of file.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2eca0df0-2d08-4674-b1e3-d443392e4f65'
SOURCE_PATH = 'pictographic-primitives/emails/file_2eca0df0-2d08-4674-b1e3-d443392e4f65.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2eca0df0-2d08-4674-b1e3-d443392e4f65', 'pictographic-primitives/emails/file_2eca0df0-2d08-4674-b1e3-d443392e4f65.svg'),)
PROFILE_SOURCE_KEYS = ('solo/file',)
SOLO_SOURCE_ICON_IDS = ('file',)
REFERENCE_EXPORT_SHA256 = '3b7710ac62c7e414ce5a4f147f85a78c1fffc5b361529d98d7cd2c1357ad93eb'

class DrawingVariant3(Sub32):
    icon_id = 'file-sub32-v3'
    variant_of = 'file-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'emails'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Document outline with a single clean clipped corner and softly rounded remaining corners.
        self.add_line('top-1',(9,2),(19,2))
        self.add_line('top-2',(19,2),(26,9))
        self.add_line('top-3',(26,9),(26,27))
        self.add_arc('br',(26,27),(23,30),radius_x=3,radius_y=3,sweep=True)
        self.add_line('bottom',(23,30),(9,30))
        self.add_arc('bl',(9,30),(6,27),radius_x=3,radius_y=3,sweep=True)
        self.add_line('left',(6,27),(6,5))
        self.add_arc('tl',(6,5),(9,2),radius_x=3,radius_y=3,sweep=True)
        self.add_contour('paper','top-1','top-2','top-3','br','bottom','bl','left','tl',closed=True)
