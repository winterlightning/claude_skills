'wristband: independent smooth-curve repair.\n\nConstruction: Wristband with an elliptical rear rim and a centered rounded clasp; paired smooth front band sections.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/watch.svg and atomic-debug/watch.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'd01c7ceb-a077-5369-924c-20e53e6260db'
SOURCE_PATH = 'pictographic-primitives/events/wristband_d01c7ceb-a077-5369-924c-20e53e6260db.svg'
AUTHOR = 'gpt-6'


class Wristband(Solo48):
    icon_id = 'wristband'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'events'
    aliases = ()
    keywords = ('wristband', 'events')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'rim',(18,28),('C',(10,27),(4,24),(4,18)),('A',20,10,True,(24,8)),('A',20,10,True,(44,18)),('C',(44,24),(38,27),(30,28)))
        box(self,'clasp',18,26,30,40,2)
        path(self,'left-band',(4,18),('L',(4,29)),('C',(4,35),(10,38),(18,38)))
        path(self,'right-band',(44,18),('L',(44,29)),('C',(44,35),(38,38),(30,38)))
        contacts(self)
