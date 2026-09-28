"""Remove the pinched inner leaf triangles and leave a generous open suspension above the bowl. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '648d5f22-ccb1-4224-9894-c373442f1825'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__trailing-hanging-planter/20260927T101610Z-thuan-mac-1/reference/hanging plant 3_648d5f22-ccb1-4224-9894-c373442f1825.svg'
AUTHOR = "gpt-6"

class TrailingHangingPlanter(Solo48):
    icon_id = 'trailing-hanging-planter'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('planter', 'hanging', 'trailing', 'vine', 'leaves', 'cord', 'plant')

    def build(self) -> None:
        """One hanging cord, three rising leaves, a broad pot and trailing side vines."""
        self.add_line('center-stem',(24,4),(24,30))
        self.add_bezier('left-leaf',(16,30),((15,23),(12,19),(10,16)))
        self.add_bezier('right-leaf',(32,30),((33,23),(36,19),(38,16)))
        self.add_line('rim-left',(8,30),(16,30))
        self.add_line('rim-center',(16,30),(32,30))
        self.add_line('rim-right',(32,30),(40,30))
        self.add_arc('bowl',(32,30),(16,30),radius_x=8,radius_y=10,sweep=True)
        self.add_contour('pot','rim-center','bowl',closed=True)
        self.add_line('left-trail',(8,30),(8,44))
        self.add_line('right-trail',(40,30),(40,44))
        for a,b in [('center-stem','pot'),('left-leaf','pot'),('right-leaf','pot'),('rim-left','pot'),('rim-right','pot'),('left-trail','rim-left'),('right-trail','rim-right')]:
            self.relate('connect',a,b)
