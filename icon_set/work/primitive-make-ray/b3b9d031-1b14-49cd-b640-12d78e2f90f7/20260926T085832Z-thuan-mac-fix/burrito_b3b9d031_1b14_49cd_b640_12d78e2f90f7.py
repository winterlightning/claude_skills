from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b3b9d031-1b14-49cd-b640-12d78e2f90f7"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__burrito/20260926T085631Z-thuan-mac/reference/burrito_b3b9d031-1b14-49cd-b640-12d78e2f90f7.svg"
AUTHOR = "claude-opus-5-5"

PLAN = 'A wrapped burrito with bowed seam and diagonal fold; split both curved contact locations at integer shared endpoints.'
PARENT_RESULT = 'icon_set/work/primitive-make-ray/b3b9d031-1b14-49cd-b640-12d78e2f90f7/20260922T221723-c23937/result.json'

class Drawing(Solo48):
    icon_id = 'burrito'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('burrito', 'food', 'wrap')

    def build(self):
        # Symbol plan (CIRCLE, radius 20 reached only at the tips (4,24) and
        # (44,24)): a slim 40x20 pill, top y14 and bottom y34, r10 end caps
        # centred (14,24) and (34,24). The wrapped end is the full left circle:
        # the seam arc bulges right to (24,24). The fold is the diameter from
        # (8,32) to (20,16) (6-8-10 points on the circle), through (14,24).
        R = 10
        arc = lambda n, a, b: self.add_arc(n, a, b, radius_x=R, radius_y=R, sweep=True)
        self.add_line('top', (14, 14), (34, 14))
        arc('right', (34, 14), (34, 34))
        self.add_line('bottom', (34, 34), (14, 34))
        arc('left-lower', (14, 34), (8, 32))
        arc('left-mid', (8, 32), (4, 24))
        arc('left-upper', (4, 24), (14, 14))
        self.add_contour('outline', 'top', 'right', 'bottom', 'left-lower', 'left-mid', 'left-upper', closed=True)
        self.add_arc('seam-upper', (14, 14), (20, 16), radius_x=R, radius_y=R, sweep=True)
        self.add_arc('seam-mid', (20, 16), (24, 24), radius_x=R, radius_y=R, sweep=True)
        self.add_arc('seam-lower', (24, 24), (14, 34), radius_x=R, radius_y=R, sweep=True)
        self.add_contour('seam', 'seam-upper', 'seam-mid', 'seam-lower')
        self.add_line('fold', (8, 32), (20, 16))
        self.relate('connect', 'seam', 'outline')
        self.relate('connect', 'fold', 'outline')
        self.relate('connect', 'fold', 'seam')
