"""Revision of the claimed reference after comparing original and rejected drawing."""
"""house phone: fresh SOLO48 repair.
Plan: Mirrored house with lower eaves; a curved handset and two joined terminal strokes.
Keyshape: SQUARE. Equal-width house provides space for the diagonal receiver.
Omissions: Receiver double outline and end loops simplified to an open stroke.
Construction reference: house and phone: coherent roof/wall contour and curved receiver with terminal ends.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7c7ae497-e683-4449-9d47-32e2c0e677e7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__house-phone/20260927T142529Z-thuan-mac-1/reference/house phone_7c7ae497-e683-4449-9d47-32e2c0e677e7.svg'
AUTHOR = 'gpt-6'
PARENT_SOURCE = 'icon_set/model/icons/solo/house_phone_7c7ae497_e683_4449_9d47_32e2c0e677e7.py'

class Drawing(Solo48):
    icon_id = 'house-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('house', 'phone')

    def house(self):
        self.add_line('roof-1', (6, 14), (24, 6))
        self.add_line('roof-2', (24, 6), (42, 14))
        self.add_line('wall-right', (42, 14), (42, 40))
        self.add_arc('corner-right', (42, 40), (40, 42), radius_x=2)
        self.add_line('floor', (40, 42), (8, 42))
        self.add_arc('corner-left', (8, 42), (6, 40), radius_x=2)
        self.add_line('wall-left', (6, 40), (6, 14))
        self.add_contour('house', 'roof-1', 'roof-2', 'wall-right', 'corner-right', 'floor', 'corner-left', 'wall-left', closed=True)

    def build(self):
        self.house()
        self.add_arc('receiver', (15, 20), (33, 32), radius_x=18, sweep=False)
        self.add_polyline('earpiece',(14,18),(15,20),(19,23))
        self.add_line('mouthpiece',(33,32),(29,28))
        self.relate('connect', 'receiver', 'earpiece')
        self.relate('connect', 'receiver', 'mouthpiece')

# Explicit user approval for this exact SVG; changes invalidate the exception.
