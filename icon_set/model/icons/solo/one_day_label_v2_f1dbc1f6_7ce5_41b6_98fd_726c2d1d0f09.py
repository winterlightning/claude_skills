# Variant of one-day-label; parent file remains unchanged.
'One day label: independent spacing revision.\n\nPreserve 1 DAY with full-width D, eight-unit A bands and an open Y.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: type and percent: consistent monoline characters and separated counters. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f1dbc1f6-7ce5-41b6-98fd-726c2d1d0f09'
SOURCE_PATH = 'pictographic-primitives/symbol/1day (text)_f1dbc1f6-7ce5-41b6-98fd-726c2d1d0f09.svg'
AUTHOR = 'gpt-6'

class OneDayLabelVariant2(Solo48):
    icon_id = 'one-day-label-v2'
    variant_of = 'one-day-label'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/labels'
    aliases = ()
    keywords = ('1-day', 'day', 'one', 'duration', 'label', 'time', 'delivery', 'text')

    def build(self):
        self.add_polyline('one',(20, 11),(24, 8),(24, 16),closed=False)
        self.add_polyline('d',(4, 24),(8, 24),(12, 28),(12, 36),(8, 40),(4, 40),closed=True)
        self.add_polyline('a',(20, 40),(20, 32),(20, 24),(28, 24),(28, 32),(28, 40),closed=False)
        self.add_line('a-bar',(20, 32),(28, 32))
        self.relate('connect','a','a-bar')
        self.add_polyline('y',(36, 24),(40, 32),(44, 24),closed=False)
        self.add_line('y-stem',(40, 32),(40, 40))
        self.relate('connect','y','y-stem')
