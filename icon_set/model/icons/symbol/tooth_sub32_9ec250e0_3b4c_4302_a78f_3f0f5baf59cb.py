"""Independent 32px profile of tooth.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9ec250e0-3b4c-4302-a78f-3f0f5baf59cb'
SOURCE_PATH = 'pictographic-primitives/health/tooth_9ec250e0-3b4c-4302-a78f-3f0f5baf59cb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9ec250e0-3b4c-4302-a78f-3f0f5baf59cb', 'pictographic-primitives/health/tooth_9ec250e0-3b4c-4302-a78f-3f0f5baf59cb.svg'),)
PROFILE_SOURCE_KEYS = ('solo/tooth',)
SOLO_SOURCE_ICON_IDS = ('tooth',)
REFERENCE_EXPORT_SHA256 = 'ea01b5c07e4e54bb0b379a4c92c6332cf3f82e8688152f3dc13479189a40fd81'

class Drawing(Sub32):
    icon_id = 'tooth-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    categories = ('health', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Tooth: crown with a notch, two 8-unit roots.
        self.add_bezier('t-1', (16, 5), ((19, 3), (21, 2), (23, 2)))
        self.add_bezier('t-2', (23, 2), ((27, 2), (28, 6), (28, 10)))
        self.add_line('t-3', (28, 10), (28, 26))
        self.add_arc('t-4', (28, 26), (20, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('t-5', (20, 26), (20, 22))
        self.add_arc('t-6', (20, 22), (12, 22), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('t-7', (12, 22), (12, 26))
        self.add_arc('t-8', (12, 26), (4, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('t-9', (4, 26), (4, 10))
        self.add_bezier('t-10', (4, 10), ((4, 6), (5, 2), (9, 2)))
        self.add_bezier('t-11', (9, 2), ((11, 2), (13, 3), (16, 5)))
        self.add_contour('tooth', 't-1', 't-2', 't-3', 't-4', 't-5', 't-6', 't-7', 't-8', 't-9', 't-10', 't-11', closed=True)
