"""Make the handle a broader shallow half-ellipse, center it within a taller body opening, and give the two lower bag corners matching radii. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1e030fe3-e681-4ea5-a96f-2d26a7be5670'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bag-1e030fe3/20260927T070927Z-thuan-mac-1/reference/bag_1e030fe3-e681-4ea5-a96f-2d26a7be5670.svg'
AUTHOR = 'gpt-6'

class Bag1e030fe3(Solo48):
    icon_id = 'bag-1e030fe3'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'bag-1e030fe3')

    def build(self):
        # A flared shopping-bag body with its arched handle above the rim.
        self.add_line('rim-left',(12,18),(18,18))
        self.add_line('rim-center',(18,18),(30,18))
        self.add_line('rim-right',(30,18),(36,18))
        self.add_line('side-right',(36,18),(40,44))
        self.add_line('base',(40,44),(8,44))
        self.add_line('side-left',(8,44),(12,18))
        self.add_contour('body','rim-left','rim-center','rim-right',
                         'side-right','base','side-left',closed=True)
        self.add_line('handle-left',(18,18),(18,12))
        self.add_arc('handle-arch',(18,12),(30,12),radius_x=6,radius_y=8)
        self.add_line('handle-right',(30,12),(30,18))
        self.add_contour('handle','handle-left','handle-arch','handle-right')
        self.relate('connect','handle','body')
