"""Front camera with left raised viewfinder and right lens. Wide envelope; Lucide rounded camera. Secondary ring and side slot removed; the separate left viewfinder remains in silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c55c909-3271-5e46-afc3-1df1e5139a05'
SOURCE_PATH = 'pictographic-primitives/photography/camera retro_6c55c909-3271-5e46-afc3-1df1e5139a05.svg'
AUTHOR = 'gpt-6'

class CameraWithSideViewfinder(Solo48):
    icon_id = 'camera-with-side-viewfinder'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('camera', 'retro', 'viewfinder', 'photo', 'photography', 'lens', 'vintage', 'snapshot')

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

        body('camera',4,16,44,40,[(8,16),(8,8),(16,8),(16,16),(20,16),(24,8),(32,8),(36,16),(40,16)])
        circle('lens',28,27,4)
