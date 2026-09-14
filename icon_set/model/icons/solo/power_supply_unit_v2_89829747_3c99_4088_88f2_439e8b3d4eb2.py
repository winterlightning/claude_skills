# Variant of power-supply-unit; parent file remains unchanged.
'Power supply unit: independent spacing revision.\n\nRetain fan opening and a simple power mark; remove internal braces and crowded socket outline.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '89829747-3c99-4088-88f2-439e8b3d4eb2'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/power supply_89829747-3c99-4088-88f2-439e8b3d4eb2.svg'
AUTHOR = 'gpt-6'

class PowerSupplyUnitVariant2(Solo48):
    icon_id = 'power-supply-unit-v2'
    variant_of = 'power-supply-unit'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('power supply', 'psu', 'computer', 'fan', 'hardware', 'socket', 'electricity', 'component')

    def build(self):
        self.add_polyline('panel',(4, 8),(44, 8),(44, 40),(4, 40),closed=True)
        self.add_arc('fana',(13, 24),(27, 24),radius_x=7,radius_y=7)
        self.add_arc('fanb',(27, 24),(13, 24),radius_x=7,radius_y=7)
        self.add_contour('fan','fana','fanb',closed=True)
        self.add_dot('power',(36, 24))
