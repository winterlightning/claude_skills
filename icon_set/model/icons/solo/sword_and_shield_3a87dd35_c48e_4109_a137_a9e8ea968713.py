"""Sword and Shield.

Plan: Upright broad sword beside curved D-profile shield. Remove inset shield panel and guard thickness. Lucide sword/shield informs broad silhouettes. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a87dd35-c48e-4109-a137-a9e8ea968713'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/cosplay weapon_3a87dd35-c48e-4109-a137-a9e8ea968713.svg'
AUTHOR = 'gpt-6'

class SwordAndShield(Solo48):
    icon_id = 'sword-and-shield'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hobbies'
    aliases = ()
    keywords = ('sword', 'and', 'shield')

    def build(self):
        self.add_polyline('blade',(11,8),(15,16),(15,28),(11,28),(7,28),(7,16),closed=True)
        self.add_polyline('guard',(4,28),(7,28),(11,28),(15,28),(18,28))
        self.add_line('grip',(11,28),(11,40))
        self.relate('connect','blade','guard');self.relate('connect','guard','grip')
        self.add_arc('shield-top',(28,10),(44,24),radius_x=16,radius_y=14)
        self.add_arc('shield-bottom',(44,24),(28,38),radius_x=16,radius_y=14)
        self.add_line('shield-flat',(28,38),(28,10))
        self.add_contour('shield','shield-top','shield-bottom','shield-flat',closed=True)
