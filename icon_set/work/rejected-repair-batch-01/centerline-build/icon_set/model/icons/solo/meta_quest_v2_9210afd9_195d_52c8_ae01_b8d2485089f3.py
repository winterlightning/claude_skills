'meta-quest: independent smooth-curve repair.\n\nConstruction: VR headset retaining its upper headband: elliptical strap arch joined at the rounded goggles brow; paired temples and a smooth centered nose saddle.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/gamepad-2.svg and atomic-debug/gamepad-2.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '9210afd9-195d-52c8-ae01-b8d2485089f3'
SOURCE_PATH = 'pictographic-primitives/technology/meta quest_9210afd9-195d-52c8-ae01-b8d2485089f3.svg'
AUTHOR = 'gpt-6'


class MetaQuestVariant2(Solo48):
    icon_id = 'meta-quest-v2'
    variant_of = 'meta-quest'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('meta', 'quest', 'technology')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'headband',(8,18),('A',16,10,True,(24,8)),('A',16,10,True,(40,18)))
        path(self,'goggles',(8,18),('L',(40,18)),('A',4,4,True,(44,22)),('L',(44,33)),('C',(44,37),(40,40),(35,40)),('C',(30,40),(30,31),(24,31)),('C',(18,31),(18,40),(13,40)),('C',(8,40),(4,37),(4,33)),('L',(4,22)),('A',4,4,True,(8,18)),closed=True)
        contacts(self)
