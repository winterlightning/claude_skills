"""Closed Eyes and Lips.

Symbol plan: Two mirrored closed eyes sit above full lips. One lash per eye and a shallow upper-lip dip replace fine eyelashes and a crowded mouth seam.
Lucide: eye-closed; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'df7f8a18-1b03-4999-aebf-6934a21a3454'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__closed-eyes-and-lips/20260927T032242Z-thuan-mac-1/reference/dating makeup_df7f8a18-1b03-4999-aebf-6934a21a3454.svg'
AUTHOR = 'gpt-6'


class ClosedEyesAndLips(Solo48):
    icon_id = 'closed-eyes-and-lips'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('closed eyes', 'face', 'eyes', 'lips', 'expression', 'beauty', 'features', 'mouth', 'portrait')

    def build(self) -> None:
        # Paired closed lids with three lashes each and one coherent lip outline.
        for side,cx in (('left',12),('right',36)):
            a=(cx-8,8);m=(cx,12);b=(cx+8,8)
            self.add_bezier(side+'-lid-a',a,((cx-6,11),(cx-4,12),m))
            self.add_bezier(side+'-lid-b',m,((cx+4,12),(cx+6,11),b))
            self.add_contour(side+'-lid',side+'-lid-a',side+'-lid-b')
            for k,(x,dx) in enumerate(((cx-6,-2),(cx+6,2))):
                y=10
                self.add_line(f'{side}-lash-{k}',(x,y),(x+dx,y+4))
                self.relate('connect',side+'-lid',f'{side}-lash-{k}')
        self.add_bezier('lip-upper-left',(10,31),((16,25),(21,26),(24,29)))
        self.add_bezier('lip-upper-right',(24,29),((27,26),(32,25),(38,31)))
        self.add_bezier('lip-lower-right',(38,31),((34,38),(29,40),(24,40)))
        self.add_bezier('lip-lower-left',(24,40),((19,40),(14,38),(10,31)))
        self.add_contour('lips','lip-upper-left','lip-upper-right','lip-lower-right','lip-lower-left',closed=True)
