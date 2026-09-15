'playstation-five-joy: independent smooth-curve repair.\n\nConstruction: Game controller with broad rounded grips and centered thumb buttons; paired controls and a smooth central saddle.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/gamepad-2.svg and atomic-debug/gamepad-2.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '98c659a9-5582-453f-ab4e-3cfe3c3fd603'
SOURCE_PATH = 'pictographic-primitives/video-games/playstation five joy_98c659a9-5582-453f-ab4e-3cfe3c3fd603.svg'
AUTHOR = 'gpt-6'


class PlaystationFiveJoyVariant2(Solo48):
    icon_id = 'playstation-five-joy-v2'
    variant_of = 'playstation-five-joy'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('playstation', 'five', 'joy', 'video-games')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'body',(14,8),('L',(34,8)),('C',(39,8),(40,12),(41,18)),('L',(44,34)),('C',(44,38),(42,40),(40,40)),('C',(39,40),(38,39),(37,38)),('L',(30,31)),('C',(27,28),(21,28),(18,31)),('L',(11,38)),('C',(10,39),(9,40),(8,40)),('C',(6,40),(4,38),(4,34)),('L',(7,18)),('C',(8,12),(9,8),(14,8)),closed=True)
        self.add_dot('left-button',(17,20));self.add_dot('right-button',(31,20))
        contacts(self)
