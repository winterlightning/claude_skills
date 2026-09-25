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
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'construction'
    categories = ('construction', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 21), (13, 14))
        self.add_bezier('p1-r1-2', (13, 14), ((13, 11), (13, 9), (12, 7)))
        self.add_bezier('p1-r1-3', (12, 7), ((11, 5), (10, 4), (9, 4)))
        self.add_bezier('p1-r1-4', (9, 4), ((9, 4), (9, 4), (9, 4)))
        self.add_line('p1-r1-5', (9, 4), (17, 4))
        self.add_line('p1-r1-6', (17, 4), (24, 9))
        self.add_line('p1-r1-7', (24, 9), (30, 15))
        self.add_line('p1-r1-8', (30, 15), (25, 22))
        self.add_line('p1-r1-9', (25, 22), (21, 18))
        self.add_line('p1-r1-10', (21, 18), (8, 27))
        self.add_bezier('p1-r1-11', (8, 27), ((8, 28), (7, 28), (6, 28)))
        self.add_bezier('p1-r1-12', (6, 28), ((5, 28), (4, 27), (3, 26)))
        self.add_bezier('p1-r1-13', (3, 26), ((2, 26), (2, 25), (2, 24)))
        self.add_bezier('p1-r1-14', (2, 24), ((2, 23), (3, 22), (4, 21)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
