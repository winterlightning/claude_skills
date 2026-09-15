"""PC monogram and baseline; remove the outer square to give the two letters legal counters and separation."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f4a1dd4-8c41-49a8-93a3-7637d13903a6'
SOURCE_PATH = 'pictographic-primitives/logos/pycharm logo_5f4a1dd4-8c41-49a8-93a3-7637d13903a6.svg'
AUTHOR = 'gpt-6'

class PycharmLogo(Solo48):
    icon_id = 'pycharm-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('pycharm', 'jetbrains', 'python', 'ide', 'logo', 'brand', 'developer')

    def build(self):
        # Plan: PC monogram and baseline; remove the outer square to give the two letters legal counters and separation.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('p-stem',(6,6),(6,22),(6,28))
        self.add_arc('p-bowl',(6,6),(6,22),radius_x=14,radius_y=8)
        self.relate('connect','p-stem','p-bowl')
        self.add_arc('c',(42,6),(42,28),radius_x=12,radius_y=11,sweep=False)
        self.add_line('baseline',(6,42),(20,42))

