"""Hand Touching Multiple Devices. Authored from the supplied visual brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da217745-f501-41f3-adeb-cb1f2534c16d'
SOURCE_PATH = 'pictographic-primitives/websites/responsive design hand_da217745-f501-41f3-adeb-cb1f2534c16d.svg'
AUTHOR = 'gpt-6'

class HandTouchingMultipleDevices(Solo48):
    icon_id = 'hand-touching-multiple-devices'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/technology"
    aliases = ()
    keywords = ('responsive', 'devices', 'hand', 'touch', 'phone', 'browser', 'screen')

    def build(self):
        self.box('phone',32,6,42,20,r=2)
        self.add_polyline('browser',(21,6),(9,6),(6,9),(6,30))
        self.add_line('toolbar',(6,15),(21,15))
        self.relate('connect','toolbar','browser')
        self.add_line('screen',(16,24),(16,42))
        self.add_arc('fingertip',(30,33),(38,33),radius_x=4)
        self.add_line('palm-1',(38,33),(38,37))
        self.add_line('palm-2',(38,37),(42,39))
        self.add_line('palm-3',(42,39),(41,42))
        self.add_contour('finger','fingertip','palm-1','palm-2','palm-3')
        self.add_polyline('thumb',(30,33),(24,29),(24,40),(29,42))
        self.relate('connect','thumb','finger')

    def box(self, name, x0, y0, x1, y1, r=3):
        # One rounded rectangle definition; all corners share a radius.
        points = [(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),
                  (x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        members=[]
        for i,p in enumerate(points):
            q=points[(i+1)%8]; part=f'{name}-{i}';members.append(part)
            if i%2: self.add_arc(part,p,q,radius_x=r)
            else: self.add_line(part,p,q)
        self.add_contour(name,*members,closed=True)
