"""Three blossoms with paired leaves in a rounded vase. SQUARE (2,2)-(46,46). Lucide flower informs repeated broad petal arcs. Four lobes replace fine scallops; paired leaves simplified to curved strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d236e3c-000a-4b02-9065-9a95cf6d2b26'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/vase plant_0d236e3c-000a-4b02-9065-9a95cf6d2b26.svg'
AUTHOR = 'gpt-6'


class ThreeBlossomVaseWithPairedLeaves(Solo48):
    icon_id = 'three-blossom-vase-with-paired-leaves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('vase', 'flowers', 'blossoms', 'bouquet', 'leaves', 'plant', 'decor')

    def build(self) -> None:
        self.add_arc('left0', (9, 5), (15, 5), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('left1', (15, 5), (15, 11), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('left3', (9, 11), (9, 5), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('left2a', (15, 11), (12, 14), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('left2b', (12, 14), (9, 11), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('left', 'left0', 'left1', 'left2a', 'left2b', 'left3', closed=True)
        self.add_arc('right0', (33, 5), (39, 5), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('right1', (39, 5), (39, 11), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('right3', (33, 11), (33, 5), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('right2a', (39, 11), (36, 14), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('right2b', (36, 14), (33, 11), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('right', 'right0', 'right1', 'right2a', 'right2b', 'right3', closed=True)
        self.add_arc('front0', (21, 23), (27, 23), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('front1', (27, 23), (27, 29), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('front3', (21, 29), (21, 23), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('front2a', (27, 29), (24, 32), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('front2b', (24, 32), (21, 29), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('front', 'front0', 'front1', 'front2a', 'front2b', 'front3', closed=True)
        self.add_line('stem-left', (15, 11), (21, 23))
        self.add_line('stem-right', (33, 11), (27, 23))
        self.relate('connect', 'stem-left', 'left')
        self.relate('connect', 'stem-left', 'front')
        self.relate('connect', 'stem-right', 'right')
        self.relate('connect', 'stem-right', 'front')
        self.add_arc('leaf-left', (2, 21), (18, 26), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('leaf-right', (30, 26), (46, 21), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.relate('connect', 'leaf-left', 'front')
        self.relate('connect', 'leaf-right', 'front')
        self.add_line('vase-l', (14, 33), (14, 40))
        self.add_arc('vase-bl', (14, 40), (20, 46), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_line('vase-b', (20, 46), (28, 46))
        self.add_arc('vase-br', (28, 46), (34, 40), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_line('vase-r', (34, 40), (34, 33))
        self.add_contour('vase', 'vase-l', 'vase-bl', 'vase-b', 'vase-br', 'vase-r', closed=False)
