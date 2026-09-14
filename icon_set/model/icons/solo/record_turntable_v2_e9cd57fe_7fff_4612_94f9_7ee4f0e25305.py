# Variant of record-turntable; parent file remains unchanged.
'Record turntable: independent spacing revision.\n\nRetain a tonearm crossing the record from its deck pivot; remove the crowded separate control.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: disc-3: circular record construction. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e9cd57fe-7fff-4612-94f9-7ee4f0e25305'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/turntable 1_e9cd57fe-7fff-4612-94f9-7ee4f0e25305.svg'
AUTHOR = 'gpt-6'

class RecordTurntableVariant2(Solo48):
    icon_id = 'record-turntable-v2'
    variant_of = 'record-turntable'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('turntable', 'record player', 'vinyl', 'dj', 'music', 'audio', 'platter', 'deck')

    def build(self):
        self.add_polyline('deck',(6, 6),(42, 6),(42, 42),(6, 42),closed=True)
        self.add_arc('platter-a',(24, 15),(24, 33),radius_x=9,radius_y=9,sweep=True)
        self.add_arc('platter-b',(24, 33),(24, 15),radius_x=9,radius_y=9,sweep=True)
        self.add_contour('platter','platter-a','platter-b',closed=True)
        self.add_line('tonearm',(6, 42),(24, 24))
        self.relate('connect','tonearm','deck')
        self.relate('connect','tonearm','platter')
