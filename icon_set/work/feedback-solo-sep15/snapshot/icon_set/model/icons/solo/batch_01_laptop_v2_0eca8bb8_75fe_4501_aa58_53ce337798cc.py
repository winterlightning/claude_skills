'batch-01-laptop: independent smooth-curve repair.\n\nConstruction: Rounded laptop display and a softly flared base, joined at the hinge.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/laptop.svg and atomic-debug/laptop.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '0eca8bb8-75fe-4501-aa58-53ce337798cc'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/laptop_0eca8bb8-75fe-4501-aa58-53ce337798cc.svg'
AUTHOR = 'gpt-6'


class Batch01LaptopVariant2(Solo48):
    icon_id = 'batch-01-laptop-v2'
    variant_of = 'batch-01-laptop'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'laptop', 'computers')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'screen',(8,30),('L',(8,12)),('A',4,4,True,(12,8)),('L',(36,8)),('A',4,4,True,(40,12)),('L',(40,30)))
        path(self,'base',(8,30),('L',(40,30)),('L',(44,36)),('C',(44,39),(42,40),(39,40)),('L',(9,40)),('C',(6,40),(4,39),(4,36)),('L',(8,30)),closed=True)
        contacts(self)
