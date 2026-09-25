"""house unlock: fresh SOLO48 repair.
Plan: Rectangular lock body with a split attachment rail and curved open hook.
Keyshape: SQUARE. House provides a balanced enclosure for the open lock.
Omissions: Body corner fillets reduced to round joins; short asymmetric shackle retained.
Construction reference: house: coherent enclosure and smooth base corners.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd9e732b9-6854-4fe7-b39f-365bfd54abee'
SOURCE_PATH = 'pictographic-primitives/other/house unlock_d9e732b9-6854-4fe7-b39f-365bfd54abee.svg'
AUTHOR = 'gpt-6'
PARENT_SOURCE = 'icon_set/model/icons/solo/house_unlock_d9e732b9_6854_4fe7_b39f_365bfd54abee.py'

class Drawing(Solo48):
    icon_id = 'house-unlock'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/buildings'
    aliases = ()
    keywords = ('house', 'unlock')

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
        self.add_polyline('lock-body', (16, 25), (20, 25), (32, 25), (32, 33), (16, 33), closed=True)
        self.add_line('shackle-rise', (20, 25), (20, 20))
        self.add_arc('shackle-bend', (20, 20), (24, 16), radius_x=4)
        self.add_line('open-tip', (24, 16), (26, 16))
        self.add_contour('shackle', 'shackle-rise', 'shackle-bend', 'open-tip')
        self.relate('connect', 'shackle', 'lock-body')
