"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: handset.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.symbol._base import Symbol32 as Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '7099417a-0fa8-4ad5-84bf-e77a845b942a'
SOURCE_PATH = 'pictographic-primitives/state/phone 1_7099417a-0fa8-4ad5-84bf-e77a845b942a.svg'
AUTHOR = 'gpt-6'

class CompleteReferenceRedrawContainerSymbol(Sub32):
    icon_id = 'telephone-handset-state-204-v2-symbol'
    related_origin_icon_id = 'telephone-handset-state-204-v2'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/telephone-handset-state-204-v2'
    counterpart_icon_id = 'telephone-handset-state-204-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)

    def build(self):
        self.add_line('handset-0-0', (7, 2), (14, 9))
        self.add_line('handset-0-1', (14, 9), (11, 13))
        self.add_bezier('handset-0-2', (11, 13), ((13.0, 17.0), (16.0, 20.0), (20, 21)))
        self.add_line('handset-0-3', (20, 21), (23, 18))
        self.add_line('handset-0-4', (23, 18), (30, 25))
        self.add_bezier('handset-0-5', (30, 25), ((30.0, 28.0), (27.0, 30.0), (24, 30)))
        self.add_bezier('handset-0-6', (24, 30), ((14.0, 29.0), (3.0, 18.0), (2, 8)))
        self.add_bezier('handset-0-7', (2, 8), ((2.0, 5.0), (4.0, 2.0), (7, 2)))
        self.add_contour('handset-0', 'handset-0-0', 'handset-0-1', 'handset-0-2', 'handset-0-3', 'handset-0-4', 'handset-0-5', 'handset-0-6', 'handset-0-7', closed=True)
