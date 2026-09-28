"""Two overlapping neutral busts, front left and rear right. Lucide users-round informs the partial rear contour; ear steps are omitted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1ac52edd-1aed-4baa-841f-a59d11ca62a6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-person-busts/20260927T101610Z-thuan-mac-1/reference/multiple neutral_1ac52edd-1aed-4baa-841f-a59d11ca62a6.svg'
AUTHOR = "gpt-6"


class TwoPersonBusts(Solo48):
    icon_id = 'two-person-busts'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    categories = ("users", "primitives")
    aliases = ()
    keywords = ('people', 'users', 'busts', 'two', 'group', 'team', 'contacts', 'accounts')

    def circle(self, name, cx, cy, radius):
        top, bottom = (cx, cy-radius), (cx, cy+radius)
        self.add_arc(name+'-a',top,bottom,radius_x=radius)
        self.add_arc(name+'-b',bottom,top,radius_x=radius)
        self.add_contour(name,name+'-a',name+'-b',closed=True)


    def front_bust(self, woman=False, fringe=None):
        """Continuous head, neck and shoulders from the original outline."""
        self.add_bezier('front-crown-right',(16,6),((22,6),(27,12),(24,17)))
        self.add_bezier('front-neck-right',(24,17),((24,22),(21,25),(22,27)))
        self.add_bezier('front-shoulder-right',(22,27),((27,29),(27,35),(27,42)))
        self.add_line('front-base',(27,42),(6,42))
        self.add_bezier('front-shoulder-left',(6,42),((6,35),(8,29),(12,27)))
        self.add_bezier('front-crown-left',(12,27),((7,20),(7,8),(16,6)))
        self.add_contour('front','front-crown-right','front-neck-right','front-shoulder-right',
                         'front-base','front-shoulder-left','front-crown-left',closed=True)

    def rear_bust(self, woman=False):
        self.add_arc('rear-crown',(32,6),(40,14),radius_x=8)
        self.add_arc('rear-jaw',(40,14),(36,22),radius_x=8)
        self.add_line('rear-neck',(36,22),(36,28))
        self.add_arc('rear-shoulder',(36,28),(42,34),radius_x=6)
        self.add_line('rear-side',(42,34),(42,42))
        self.add_line('rear-base',(42,42),(36,42))
        self.add_contour('rear','rear-crown','rear-jaw','rear-neck','rear-shoulder','rear-side','rear-base')
        if woman:
            self.add_line('rear-hair',(40,14),(42,25))
            self.relate('connect','rear','rear-hair')

    def build(self) -> None:
        # Square centerline extremes (6,6)-(42,42); rear person is occluded.
        self.front_bust()
        self.rear_bust()
