"""Independent 32px profile of minimal-smartphone-with-home-bar.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2bde9c42-ab23-4516-8f6a-20cc999de0e3'
SOURCE_PATH = 'pictographic-primitives/phones/mobile phone_2bde9c42-ab23-4516-8f6a-20cc999de0e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2bde9c42-ab23-4516-8f6a-20cc999de0e3', 'pictographic-primitives/phones/mobile phone_2bde9c42-ab23-4516-8f6a-20cc999de0e3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/minimal-smartphone-with-home-bar',)
SOLO_SOURCE_ICON_IDS = ('minimal-smartphone-with-home-bar',)
REFERENCE_EXPORT_SHA256 = 'a13cff8651224a9182505adaacf2df57762e4b544a4f778d3645d779e17d9023'

class Drawing(Sub32):
    icon_id = 'minimal-smartphone-with-home-bar-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/device'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (24, 2))
        self.add_arc('p1-r1-2', (24, 2), (27, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 5), (27, 27))
        self.add_arc('p1-r1-4', (27, 27), (24, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (24, 30), (8, 30))
        self.add_arc('p1-r1-6', (8, 30), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (5, 27), (5, 5))
        self.add_arc('p1-r1-8', (5, 5), (8, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (14, 24), (18, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
