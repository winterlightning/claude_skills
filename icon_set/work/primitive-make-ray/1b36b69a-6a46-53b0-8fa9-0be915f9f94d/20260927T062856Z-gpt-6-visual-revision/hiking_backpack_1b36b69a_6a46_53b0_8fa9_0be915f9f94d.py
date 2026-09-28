"""Fresh SOLO48 revision of hiking-backpack from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '1b36b69a-6a46-53b0-8fa9-0be915f9f94d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hiking-backpack/20260927T061852Z-thuan-mac-1/reference/outdoors backpack_1b36b69a-6a46-53b0-8fa9-0be915f9f94d.svg'
AUTHOR = "gpt-6"

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

        # Overhanging top flap, central front pocket and side pockets.
        box(self,'body',12,10,36,42,5,ys=(24,36))
        box(self,'flap',10,10,38,22,4)
        poly(self,'front-pocket',(19,22),(19,32),(29,32),(29,22))
        poly(self,'side-left',(12,27),(7,27),(7,38),(12,38))
        poly(self,'side-right',(36,27),(41,27),(41,38),(36,38))
        contacts(self)
