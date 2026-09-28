"""An upright hand raises its index finger while the other fingers curl beside it and the thumb angles outward. A broad open arc surrounds the fingertip, marking the point of contact."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd164057e-27d7-4db0-bfd1-12a976e09a11'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__finger-tap-gesture/20260927T075452Z-thuan-mac-1/reference/finger tap 1_d164057e-27d7-4db0-bfd1-12a976e09a11.svg'
AUTHOR = "gpt-6"

class MobileIcon(Solo48):
    icon_id = 'finger-tap-gesture'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    categories = ('mobile', 'primitives')
    aliases = ()
    keywords = ('finger', 'tap', 'hand', 'touch', 'gesture', 'press', 'interaction')

    def build(self):
        # Lucide construction references: pointer, hand.
        # Typed paths own continuous joins; repeated shapes share dimensions.
        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                ident = f"{name}-{i}"
                if kind == 'L':
                    self.add_line(ident, here, end)
                elif kind == 'C':
                    self.add_bezier(ident, here, (args[0],args[1],end))
                else:
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def rounded(name,x0,y0,x1,y1,r,split_y=None):
            right = [('L',(x1,split_y))] if split_y is not None else []
            left = [('L',(x0,split_y))] if split_y is not None else []
            path(name,(x0+r,y0),[
                ('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),
                *right,('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),
                ('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),
                *left,('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        # SQUARE extremes (6,6)-(42,42). One hand contour, separate contact halo.
        # Human reference: icon_set/references/human_ref/full_body_ref.png (continuous rounded limbs).
        # No head or body is depicted, so a head-to-body gap is not applicable.
        path('contact',(6,16),[('A',(24,6),18,10,True),('A',(42,16),18,10,True)])
        path('hand',(14,26),[('L',(14,22)),('A',(18,18),4,4,True),('A',(22,22),4,4,True),('L',(22,26)),('L',(30,26)),('A',(38,34),8,8,True),('A',(30,42),8,8,True),('L',(22,42)),('C',(10,34),(16,42),(16,34)),('A',(10,26),4,4,True),('L',(14,26))],True)
