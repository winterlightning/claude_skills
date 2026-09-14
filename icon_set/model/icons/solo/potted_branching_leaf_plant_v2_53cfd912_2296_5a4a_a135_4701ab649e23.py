# Variant of potted-branching-leaf-plant; parent file remains unchanged.
'Potted branching leaf plant: independent spacing revision.\n\nReduce five cramped leaves to two broad branching leaves; deepen pot to ten units.\nNative solo family, VRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: sprout: broad leaf silhouettes around a central stem. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '53cfd912-2296-5a4a-a135-4701ab649e23'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_53cfd912-2296-5a4a-a135-4701ab649e23.svg'
AUTHOR = 'gpt-6'

class PottedBranchingLeafPlantVariant2(Solo48):
    icon_id = 'potted-branching-leaf-plant-v2'
    variant_of = 'potted-branching-leaf-plant'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/plants'
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self):
        self.add_arc('left-a',(8, 4),(24, 20),radius_x=16,radius_y=16,sweep=True)
        self.add_arc('left-b',(24, 20),(8, 4),radius_x=16,radius_y=16,sweep=True)
        self.add_contour('left-leaf','left-a','left-b',closed=True)
        self.add_arc('right-a',(24, 20),(40, 4),radius_x=16,radius_y=16,sweep=True)
        self.add_arc('right-b',(40, 4),(24, 20),radius_x=16,radius_y=16,sweep=True)
        self.add_contour('right-leaf','right-a','right-b',closed=True)
        self.add_line('stem',(24, 20),(24, 34))
        self.add_polyline('pot',(16, 34),(24, 34),(32, 34),(30, 44),(18, 44),closed=True)
        self.relate('connect','left-leaf','right-leaf')
        self.relate('connect','stem','left-leaf')
        self.relate('connect','stem','right-leaf')
        self.relate('connect','stem','pot')
