# Variant of four-wheel-drive-text-label; parent file remains unchanged.
'Four wheel drive text label: independent spacing revision.\n\nStack 4 above WD; angular D preserves exact inter-letter clearance.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: type and percent: consistent monoline characters and separated counters. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1dfab6f7-a053-5aee-8d2b-b99c63e6f3df'
SOURCE_PATH = 'pictographic-primitives/transportation/four wheel drive_1dfab6f7-a053-5aee-8d2b-b99c63e6f3df.svg'
AUTHOR = 'gpt-6'

class FourWheelDriveTextLabelVariant2(Solo48):
    icon_id = 'four-wheel-drive-text-label-v2'
    variant_of = 'four-wheel-drive-text-label'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('4wd', 'four wheel drive', '4x4', 'drivetrain', 'car', 'dashboard', 'text', 'label')

    def build(self):
        self.add_polyline('four',(20, 6),(20, 14),(28, 14),closed=False)
        self.add_polyline('stem',(28, 6),(28, 14),(28, 18),closed=False)
        self.relate('connect','four','stem')
        self.add_polyline('w',(6, 26),(6, 42),(14, 34),(22, 42),(22, 26),closed=False)
        self.add_polyline('d',(30, 26),(38, 26),(42, 30),(42, 38),(38, 42),(30, 42),closed=True)
