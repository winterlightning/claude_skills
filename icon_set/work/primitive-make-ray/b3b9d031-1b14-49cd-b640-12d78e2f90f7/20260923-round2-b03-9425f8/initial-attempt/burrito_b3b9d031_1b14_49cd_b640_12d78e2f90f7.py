from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b3b9d031-1b14-49cd-b640-12d78e2f90f7'
SOURCE_PATH = 'icon_set/work/todo-references/burrito_b3b9d031-1b14-49cd-b640-12d78e2f90f7.svg'
AUTHOR = 'gpt-6'

PLAN = 'A wrapped burrito with bowed seam and diagonal fold; split both curved contact locations at integer shared endpoints.'
PARENT_RESULT = 'icon_set/work/primitive-make-ray/b3b9d031-1b14-49cd-b640-12d78e2f90f7/20260922T221723-c23937/result.json'

class Drawing(Solo48):
    icon_id = 'burrito'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('medical', 'capsule')

    def build(self):
        self.add_line('top',(18,10),(30,10))
        self.add_arc('right',(30,10),(30,38),radius_x=14)
        self.add_line('bottom',(30,38),(18,38))
        self.add_arc('left-lower',(18,38),(4,24),radius_x=14)
        self.add_arc('left-upper',(4,24),(18,10),radius_x=14)
        self.add_contour('outline','top','right','bottom','left-lower','left-upper',closed=True)
        self.add_bezier('seam-upper',(18,10),((20,12),(22,14),(24,18)))
        self.add_bezier('seam-lower',(24,18),((28,26),(26,36),(18,38)))
        self.add_contour('seam','seam-upper','seam-lower')
        self.add_line('fold',(4,24),(24,18))
        self.relate('connect','seam-upper','top','left-upper')
        self.relate('connect','seam-lower','bottom','left-lower')
        self.relate('connect','fold','left-lower','left-upper','seam-upper','seam-lower')
