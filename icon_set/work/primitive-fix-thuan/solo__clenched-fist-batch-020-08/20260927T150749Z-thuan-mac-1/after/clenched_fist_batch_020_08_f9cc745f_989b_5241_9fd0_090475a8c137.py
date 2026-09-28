from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f9cc745f-989b-5241-9fd0-090475a8c137'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__clenched-fist-batch-020-08/20260927T150749Z-thuan-mac-1/reference/hand fist bump_f9cc745f-989b-5241-9fd0-090475a8c137.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/hand fist bump_f9cc745f-989b-5241-9fd0-090475a8c137.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/08-clenched-hand-fist--f9cc745f-989b-5241-9fd0-090475a8c137.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Lower finger seam and palm curve omitted to retain an open fist interior.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'clenched-fist-batch-020-08'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    keywords = ('hand', 'fist', 'clenched', 'gesture', 'knuckles', 'fingers', 'arm', 'bump')

    def build(self):
        # The upper palm, three rounded knuckles and wrist are one open contour.
        self.add_line('wrist-upper',(4,16),(10,16))
        self.add_bezier('palm-top',(10,16),((14,16),(16,8),(24,8)))
        self.add_line('knuckle-top',(24,8),(34,8))
        self.add_bezier('finger-top',(34,8),((40,8),(44,10),(44,15)))
        self.add_bezier('finger-upper',(44,15),((44,18),(43,20),(42,21)))
        self.add_bezier('finger-middle',(42,21),((44,23),(44,27),(42,29)))
        self.add_bezier('finger-lower',(42,29),((44,31),(44,33),(42,35)))
        self.add_bezier('hand-bottom',(42,35),((42,38),(40,40),(38,40)))
        self.add_line('palm-bottom',(38,40),(18,40))
        self.add_bezier('wrist-lower',(18,40),((14,40),(12,34),(10,34)))
        self.add_line('wrist-end',(10,34),(4,34))
        self.add_contour('outline','wrist-upper','palm-top','knuckle-top','finger-top','finger-upper','finger-middle','finger-lower','hand-bottom','palm-bottom','wrist-lower','wrist-end')
        self.add_bezier('thumb-a',(20,8),((21,14),(23,19),(26,20)))
        self.add_bezier('thumb-b',(26,20),((30,23),(33,23),(36,18)))
        self.add_contour('thumb','thumb-a','thumb-b')
        self.add_line('finger-seam-upper',(34,21),(42,21))
        self.relate('connect','outline','thumb')
        self.relate('connect','outline','finger-seam-upper')
