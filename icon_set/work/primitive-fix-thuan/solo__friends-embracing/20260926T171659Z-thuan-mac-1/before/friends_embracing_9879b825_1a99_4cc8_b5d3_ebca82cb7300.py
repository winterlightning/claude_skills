"""Two friends embrace with an upper arm and a forearm crossing the bodies. Lucide users informs paired heads and body arches. Fingers and doubled forearm outlines are reduced to clear strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9879b825-1a99-4cc8-b5d3-ebca82cb7300'
SOURCE_PATH = 'pictographic-primitives/users/user friends_9879b825-1a99-4cc8-b5d3-ebca82cb7300.svg'
AUTHOR = 'gpt-6'


class FriendsEmbracing(Solo48):
    icon_id = 'friends-embracing'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    categories = ("users", "primitives")
    aliases = ()
    keywords = ('friends', 'embrace', 'hug', 'people', 'two', 'together', 'support', 'users')

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
        # Portrait centerline extremes (8,6)-(40,42); genuine shoulder and body contacts.
        for name,cx in (('left',13),('right',35)):
            self.circle(name+'-head',cx,9,5)
            self.standing_bust(name,cx)
        self.add_line('upper-arm',(13,24),(35,24))
        self.add_polyline('embracing-arm',(13,34),(18,34),(30,34),(35,34))
        for body in ('left','right'):
            self.relate('connect',body,'upper-arm')
            self.relate('connect',body,'embracing-arm')
