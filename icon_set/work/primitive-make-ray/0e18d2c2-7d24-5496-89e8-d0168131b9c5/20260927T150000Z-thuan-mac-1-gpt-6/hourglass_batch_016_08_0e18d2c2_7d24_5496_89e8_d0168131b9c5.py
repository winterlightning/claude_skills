from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0e18d2c2-7d24-5496-89e8-d0168131b9c5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hourglass-batch-016-08/20260927T145836Z-thuan-mac-1/reference/hourglass_0e18d2c2-7d24-5496-89e8-d0168131b9c5.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/references/hourglass_0e18d2c2-7d24-5496-89e8-d0168131b9c5.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/08-simple-hourglass-time-symbol--0e18d2c2-7d24-5496-89e8-d0168131b9c5.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Chambers use deliberate straight slopes instead of many small curves.']
CONSTRUCTION_REFERENCE = 'hourglass: broad caps and a pinched waist.'

class BatchIcon(Solo48):
    icon_id = 'hourglass-batch-016-08'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    keywords = ('hourglass', 'time', 'timer', 'glass', 'chambers', 'waist')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        # Matching curved bowls replace the angular bow-tie silhouette.
        self.add_line('top', (8, 4), (40, 4))
        self.add_line('right-upper-wall', (40, 4), (40, 12))
        self.add_bezier('right-upper-bowl', (40, 12), ((40, 19), (29, 20), (24, 24)))
        self.add_bezier('right-lower-bowl', (24, 24), ((29, 28), (40, 29), (40, 36)))
        self.add_line('right-lower-wall', (40, 36), (40, 44))
        self.add_line('bottom', (40, 44), (8, 44))
        self.add_line('left-lower-wall', (8, 44), (8, 36))
        self.add_bezier('left-lower-bowl', (8, 36), ((8, 29), (19, 28), (24, 24)))
        self.add_bezier('left-upper-bowl', (24, 24), ((19, 20), (8, 19), (8, 12)))
        self.add_line('left-upper-wall', (8, 12), (8, 4))
        self.add_contour('glass', 'top', 'right-upper-wall', 'right-upper-bowl', 'right-lower-bowl', 'right-lower-wall', 'bottom', 'left-lower-wall', 'left-lower-bowl', 'left-upper-bowl', 'left-upper-wall', closed=True)
