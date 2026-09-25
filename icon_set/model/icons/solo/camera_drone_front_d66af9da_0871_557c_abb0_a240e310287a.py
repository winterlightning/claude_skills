"""Camera drone with suspended lens and paired landing feet. Wide envelope; Lucide drone symmetry and minimal body; lens reflection omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd66af9da-0871-557c-abb0-a240e310287a'
SOURCE_PATH = 'pictographic-primitives/technology/drone camera_d66af9da-0871-557c-abb0-a240e310287a.svg'
AUTHOR = 'gpt-6'

class CameraDroneFront(Solo48):
    icon_id = 'camera-drone-front'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('drone', 'camera', 'quadcopter', 'aerial', 'photography', 'gimbal', 'uav')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x,y-r),(x,y+r),r)
            arc(n+'b',(x,y+r),(x,y-r),r)
            contour(n,n+'a',n+'b',closed=True)
        def box(n,l,t,r,b,rad=4):
            line(n+'t',(l+rad,t),(r-rad,t)); arc(n+'tr',(r-rad,t),(r,t+rad),rad)
            line(n+'r',(r,t+rad),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            line(n+'l',(l,b-rad),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)
        for x in (10,38):
            poly(f'rotor-{x}',(x-6,8),(x,8),(x+6,8))
            line(f'mast-{x}',(x,8),(x,18));connect(f'rotor-{x}',f'mast-{x}')
        poly('body',(6,18),(10,18),(18,18),(24,20),(30,18),(38,18),(42,18))
        connect('body','mast-10');connect('body','mast-38')
        circle('camera',24,34,6)
        line('gimbal',(24,20),(24,28));connect('gimbal','body');connect('gimbal','camera')
        poly('foot-left',(12,18),(8,36),(6,36));connect('foot-left','body')
        poly('foot-right',(36,18),(40,36),(42,36));connect('foot-right','body')
