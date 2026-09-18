# Variant of hard-hat-on-stand-2c1fa7b6-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of hard-hat-on-stand-2c1fa7b6.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2c1fa7b6-a8c3-4407-9935-862250d036d1'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_2c1fa7b6-a8c3-4407-9935-862250d036d1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2c1fa7b6-a8c3-4407-9935-862250d036d1', 'pictographic-primitives/protection/helmet_2c1fa7b6-a8c3-4407-9935-862250d036d1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hard-hat-on-stand-2c1fa7b6',)
SOLO_SOURCE_ICON_IDS = ('hard-hat-on-stand-2c1fa7b6',)
REFERENCE_EXPORT_SHA256 = '12f446f680d96f9ac87f65cc989236605efa365c44c8f0ebc558e2fa3101c561'

class DrawingVariant3(Sub32):
    icon_id = 'hard-hat-on-stand-2c1fa7b6-sub32-v3'
    variant_of = 'hard-hat-on-stand-2c1fa7b6-sub32-v2'
    variant_label = 'Restore omitted source details'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/protection'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # The dome stops at the crown strip; no hidden crossing or doubled top edge.
        self.add_bezier('dome-left',(6,14),((6,10),(8,6),(12,4)))
        self.add_bezier('dome-right',(20,4),((24,6),(26,10),(26,14)))
        self.add_polyline('tab',(12,6),(12,2),(20,2),(20,6))
        self.relate('connect','tab','dome-left');self.relate('connect','tab','dome-right')
        self.add_polyline('brim',(2,14),(30,14),(30,22),(2,22),closed=True)
        self.relate('connect','brim','dome-left');self.relate('connect','brim','dome-right')
        self.add_line('stand',(16,22),(16,30));self.add_line('foot',(10,30),(22,30));self.relate('connect','stand','brim');self.relate('connect','stand','foot')
