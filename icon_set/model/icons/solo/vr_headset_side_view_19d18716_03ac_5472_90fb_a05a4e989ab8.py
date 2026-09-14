"""Side VR headset with arched head strap and sweeping rear strap. Horizontal envelope; Lucide headset strap construction; deliberate right-facing asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '19d18716-03ac-5472-90fb-a05a4e989ab8'
SOURCE_PATH = 'pictographic-primitives/technology/meta quest_19d18716-03ac-5472-90fb-a05a4e989ab8.svg'
AUTHOR = 'gpt-6'

class VrHeadsetSideView(Solo48):
    icon_id = 'vr-headset-side-view'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('vr', 'headset', 'quest', 'virtual-reality', 'goggles', 'device', 'side')

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
        box('visor',24,20,44,40,6)
        arc('head-strap',(8,26),(24,26),8,18);connect('head-strap','visor')
        poly('rear-strap',(24,26),(8,26),(4,32),(4,40),(10,34),(24,34));connect('rear-strap','visor');connect('rear-strap','head-strap')
