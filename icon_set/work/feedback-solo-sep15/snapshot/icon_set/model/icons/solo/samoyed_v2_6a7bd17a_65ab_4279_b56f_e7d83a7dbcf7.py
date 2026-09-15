'samoyed: independent smooth-curve repair.\n\nConstruction: Samoyed head with paired rounded ears, broad cheek arcs and short shoulder wisps; preserve the open lower face.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/cat.svg and atomic-debug/cat.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '6a7bd17a-65ab-4279-b56f-e7d83a7dbcf7'
SOURCE_PATH = 'pictographic-primitives/pets/samoyed_6a7bd17a-65ab-4279-b56f-e7d83a7dbcf7.svg'
AUTHOR = 'gpt-6'


class SamoyedVariant2(Solo48):
    icon_id = 'samoyed-v2'
    variant_of = 'samoyed'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('samoyed', 'pets')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'head',(12,34),('C',(8,32),(6,26),(8,19)),('C',(4,15),(4,8),(9,8)),('C',(12,8),(14,10),(15,11)),('C',(20,9),(28,9),(33,11)),('C',(34,10),(36,8),(39,8)),('C',(44,8),(44,15),(40,19)),('C',(42,26),(40,32),(36,34)))
        path(self,'left-fur',(12,34),('C',(8,34),(4,37),(4,40)))
        path(self,'right-fur',(36,34),('C',(40,34),(44,37),(44,40)))
        contacts(self)
