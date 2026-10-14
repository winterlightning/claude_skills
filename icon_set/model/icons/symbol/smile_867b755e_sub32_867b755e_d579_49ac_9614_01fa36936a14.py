"""Independent 32px profile of smile-867b755e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '867b755e-d579-49ac-9614-01fa36936a14'
SOURCE_PATH = 'pictographic-primitives/smileys/smile_867b755e-d579-49ac-9614-01fa36936a14.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('867b755e-d579-49ac-9614-01fa36936a14', 'pictographic-primitives/smileys/smile_867b755e-d579-49ac-9614-01fa36936a14.svg'),)
PROFILE_SOURCE_KEYS = ('solo/smile-867b755e',)
SOLO_SOURCE_ICON_IDS = ('smile-867b755e',)
REFERENCE_EXPORT_SHA256 = '425abd922116237f4849cf15f9905db1f85d1f12075a53b398a48c318cce1441'

class Drawing(Sub32):
    icon_id = 'smile-867b755e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Smile: face circle, two eye dots, a gentle smile.
        self.add_arc('f-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('f-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('face', 'f-1', 'f-2', closed=True)
        self.add_dot('eye-l', (12, 12))
        self.add_dot('eye-r', (20, 12))
        self.add_arc('mouth', (13, 20), (19, 20), radius_x=3, radius_y=2, large_arc=False, sweep=False)
