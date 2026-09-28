"""Fresh SOLO48 revision of hiking-backpack from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '1b36b69a-6a46-53b0-8fa9-0be915f9f94d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hiking-backpack/20260927T061852Z-thuan-mac-1/reference/outdoors backpack_1b36b69a-6a46-53b0-8fa9-0be915f9f94d.svg'
AUTHOR = 'gpt-6'

class HikingBackpack(Solo48):
    icon_id = 'hiking-backpack'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('backpack', 'hiking', 'rucksack', 'camping', 'travel', 'bag', 'outdoors', 'outdoors-batch-02')

    def build(self) -> None:

        # Rounded main bag with projecting side pockets and a hanging flap tab.
        path(self,'body',(16,6),('L',(32,6)),('A',4,4,True,(36,10)),
             ('L',(36,24)),('L',(42,24)),('L',(42,38)),('L',(36,38)),
             ('A',4,4,True,(32,42)),('L',(16,42)),('A',4,4,True,(12,38)),
             ('L',(6,38)),('L',(6,24)),('L',(12,24)),('L',(12,10)),
             ('A',4,4,True,(16,6)),closed=True)
        line(self,'flap',(12,18),(36,18))
        poly(self,'tab',(20,18),(20,30),(28,30),(28,18))
        contacts(self)
