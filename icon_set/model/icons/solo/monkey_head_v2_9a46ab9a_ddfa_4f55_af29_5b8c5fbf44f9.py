# Variant of monkey-head; parent file remains unchanged.
'Monkey head: independent spacing revision.\n\nOpen facial lobes and ears; shorter central mouth clears the curved jaw.\nNative solo family, HRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9a46ab9a-ddfa-4f55-af29-5b8c5fbf44f9'
SOURCE_PATH = 'pictographic-primitives/animals/monkey 1_9a46ab9a-ddfa-4f55-af29-5b8c5fbf44f9.svg'
AUTHOR = 'gpt-6'

class MonkeyHeadVariant2(Solo48):
    icon_id = 'monkey-head-v2'
    variant_of = 'monkey-head'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('monkey', 'head', 'animal')

    def build(self):
        self.add_line('left',(12, 30),(12, 18))
        self.add_arc('brow-left',(12, 18),(24, 18),radius_x=6,radius_y=10,sweep=True)
        self.add_arc('brow-right',(24, 18),(36, 18),radius_x=6,radius_y=10,sweep=True)
        self.add_line('right',(36, 18),(36, 30))
        self.add_arc('jaw-right',(36, 30),(24, 40),radius_x=12,radius_y=10,sweep=True)
        self.add_arc('jaw-left',(24, 40),(12, 30),radius_x=12,radius_y=10,sweep=True)
        self.add_contour('face','left','brow-left','brow-right','right','jaw-right','jaw-left',closed=True)
        self.add_arc('ear-left',(12, 18),(12, 30),radius_x=8,radius_y=6,sweep=False)
        self.add_arc('ear-right',(36, 18),(36, 30),radius_x=8,radius_y=6,sweep=True)
        self.relate('connect','face','ear-left')
        self.relate('connect','face','ear-right')
        self.add_line('mouth',(22, 30),(26, 30))
