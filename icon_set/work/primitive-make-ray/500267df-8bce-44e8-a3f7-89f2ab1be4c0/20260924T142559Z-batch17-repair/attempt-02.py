"""shield 3: standalone batch 17 repair.
Retained the crowned shield, horizontal band and pointed lower body. Lowered the band to open the space beneath the crown valleys.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '500267df-8bce-44e8-a3f7-89f2ab1be4c0'
SOURCE_PATH = 'pictographic-primitives/other/shield 3_500267df-8bce-44e8-a3f7-89f2ab1be4c0.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'shield'

class AuthoredIcon(Solo48):
    icon_id = 'shield-3'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('shield', '3')

    def build(self):
        self.add_polyline('crown',(8,21),(8,8),(14,11),(24,4),(34,11),(40,8),(40,21))
        self.add_line('band',(8,21),(40,21))
        self.add_bezier('lower',(40,21),((40,29),(35,37),(24,44)),((13,37),(8,29),(8,21)))
        self.relate('connect','crown','band');self.relate('connect','band','lower');self.relate('connect','crown','lower')

