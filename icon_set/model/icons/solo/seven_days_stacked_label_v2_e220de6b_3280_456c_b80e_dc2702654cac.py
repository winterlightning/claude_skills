# Variant of seven-days-stacked-label; parent file remains unchanged.
'Seven days stacked label: independent spacing revision.\n\nUse the same roomy DAY construction as 1 DAY, retaining the seven above.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: type and percent: consistent monoline characters and separated counters. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e220de6b-3280-456c-b80e-dc2702654cac'
SOURCE_PATH = 'pictographic-primitives/symbol/7day (text)_e220de6b-3280-456c-b80e-dc2702654cac.svg'
AUTHOR = 'gpt-6'

class SevenDaysStackedLabelVariant2(Solo48):
    icon_id = 'seven-days-stacked-label-v2'
    variant_of = 'seven-days-stacked-label'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/labels'
    aliases = ()
    keywords = ('7-days', 'days', 'seven', 'week', 'duration', 'trial', 'label', 'text')

    def build(self):
        self.add_polyline('seven',(18, 8),(30, 8),(22, 16),closed=False)
        self.add_polyline('d',(4, 24),(8, 24),(12, 28),(12, 36),(8, 40),(4, 40),closed=True)
        self.add_polyline('a',(20, 40),(20, 32),(20, 24),(28, 24),(28, 32),(28, 40),closed=False)
        self.add_line('a-bar',(20, 32),(28, 32))
        self.relate('connect','a','a-bar')
        self.add_polyline('y',(36, 24),(40, 32),(44, 24),closed=False)
        self.add_line('y-stem',(40, 32),(40, 40))
        self.relate('connect','y','y-stem')
