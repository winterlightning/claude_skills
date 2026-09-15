"""Round humidifier with collar, water line, and curled mist. Portrait envelope; no exact Lucide match; mirrored vessel with an asymmetric vapor curl."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fdf1153b-ad8f-51e3-bcb3-9039939523a9'
SOURCE_PATH = 'pictographic-primitives/technology/humidifier_fdf1153b-ad8f-51e3-bcb3-9039939523a9.svg'
AUTHOR = 'gpt-6'

class HumidifierBottle(Solo48):
    icon_id = 'humidifier-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('humidifier', 'mist', 'water', 'vessel', 'air', 'appliance', 'moisture')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def chain(n,*p):
            for i,(a,b) in enumerate(zip(p,p[1:]),1): line(f'{n}-{i}',a,b)
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
        chain('neck',(18,17),(30,17),(32,23))
        arc('shoulder-right',(32,23),(40,34),14)
        arc('lower-right',(40,34),(30,42),10)
        line('bottom',(30,42),(18,42))
        arc('lower-left',(18,42),(8,34),10)
        arc('shoulder-left',(8,34),(16,23),14)
        line('neck-left',(16,23),(18,17))
        contour('vessel','neck-1','neck-2','shoulder-right','lower-right','bottom','lower-left','shoulder-left','neck-left',closed=True)
        arc('water-left',(8,34),(24,34),18,sweep=True)
        arc('water-right',(24,34),(40,34),18,sweep=False)
        contour('water','water-left','water-right');connect('water','vessel')
        arc('mist',(24,6),(20,8),4,sweep=False)
