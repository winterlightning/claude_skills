"""Independent 32px profile of claw-hammer-on-diagonal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '20af476c-a57f-4ace-b516-465f1fa2eefd'
SOURCE_PATH = 'pictographic-primitives/construction/hammer_20af476c-a57f-4ace-b516-465f1fa2eefd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('20af476c-a57f-4ace-b516-465f1fa2eefd', 'pictographic-primitives/construction/hammer_20af476c-a57f-4ace-b516-465f1fa2eefd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/claw-hammer-on-diagonal',)
SOLO_SOURCE_ICON_IDS = ('claw-hammer-on-diagonal',)
REFERENCE_EXPORT_SHA256 = '6b03edc1f91cf6e3c567119e95e19a7bffb29ffebcbd4fede20f70d88c24a770'

class Drawing(Sub32):
    icon_id = 'claw-hammer-on-diagonal-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'construction'
    categories = ('construction', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Claw hammer on the diagonal: straight handle, a head with a flat face and a curved claw.
        self.add_line('head-1', (16, 2), (30, 16))
        self.add_line('head-2', (30, 16), (24, 22))
        self.add_line('head-3', (24, 22), (10, 8))
        self.add_line('claw-1', (10, 8), (3, 6))
        self.add_bezier('claw-2', (3, 6), ((7, 3), (12, 2), (16, 2)))
        self.add_contour('head', 'head-1', 'head-2', 'head-3', 'claw-1', 'claw-2', closed=True)
        self.add_line('handle', (17, 15), (2, 30))
        self.relate('connect', 'head', 'handle')
