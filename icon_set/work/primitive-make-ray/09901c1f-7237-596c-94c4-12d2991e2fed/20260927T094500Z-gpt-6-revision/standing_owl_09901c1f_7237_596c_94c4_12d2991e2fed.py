"""Make both owl ear tufts truly triangular and mirrored; round the lower face symmetrically and center the eyes and beak. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '09901c1f-7237-596c-94c4-12d2991e2fed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-owl/20260927T093533Z-thuan-mac-1/reference/wild bird owl body_09901c1f-7237-596c-94c4-12d2991e2fed.svg'
AUTHOR = "gpt-6"

class StandingOwl(Solo48):
    icon_id = 'standing-owl'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('owl', 'standing', 'wise', 'bird', 'night', 'feathers', 'nocturnal', 'perch')

    def build(self):
        """Tall owl body, ear tufts and face from the original bird silhouette.

        Lucide bird informed the long flank and Lucide cat the paired ear tips.
        The wide cat-like face of the rejected drawing is replaced by a full body.
        """
        self.add_bezier('left-flank', (10,44), ((11,30),(15,20),(17,15)))
        self.add_line('left-neck', (17,15), (17,9))
        self.add_line('left-ear', (17,9), (14,4))
        self.add_line('crown-left', (14,4), (24,10))
        self.add_line('crown-right', (24,10), (34,4))
        self.add_line('right-ear', (34,4), (31,15))
        self.add_bezier('right-shoulder', (31,15), ((36,19),(38,24),(38,28)))
        self.add_bezier('right-flank', (38,28), ((38,34),(35,39),(30,41)))
        self.add_bezier('base', (30,41), ((23,44),(16,44),(10,44)))
        self.add_contour('owl-body','left-flank','left-neck','left-ear','crown-left',
                         'crown-right','right-ear','right-shoulder','right-flank','base',closed=True)
        self.add_dot('eye',(24,22))
        self.add_bezier('wing',(29,29),((29,33),(25,35),(20,35)))
