"""Wide visor with central nose indentation and right strap. Consistent circular corners informed by Lucide smartphone; intentional right-side connector."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dfd86ad0-9936-5051-a60d-200aa0c585ad'
SOURCE_PATH = 'pictographic-primitives/technology/apple vision pro_dfd86ad0-9936-5051-a60d-200aa0c585ad.svg'
AUTHOR = 'gpt-6'

class MixedRealityHeadset(Solo48):
    icon_id = 'mixed-reality-headset'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('headset', 'mixed-reality', 'vision-pro', 'visor', 'spatial', 'vr', 'ar', 'goggles')

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
        line('top',(14,8),(30,8))
        arc('tr',(30,8),(40,18),10)
        line('right',(40,18),(40,30))
        arc('br',(40,30),(30,40),10)
        arc('nose-r',(30,40),(22,36),10)
        arc('nose-l',(22,36),(14,40),10)
        arc('bl',(14,40),(6,30),10)
        line('left',(6,30),(6,18))
        arc('tl',(6,18),(14,8),10)
        contour('visor','top','tr','right','br','nose-r','nose-l','bl','left','tl',closed=True)
        line('strap',(40,23),(42,23))
        connect('strap','visor')
