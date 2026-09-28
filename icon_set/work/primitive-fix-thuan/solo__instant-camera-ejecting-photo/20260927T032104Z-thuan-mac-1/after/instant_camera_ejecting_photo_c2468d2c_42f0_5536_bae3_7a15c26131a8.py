"""Instant camera with a print emerging beneath its lens. Vertical envelope accommodates the paper. Lucide camera corners; raised top block restored; square viewfinder omitted to retain lens and emerging sheet."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c2468d2c-42f0-5536-bae3-7a15c26131a8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__instant-camera-ejecting-photo/20260927T032104Z-thuan-mac-1/reference/camera polaroid_c2468d2c-42f0-5536-bae3-7a15c26131a8.svg'
AUTHOR = "gpt-6"

class InstantCameraEjectingPhoto(Solo48):
    icon_id = 'instant-camera-ejecting-photo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    categories = ("photography", "primitives")
    aliases = ()
    keywords = ('instant camera', 'polaroid', 'print', 'photo', 'camera', 'retro', 'snapshot', 'picture')

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

        body('camera',8,12,40,36,bottom=[(36,36),(32,36),(16,36),(12,36)])
        poly('top-block',(15,12),(15,4),(33,4),(33,12));connect('top-block','camera')
        circle('lens',21,24,3)
        poly('print',(16,36),(14,44),(34,44),(32,36));connect('print','camera')
