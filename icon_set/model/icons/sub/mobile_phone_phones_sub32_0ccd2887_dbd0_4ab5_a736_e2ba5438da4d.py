"""Independent 32px profile of mobile-phone-phones.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0ccd2887-dbd0-4ab5-a736-e2ba5438da4d'
SOURCE_PATH = 'pictographic-primitives/phones/mobile phone_0ccd2887-dbd0-4ab5-a736-e2ba5438da4d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0ccd2887-dbd0-4ab5-a736-e2ba5438da4d', 'pictographic-primitives/phones/mobile phone_0ccd2887-dbd0-4ab5-a736-e2ba5438da4d.svg'), ('70454eff-c88b-47e2-b376-ad91c78c22f0', 'pictographic-primitives/phones/mobile phone_70454eff-c88b-47e2-b376-ad91c78c22f0.svg'), ('c4f9e2f1-641c-4dbb-ae42-c4ce12aafedf', 'pictographic-primitives/phones/mobile phone_c4f9e2f1-641c-4dbb-ae42-c4ce12aafedf.svg'))
PROFILE_SOURCE_KEYS = ('solo/mobile-phone-phones', 'solo/mobile-phone-70454eff', 'solo/mobile-phone-c4f9e2f1')
SOLO_SOURCE_ICON_IDS = ('mobile-phone-phones', 'mobile-phone-70454eff', 'mobile-phone-c4f9e2f1')
REFERENCE_EXPORT_SHA256 = '04503e0736e507598f14c69f2520921f4375190d995f1c7e395b765219108e21'

class Drawing(Sub32):
    icon_id = 'mobile-phone-phones-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'phones'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 23), (27, 23))
        self.add_line('p1-r1-2', (27, 23), (27, 27))
        self.add_arc('p1-r1-3', (27, 27), (26, 29), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (26, 29), (24, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (24, 30), (8, 30))
        self.add_arc('p1-r1-6', (8, 30), (6, 29), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (6, 29), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (5, 27), (5, 5))
        self.add_arc('p1-r1-9', (5, 5), (8, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (8, 2), (24, 2))
        self.add_arc('p1-r1-11', (24, 2), (27, 5), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-12', (27, 5), (27, 23))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
