"""Hand Touching Multiple Devices. Authored from the supplied visual brief."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'da217745-f501-41f3-adeb-cb1f2534c16d'
SOURCE_PATH = 'pictographic-primitives/websites/responsive design hand_da217745-f501-41f3-adeb-cb1f2534c16d.svg'
AUTHOR = 'gpt-6'

class HandTouchingMultipleDevices(Solo48):
    icon_id = 'hand-touching-multiple-devices'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    categories = ('websites', 'primitives')
    aliases = ()
    keywords = ('responsive', 'devices', 'hand', 'touch', 'phone', 'browser', 'screen')

    def build(self) -> None:
        self.box('landscape-screen',6,6,24,18,r=2)
        self.box('phone',33,6,42,20,r=2,joins=((34,20),))
        self.add_line('finger-left',(30,33),(30,24))
        self.add_arc('finger-left-round',(30,24),(34,20),radius_x=4)
        self.add_arc('finger-right-round',(34,20),(38,24),radius_x=4)
        self.add_polyline('palm',(38,24),(38,31),(42,34),(40,42))
        self.add_contour('index','finger-left','finger-left-round','finger-right-round')
        self.relate('connect','index','phone')
        self.relate('connect','index','palm')
        self.add_polyline('thumb',(30,33),(21,27),(21,37),(26,42))
        self.relate('connect','thumb','index')

    def box(self, name, x0, y0, x1, y1, r=2, joins=()):
        # A shared corner radius and explicit attachment nodes own this rectangle.
        points=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),
                (x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        members=[]
        for i,p in enumerate(points):
            q=points[(i+1)%8]
            if i%2:
                name_i=f'{name}-{i}';self.add_arc(name_i,p,q,radius_x=r);members.append(name_i)
            else:
                mid=[v for v in joins if v!=p and v!=q and
                     ((p[0]==q[0]==v[0] and min(p[1],q[1])<v[1]<max(p[1],q[1])) or
                      (p[1]==q[1]==v[1] and min(p[0],q[0])<v[0]<max(p[0],q[0])))]
                run=[p]+sorted(mid,key=lambda v:(v[0]-p[0])**2+(v[1]-p[1])**2)+[q]
                for j,(a,b) in enumerate(zip(run,run[1:])):
                    name_i=f'{name}-{i}-{j}';self.add_line(name_i,a,b);members.append(name_i)
        self.add_contour(name,*members,closed=True)
