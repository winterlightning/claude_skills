"""house phone: fresh SOLO48 repair.
Plan: Mirrored house with lower eaves; a curved handset and two joined terminal strokes.
Keyshape: SQUARE. Equal-width house provides space for the diagonal receiver.
Omissions: Receiver double outline and end loops simplified to an open stroke.
Construction reference: house and phone: coherent roof/wall contour and curved receiver with terminal ends.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7c7ae497-e683-4449-9d47-32e2c0e677e7'
SOURCE_PATH = 'pictographic-primitives/other/house phone_7c7ae497-e683-4449-9d47-32e2c0e677e7.svg'
AUTHOR = 'gpt-6'
PARENT_SOURCE = 'icon_set/model/icons/solo/house_phone_7c7ae497_e683_4449_9d47_32e2c0e677e7.py'

class Drawing(Solo48):
    icon_id = 'house-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/buildings'
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
        self.add_arc('receiver', (16, 21), (31, 33), radius_x=15, sweep=False)
        self.add_line('earpiece', (16, 21), (20, 24))
        self.add_line('mouthpiece', (31, 33), (28, 29))
        self.relate('connect', 'receiver', 'earpiece')
        self.relate('connect', 'receiver', 'mouthpiece')
