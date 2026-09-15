"""A man stands in front of a woman with a trailing hair contour. Lucide users-round informs front/rear hierarchy; ear nubs and tiny fringe details are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a6b2b48-3cc2-4682-9213-0c7d99acf693'
SOURCE_PATH = 'pictographic-primitives/users/multiple man woman 3_6a6b2b48-3cc2-4682-9213-0c7d99acf693.svg'
AUTHOR = 'gpt-6'


class ManAndWomanBusts(Solo48):
    icon_id = 'man-and-woman-busts'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/groups"
    aliases = ()
    keywords = ('man', 'woman', 'couple', 'busts', 'users', 'people', 'pair', 'profile')

    def circle(self, name, cx, cy, radius):
        top, bottom = (cx, cy-radius), (cx, cy+radius)
        self.add_arc(name+'-a',top,bottom,radius_x=radius)
        self.add_arc(name+'-b',bottom,top,radius_x=radius)
        self.add_contour(name,name+'-a',name+'-b',closed=True)


    def front_bust(self, woman=False, fringe=None):
        cx,cy,radius = (16,16,10) if woman else (16,14,8)
        self.circle('front-head',cx,cy,radius)
        if woman:
            for side,direction in (('left',-1),('right',1)):
                x=cx+direction*radius
                self.add_line('hair-'+side,(x,cy),(x,28))
                self.relate('connect','front-head','hair-'+side)
            if fringe=='pointed':
                self.add_polyline('fringe',(6,16),(16,13),(26,16))
            else:
                self.add_arc('fringe',(6,16),(26,16),radius_x=26)
            self.relate('connect','front-head','fringe')
        ry=7 if woman else 9
        self.add_arc('front-shoulders',(6,42),(26,42),radius_x=10,radius_y=ry)
        self.add_line('front-base',(26,42),(6,42))
        self.add_contour('front-body','front-shoulders','front-base',closed=True)

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
        # Square centerline extremes (6,6)-(42,42).
        self.front_bust()
        self.rear_bust(woman=True)
