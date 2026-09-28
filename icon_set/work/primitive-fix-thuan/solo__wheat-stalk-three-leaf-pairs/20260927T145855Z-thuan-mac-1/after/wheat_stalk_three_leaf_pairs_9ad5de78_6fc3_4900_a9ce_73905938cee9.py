"""Wheat Grain Stalk.

Two mirrored pairs of pointed wheat leaves, regular 20-unit vertical repeat; omit the third pair after its retained-count layout failed the minimum hole size check. Centerline extremes (8,4)-(40,44). Lucide wheat informs repeated leaf symbols; retain source upright symmetry and omit veins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9ad5de78-6fc3-4900-a9ce-73905938cee9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wheat-stalk-three-leaf-pairs/20260927T145855Z-thuan-mac-1/reference/barley_9ad5de78-6fc3-4900-a9ce-73905938cee9.svg'
AUTHOR = 'gpt-6'

class WheatStalkThreeLeafPairs(Solo48):
    icon_id = 'wheat-stalk-three-leaf-pairs'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('wheat', 'grain', 'stalk')

    def build(self):
        # Three open mirrored leaf pairs preserve the source count without pinched counters.
        for index, top in enumerate((4, 18, 32)):
            root = (24, top + 6)
            self.add_bezier(f'leaf-left-{index}', root, ((17, top + 6), (10, top + 2), (8, top)))
            self.add_bezier(f'leaf-right-{index}', root, ((31, top + 6), (38, top + 2), (40, top)))
        self.add_line('stalk-top', (24, 10), (24, 24))
        self.add_line('stalk-middle', (24, 24), (24, 38))
        self.add_line('stalk-bottom', (24, 38), (24, 44))
        for index, segment in enumerate(('stalk-top', 'stalk-middle', 'stalk-bottom')):
            self.relate('connect', f'leaf-left-{index}', f'leaf-right-{index}', segment)
        self.relate('connect', 'stalk-top', 'stalk-middle')
        self.relate('connect', 'stalk-middle', 'stalk-bottom')
