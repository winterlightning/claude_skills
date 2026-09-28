'Six-leaf vine: six alternating curved leaves with clear counters and a shared stem, preserving the alternating rhythm.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5044236b-6b82-4b28-beb5-504a9abb027a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__six-leaf-hanging-vine/20260927T093511Z-thuan-mac-1/reference/hanging plant 4_5044236b-6b82-4b28-beb5-504a9abb027a.svg'
AUTHOR = 'gpt-6'

class SixLeafHangingVine(Solo48):
    icon_id = 'six-leaf-hanging-vine'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "decoration"
    categories = ("primitives", "decoration")
    aliases = ()
    keywords = ('vine', 'hanging', 'leaves', 'stem', 'foliage', 'plant', 'botanical')

    def build(self) -> None:
        # Three shared stem nodes each own two offset, pointed leaves.
        self.add_polyline('stem', (24, 8), (24, 24), (24, 40))
        for j, y in enumerate((8, 24, 40)):
            up = 4 if j == 0 else 4.8
            down = 4 if j == 2 else 4.8
            left = f'leaf-left-{j}'
            right = f'leaf-right-{j}'
            self.add_bezier(left+'-upper', (24, y),
                            ((20, y-up), (12, y-up), (8, y-4)))
            self.add_bezier(left+'-lower', (8, y-4),
                            ((10, y+down), (18, y+down), (24, y)))
            self.add_contour(left, left+'-upper', left+'-lower', closed=True)
            self.add_bezier(right+'-upper', (24, y),
                            ((30, y-up), (36, y-up), (40, y+4)))
            self.add_bezier(right+'-lower', (40, y+4),
                            ((36, y+down), (30, y+down), (24, y)))
            self.add_contour(right, right+'-upper', right+'-lower', closed=True)
            self.relate('connect', left, 'stem')
            self.relate('connect', right, 'stem')
            self.relate('connect', left, right)
