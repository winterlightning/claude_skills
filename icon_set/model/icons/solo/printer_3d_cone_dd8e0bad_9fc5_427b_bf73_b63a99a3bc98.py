"""Square print chamber; integral nozzle and printed object. Lucide printer rounded frame; rails and tiny highlight omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dd8e0bad-9fc5-427b-bf73-b63a99a3bc98'
SOURCE_PATH = 'pictographic-primitives/technology/3 d print triangle_dd8e0bad-9fc5-427b-bf73-b63a99a3bc98.svg'
AUTHOR = 'gpt-6'

class Printer3DCone(Solo48):
    icon_id = 'printer-3d-cone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('3d-printing', 'printer', 'cone', 'nozzle', 'fabrication', 'maker', 'model')

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
        box('frame',6,6,42,42)
        poly('feed',(16,6),(16,16),(21,21),(26,16))
        connect('feed','frame')
        poly('print',(22,42),(22,36),(30,26),(38,36),(38,42))
        connect('print','frame')
