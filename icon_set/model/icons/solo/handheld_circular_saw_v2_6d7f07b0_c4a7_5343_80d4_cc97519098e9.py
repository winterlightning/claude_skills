# Variant of handheld-circular-saw; parent file remains unchanged.
'Handheld circular saw: independent spacing revision.\n\nReplace tiny blade notches with a broad exposed circular blade.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: hand: clear finger returns and rounded joins. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6d7f07b0-c4a7-5343-80d4-cc97519098e9'
SOURCE_PATH = 'pictographic-primitives/tools/power tools electric saw_6d7f07b0-c4a7-5343-80d4-cc97519098e9.svg'
AUTHOR = 'gpt-6'

class HandheldCircularSawVariant2(Solo48):
    icon_id = 'handheld-circular-saw-v2'
    variant_of = 'handheld-circular-saw'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('circular saw', 'saw', 'power tool', 'blade', 'cutting', 'woodworking', 'handheld', 'construction')

    def build(self):
        self.add_arc('guard',(10, 28),(42, 28),radius_x=16,radius_y=16,sweep=True)
        self.add_polyline('shoe',(6, 28),(10, 28),(14, 28),(26, 28),(38, 28),(42, 28),closed=False)
        self.add_polyline('handle',(10, 28),(6, 20),(6, 6),(26, 6),(26, 12),closed=False)
        self.relate('connect','shoe','guard')
        self.relate('connect','handle','guard')
        self.relate('connect','handle','shoe')
        self.add_arc('blade',(38, 28),(14, 28),radius_x=12,radius_y=14,sweep=True)
        self.relate('connect','blade','shoe')
