"""Front VR headset with dome strap, nose bridge and lower shell. Square envelope; Lucide headset coherent strap curves with mirrored visor geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd16bbdd4-caba-5737-9a5d-49dbef78c13a'
SOURCE_PATH = 'pictographic-primitives/technology/meta quest pro_d16bbdd4-caba-5737-9a5d-49dbef78c13a.svg'
AUTHOR = 'gpt-6'

class VrHeadsetFrontView(Solo48):
    icon_id = 'vr-headset-front-view'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('vr', 'headset', 'quest', 'virtual-reality', 'goggles', 'device', 'front')

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
        line('top',(14,16),(34,16));arc('right-top',(34,16),(42,24),8);arc('right-bottom',(42,24),(34,32),8)
        chain('nose',(34,32),(30,32),(24,29),(18,32),(14,32))
        arc('left-bottom',(14,32),(6,24),8);arc('left-top',(6,24),(14,16),8)
        contour('visor','top','right-top','right-bottom','nose-1','nose-2','nose-3','nose-4','left-bottom','left-top',closed=True)
        arc('upper-strap',(14,16),(34,16),10);connect('upper-strap','visor')
        arc('lower-shell',(14,32),(34,32),10,sweep=False);connect('lower-shell','visor')
