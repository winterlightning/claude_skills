# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of graduation-cap-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e5ae7651-62d6-4c05-b34e-faf818f521bc'
SOURCE_PATH = 'pictographic-primitives/symbol/graduation cap_e5ae7651-62d6-4c05-b34e-faf818f521bc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e5ae7651-62d6-4c05-b34e-faf818f521bc', 'pictographic-primitives/symbol/graduation cap_e5ae7651-62d6-4c05-b34e-faf818f521bc.svg'), ('ac0c8839-9020-4a65-9a30-af5a45d63503', 'pictographic-primitives/accessories/batch-07/cap_ac0c8839-9020-4a65-9a30-af5a45d63503.svg'), ('5f6ee542-cdce-408a-b798-b60860e5b325', 'pictographic-primitives/accessories/batch-06/cap_5f6ee542-cdce-408a-b798-b60860e5b325.svg'))
PROFILE_SOURCE_KEYS = ('solo/graduation-cap-symbol', 'solo/academic-graduation-cap', 'solo/graduation-mortarboard')
SOLO_SOURCE_ICON_IDS = ('graduation-cap-symbol', 'academic-graduation-cap', 'graduation-mortarboard')
REFERENCE_EXPORT_SHA256 = '3db2ce90f5f70f0792c27acb4fbe21a247b788f59a72a50715d7930ff3bccb1b'

class DrawingVariant2(Sub32):
    icon_id = 'graduation-cap-symbol-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Shared diamond attachment points and a mirrored, smoothly rounded cap band.
        self.add_line('rim-a',(2,12),(6,14))
        self.add_line('rim-b',(6,14),(16,19))
        self.add_line('rim-c',(16,19),(26,14))
        self.add_line('rim-d',(26,14),(30,12))
        self.add_line('rim-e',(30,12),(16,4))
        self.add_line('rim-f',(16,4),(2,12))
        self.add_contour('rim','rim-a','rim-b','rim-c','rim-d','rim-e','rim-f',closed=True)
        self.add_line('band-left',(6,14),(6,23))
        self.add_bezier('band-bottom-left',(6,23),((6,26),(12,28),(16,28)))
        self.add_bezier('band-bottom-right',(16,28),((20,28),(26,26),(26,23)))
        self.add_line('band-right',(26,23),(26,14))
        self.add_contour('band','band-left','band-bottom-left','band-bottom-right','band-right',closed=False)
        for rim in ['rim-a','rim-b']: self.relate('connect',rim,'band-left')
        for rim in ['rim-c','rim-d']: self.relate('connect',rim,'band-right')
