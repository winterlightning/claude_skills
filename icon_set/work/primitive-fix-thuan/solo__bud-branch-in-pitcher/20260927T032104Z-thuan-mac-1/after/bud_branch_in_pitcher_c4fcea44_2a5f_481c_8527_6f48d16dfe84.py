'Bud branch in pitcher.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c4fcea44-2a5f-481c-8527-6f48d16dfe84'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bud-branch-in-pitcher/20260927T032104Z-thuan-mac-1/reference/vase plant_c4fcea44-2a5f-481c-8527-6f48d16dfe84.svg'
AUTHOR = "gpt-6"

class BudBranchInPitcher(Solo48):
    icon_id = 'bud-branch-in-pitcher'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('bud', 'branch', 'in', 'pitcher')

    def build(self) -> None:
        # A branching stem carries three round buds above a pitcher with a handle.
        self.add_polyline('pitcher', (10, 30), (31, 30), (31, 44), (11, 44), (12, 33), (10, 30))
        self.add_line('stem', (22, 30), (22, 12))
        self.add_polyline('branches', (11, 22), (22, 21), (33, 22))
        self.relate('connect', 'pitcher', 'stem')
        self.relate('connect', 'stem', 'branches')
        for name, x, y, radius in (('bud-top', 22, 8, 4), ('bud-left', 11, 19, 3), ('bud-right', 33, 19, 3)):
            self.add_arc(name+'-upper', (x-radius, y), (x+radius, y), radius_x=radius)
            self.add_arc(name+'-lower', (x+radius, y), (x-radius, y), radius_x=radius)
            self.add_contour(name, name+'-upper', name+'-lower', closed=True)
        self.relate('connect', 'bud-top', 'stem')
        self.relate('connect', 'bud-left', 'branches')
        self.relate('connect', 'bud-right', 'branches')
        self.add_arc('handle', (31, 31), (31, 41), radius_x=9, radius_y=5)
        self.relate('connect', 'handle', 'pitcher')
