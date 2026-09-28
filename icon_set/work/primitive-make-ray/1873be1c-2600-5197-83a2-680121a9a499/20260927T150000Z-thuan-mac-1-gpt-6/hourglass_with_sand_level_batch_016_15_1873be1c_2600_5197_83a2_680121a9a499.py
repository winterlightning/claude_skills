from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1873be1c-2600-5197-83a2-680121a9a499'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hourglass-with-sand-level-batch-016-15/20260927T145836Z-thuan-mac-1/reference/hourglass_1873be1c-2600-5197-83a2-680121a9a499.svg'
AUTHOR = "gpt-6"
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/references/hourglass_1873be1c-2600-5197-83a2-680121a9a499.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/15-traditional-sand-timer-icon--1873be1c-2600-5197-83a2-680121a9a499.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Chambers use deliberate straight slopes instead of many small curves.']
CONSTRUCTION_REFERENCE = 'hourglass: broad caps and a pinched waist.'

class BatchIcon(Solo48):
    icon_id = 'hourglass-with-sand-level-batch-016-15'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    keywords = ('hourglass', 'sand', 'timer', 'time', 'glass', 'chambers')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
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
        self.add_line('sand', (21, 13), (27, 13))
