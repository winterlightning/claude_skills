"""Camera on a short neck and three splayed tripod legs. Vertical envelope reserves support height; Lucide camera corners. Top hump omitted so lens and mount remain clear; symmetric legs share a joint."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54ea6b6a-9a44-52db-a388-ae80f56aa5ac'
SOURCE_PATH = 'pictographic-primitives/photography/camera tripod_54ea6b6a-9a44-52db-a388-ae80f56aa5ac.svg'
AUTHOR = 'gpt-6'

class CameraOnTripod(Solo48):
    icon_id = 'camera-on-tripod'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    categories = ("photography", "primitives")
    aliases = ()
    keywords = ('camera', 'tripod', 'stand', 'photo', 'photography', 'studio', 'mount', 'lens')

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

        body('camera',8,4,40,28,bottom=[(36,28),(24,28),(12,28)])
        circle('lens',24,16,3)
        line('neck',(24,28),(24,34));connect('neck','camera')
        for i,x in enumerate((8,24,40)):
            line('leg-'+str(i),(24,34),(x,44));connect('neck','leg-'+str(i))
        for a,b in ((0,1),(1,2),(0,2)):connect('leg-'+str(a),'leg-'+str(b))
