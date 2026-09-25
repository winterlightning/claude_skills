"""Two friends stand together with an arm resting across the shoulders. Lucide users and user-round inform paired heads and arched bodies. The small hand is reduced to a rounded contact."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc3c63fc-721e-43dd-a5cf-cb7496abf926'
SOURCE_PATH = 'pictographic-primitives/users/user friends 2_fc3c63fc-721e-43dd-a5cf-cb7496abf926.svg'
AUTHOR = 'gpt-6'


class FriendsArmOnShoulder(Solo48):
    icon_id = 'friends-arm-on-shoulder'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    aliases = ()
    keywords = ('friends', 'people', 'two', 'shoulder', 'support', 'together', 'pair', 'users')

    def circle(self,name,cx,cy,r):
        pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(i);self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def standing_bust(self,name,cx):
        self.add_line(name+'-left-low',(cx-5,44),(cx-5,34))
        self.add_line(name+'-left-high',(cx-5,34),(cx-5,29))
        self.add_arc(name+'-cap-left',(cx-5,29),(cx,24),radius_x=5)
        self.add_arc(name+'-cap-right',(cx,24),(cx+5,29),radius_x=5)
        self.add_line(name+'-right-high',(cx+5,29),(cx+5,34))
        self.add_line(name+'-right-low',(cx+5,34),(cx+5,44))
        self.add_contour(name,*[name+s for s in ('-left-low','-left-high','-cap-left','-cap-right','-right-high','-right-low')])

    def build(self) -> None:
        # Portrait centerline extremes (8,6)-(40,42); paired figures share dimensions.
        for name,cx in (('left',13),('right',35)):
            self.circle(name+'-head',cx,9,5)
            self.standing_bust(name,cx)
        self.add_line('friendly-arm',(13,24),(35,24))
        self.relate('connect','left','friendly-arm')
        self.relate('connect','right','friendly-arm')
