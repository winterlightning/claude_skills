'skull-interface-essential: independent smooth-curve repair.\n\nConstruction: Skull with circular crown and smooth cheeks; eye dots stay separate and the jaw has a central tooth notch.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/skull.svg and atomic-debug/skull.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '83b97801-31fc-4c2f-86e6-c8775e2ddea6'
SOURCE_PATH = 'pictographic-primitives/interface-essential/skull_83b97801-31fc-4c2f-86e6-c8775e2ddea6.svg'
AUTHOR = 'gpt-6'


class SkullInterfaceEssential(Solo48):
    icon_id = 'skull-interface-essential'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'skull',(24,8),('C',(12,8),(4,17),(4,25)),('C',(4,30),(12,29),(12,34)),('L',(12,36)),('A',4,4,False,(16,40)),('L',(24,40)),('L',(32,40)),('A',4,4,False,(36,36)),('L',(36,34)),('C',(36,29),(44,30),(44,25)),('C',(44,17),(36,8),(24,8)),closed=True)
        self.add_dot('eye-left',(16,23));self.add_dot('eye-right',(32,23))
        line(self,'tooth',(24,33),(24,40))
        contacts(self)
