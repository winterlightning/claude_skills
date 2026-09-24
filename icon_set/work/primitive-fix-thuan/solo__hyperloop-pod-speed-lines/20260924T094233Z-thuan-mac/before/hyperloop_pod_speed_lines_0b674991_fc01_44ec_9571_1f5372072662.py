"""Streamlined right-facing pod with curved windshield. HRECT_L landscape envelope matches the horizontal vehicle and its motion trails; Lucide train-front coherent vehicle shell. Three trailing motion lines retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0b674991-fc01-44ec-9571-1f5372072662'
SOURCE_PATH = 'pictographic-primitives/technology/hyperloop speed_0b674991-fc01-44ec-9571-1f5372072662.svg'
AUTHOR = 'gpt-6'

class HyperloopPodSpeedLines(Solo48):
    icon_id = 'hyperloop-pod-speed-lines'
    keyshape = Keyshape.HRECT_L
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
        line('roof',(20,8),(24,8))
        arc('nose-top',(24,8),(44,24),20,16)
        arc('nose-bottom',(44,24),(24,40),20,16)
        line('bottom',(24,40),(20,40))
        arc('rear-bottom',(20,40),(16,36),4)
        line('rear',(16,36),(16,12));arc('rear-top',(16,12),(20,8),4)
        contour('pod','roof','nose-top','nose-bottom','bottom','rear-bottom','rear','rear-top',closed=True)
        line('speed-top',(4,8),(20,8));connect('speed-top','pod')
        line('speed-mid',(4,24),(7,24))
        line('speed-bottom',(4,40),(20,40));connect('speed-bottom','pod')
        arc('window-curve',(24,8),(32,24),8,16,sweep=False)
        line('window-bottom',(32,24),(44,24));contour('window','window-curve','window-bottom');connect('window','pod')
