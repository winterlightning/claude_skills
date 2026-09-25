"""Physical body-scanning scene. Lucide person-standing simplified limbs; paired posts and short sensor marks, open base around feet."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7098a290-16a5-50dd-95e1-1f75ae0db128'
SOURCE_PATH = 'pictographic-primitives/technology/body scanner_7098a290-16a5-50dd-95e1-1f75ae0db128.svg'
AUTHOR = 'gpt-6'

class BodyScannerGate(Solo48):
    icon_id = 'body-scanner-gate'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('body-scanner', 'scanner', 'security', 'person', 'gate', 'airport', 'detector', 'screening')

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
        poly('gate-left',(6,6),(6,26),(6,42),(10,42))
        poly('gate-right',(42,6),(42,26),(42,42),(38,42))
        circle('head',24,15,3)
        poly('shoulders',(16,32),(16,28),(24,28),(32,28),(32,32))
        poly('body',(24,28),(24,34),(19,42))
        line('leg-right',(24,34),(29,42))
        connect('body','shoulders'); connect('body','leg-right')
        line('sensor-left',(6,26),(8,26));connect('sensor-left','gate-left')
        line('sensor-right',(42,26),(40,26));connect('sensor-right','gate-right')
