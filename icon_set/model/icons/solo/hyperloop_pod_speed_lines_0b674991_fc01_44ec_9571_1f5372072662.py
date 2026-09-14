"""Streamlined right-facing pod with curved windshield. Radial envelope permits a naturally long silhouette; Lucide train-front coherent vehicle shell. Three trailing motion lines retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0b674991-fc01-44ec-9571-1f5372072662'
SOURCE_PATH = 'pictographic-primitives/technology/hyperloop speed_0b674991-fc01-44ec-9571-1f5372072662.svg'
AUTHOR = 'gpt-6'

class HyperloopPodSpeedLines(Solo48):
    icon_id = 'hyperloop-pod-speed-lines'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('hyperloop', 'pod', 'speed', 'train', 'transport', 'fast', 'capsule')

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
        line('roof',(20,14),(24,14))
        arc('nose-top',(24,14),(42,24),20,10)
        arc('nose-bottom',(42,24),(24,34),20,10)
        line('bottom',(24,34),(20,34))
        arc('rear-bottom',(20,34),(16,30),4)
        line('rear',(16,30),(16,18));arc('rear-top',(16,18),(20,14),4)
        contour('pod','roof','nose-top','nose-bottom','bottom','rear-bottom','rear','rear-top',closed=True)
        line('speed-top',(8,14),(20,14));connect('speed-top','pod')
        line('speed-mid',(6,24),(7,24))
        line('speed-bottom',(8,34),(20,34));connect('speed-bottom','pod')
        arc('window-curve',(24,14),(32,24),8,10,sweep=False)
        line('window-bottom',(32,24),(42,24));contour('window','window-curve','window-bottom');connect('window','pod')
