"""Telephone Handset: A curved handset runs from upper left to lower right, joining two widened earpieces. Rounded corners soften the ends and the deep inner bend of its connecting grip.

Construction: Diagonal telephone handset preserves two angled earpieces and curved connecting grip; Lucide phone informs coherent outer sweep.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7099417a-0fa8-4ad5-84bf-e77a845b942a'
SOURCE_PATH = 'pictographic-primitives/state/phone 1_7099417a-0fa8-4ad5-84bf-e77a845b942a.svg'
AUTHOR = 'gpt-6'

class TelephoneHandsetState204ContainerSymbol(Sub32):
    icon_id = 'telephone-handset-state-204-symbol'
    related_origin_icon_id = 'telephone-handset-state-204'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/telephone-handset-state-204'
    counterpart_icon_id = 'telephone-handset-state-204'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('telephone', 'handset', 'curved', 'runs', 'upper', 'left', 'lower', 'right')

    def build(self):
        self.add_arc('upper-corner', (2, 6), (6, 2), radius_x=4)
        self.add_line('upper-edge', (6, 2), (12, 8))
        self.add_arc('upper-turn', (12, 8), (12, 12), radius_x=3)
        self.add_line('upper-neck', (12, 12), (10, 14))
        self.add_arc('grip', (10, 14), (18, 22), radius_x=18, sweep=False)
        self.add_line('lower-neck', (18, 22), (20, 20))
        self.add_arc('lower-turn', (20, 20), (24, 20), radius_x=3)
        self.add_line('lower-edge', (24, 20), (30, 26))
        self.add_arc('lower-corner', (30, 26), (26, 30), radius_x=4)
        self.add_arc('outer', (26, 30), (2, 6), radius_x=24)
        self.add_contour('handset', 'upper-corner', 'upper-edge', 'upper-turn', 'upper-neck', 'grip', 'lower-neck', 'lower-turn', 'lower-edge', 'lower-corner', 'outer', closed=True)
