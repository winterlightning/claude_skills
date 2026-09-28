"""Camera with a square carrying handle and central lens. Square envelope makes the handle opening readable; Lucide camera rounded corners. Lens reduced while retaining a complete circle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8b17656-f666-5e6c-a3ff-976538f73f05'
SOURCE_PATH = 'pictographic-primitives/photography/camera display_c8b17656-f666-5e6c-a3ff-976538f73f05.svg'
AUTHOR = 'gpt-6'

class CameraWithTopHandle(Solo48):
    icon_id = 'camera-with-top-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    categories = ("photography", "primitives")
    aliases = ()
    keywords = ('camera', 'handle', 'photo', 'photography', 'lens', 'picture', 'snapshot', 'display')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,sweep=True): self.add_arc(n,a,b,radius_x=r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'-upper',(x-r,y),(x+r,y),r)
            arc(n+'-lower',(x+r,y),(x-r,y),r)
            contour(n,n+'-upper',n+'-lower',closed=True)
        def body(n,l,t,r,b,top=None,bottom=None):
            rad=4
            points=top or [(l+rad,t),(r-rad,t)]
            ids=[]
            for i,(a,z) in enumerate(zip(points,points[1:])):
                name=n+'-top-'+str(i);line(name,a,z);ids.append(name)
            arc(n+'-tr',points[-1],(r,t+rad),rad)
            line(n+'-right',(r,t+rad),(r,b-rad))
            arc(n+'-br',(r,b-rad),(r-rad,b),rad)
            bp=bottom or [(r-rad,b),(l+rad,b)]
            bids=[]
            for i,(a,z) in enumerate(zip(bp,bp[1:])):
                name=n+'-bottom-'+str(i);line(name,a,z);bids.append(name)
            arc(n+'-bl',(l+rad,b),(l,b-rad),rad)
            line(n+'-left',(l,b-rad),(l,t+rad))
            arc(n+'-tl',(l,t+rad),points[0],rad)
            contour(n,*ids,n+'-tr',n+'-right',n+'-br',*bids,n+'-bl',n+'-left',n+'-tl',closed=True)

        body('camera',6,16,42,42,[(10,16),(16,16),(32,16),(38,16)])
        poly('handle',(16,16),(16,6),(32,6),(32,16));connect('handle','camera')
        circle('lens',24,29,4)
