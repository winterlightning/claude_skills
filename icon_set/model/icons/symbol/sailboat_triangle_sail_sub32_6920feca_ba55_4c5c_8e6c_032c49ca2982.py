"""Independent 32px profile of sailboat-triangle-sail.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6920feca-ba55-4c5c-8e6c-032c49ca2982'
SOURCE_PATH = 'pictographic-primitives/outdoors/sailing boat_6920feca-ba55-4c5c-8e6c-032c49ca2982.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6920feca-ba55-4c5c-8e6c-032c49ca2982', 'pictographic-primitives/outdoors/sailing boat_6920feca-ba55-4c5c-8e6c-032c49ca2982.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sailboat-triangle-sail',)
SOLO_SOURCE_ICON_IDS = ('sailboat-triangle-sail',)
REFERENCE_EXPORT_SHA256 = 'f850253c460aa222eaddc613f2f9789730c2299eb7dd03edc4e7ecb23b8fb31b'

class Drawing(Sub32):
    icon_id = 'sailboat-triangle-sail-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'outdoors'
    categories = ('outdoors', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Sailboat: mast with a triangular sail over a trapezoid hull.
        self.add_polyline('sail', (16, 20), (16, 4), (28, 20))
        self.add_polyline('hull', (2, 20), (30, 20), (24, 28), (8, 28), closed=True)
        self.relate('connect', 'sail', 'hull')
