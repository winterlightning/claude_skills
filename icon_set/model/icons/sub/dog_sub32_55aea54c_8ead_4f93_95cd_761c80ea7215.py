"""Independent 32px profile of dog.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '55aea54c-8ead-4f93-95cd-761c80ea7215'
SOURCE_PATH = 'pictographic-primitives/pets/dog_55aea54c-8ead-4f93-95cd-761c80ea7215.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('55aea54c-8ead-4f93-95cd-761c80ea7215', 'pictographic-primitives/pets/dog_55aea54c-8ead-4f93-95cd-761c80ea7215.svg'), ('c099ef25-3154-4ff5-ba1a-7e0f9f82bb67', 'pictographic-primitives/pets/dog_c099ef25-3154-4ff5-ba1a-7e0f9f82bb67.svg'))
PROFILE_SOURCE_KEYS = ('solo/dog', 'solo/dog-c099ef25')
SOLO_SOURCE_ICON_IDS = ('dog', 'dog-c099ef25')
REFERENCE_EXPORT_SHA256 = 'adb4efb7fd21d7e72c1cc9bd121da49e19ab2da62b6b85681de5ab03e8a569d0'

class Drawing(Sub32):
    icon_id = 'dog-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'pets'
    categories = ('pets', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 25), ((5, 16), (9, 7), (14, 2)))
        self.add_line('p1-r1-2', (14, 2), (16, 9))
        self.add_bezier('p1-r1-3', (16, 9), ((17, 11), (21, 11), (25, 11)))
        self.add_bezier('p1-r1-4', (25, 11), ((28, 12), (30, 14), (30, 17)))
        self.add_bezier('p1-r1-5', (30, 17), ((30, 21), (24, 22), (17, 23)))
        self.add_line('p1-r1-6', (17, 23), (15, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
