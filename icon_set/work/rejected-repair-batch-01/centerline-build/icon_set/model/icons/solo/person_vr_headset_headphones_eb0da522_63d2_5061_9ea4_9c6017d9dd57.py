"""Person wearing a VR visor and headphones. Square extremes 6/6/42/42. Lucide headphones and person construction inspected earlier inform the arch, ear pieces and shoulders. Collar, inner headband and nose dip omitted to retain clear main equipment."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eb0da522-63d2-5061-9ea4-9c6017d9dd57'
SOURCE_PATH = 'pictographic-primitives/technology/vr user headphones_eb0da522-63d2-5061-9ea4-9c6017d9dd57.svg'
AUTHOR = 'gpt-6'

class PersonVrHeadsetHeadphones(Solo48):
    icon_id = 'person-vr-headset-headphones'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('vr', 'headset', 'headphones', 'person', 'user', 'audio', 'virtual-reality')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def chain(n,*p):
            for i,(a,b) in enumerate(zip(p,p[1:]),1): line(f'{n}-{i}',a,b)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x,y-r),(x+r,y),r)
            arc(n+'b',(x+r,y),(x,y+r),r)
            arc(n+'c',(x,y+r),(x-r,y),r)
            arc(n+'d',(x-r,y),(x,y-r),r)
            contour(n,n+'a',n+'b',n+'c',n+'d',closed=True)
        def box(n,l,t,r,b,rad=4):
            line(n+'t',(l+rad,t),(r-rad,t)); arc(n+'tr',(r-rad,t),(r,t+rad),rad)
            chain(n+'r',(r,t+rad),(r,(t+b)//2),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            chain(n+'l',(l,b-rad),(l,(t+b)//2),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r-1','r-2','br','b','bl','l-1','l-2','tl')],closed=True)
        box('visor',10,18,38,28,4)
        arc('band',(14,18),(34,18),10,12);connect('band','visor')
        poly('left-ear',(10,23),(6,26));poly('right-ear',(38,23),(42,26));connect('left-ear','visor');connect('right-ear','visor')
        arc('face-left',(14,28),(24,36),10,8,sweep=False);arc('face-right',(24,36),(34,28),10,8,sweep=False)
        contour('face','face-left','face-right');connect('face','visor')
        arc('shoulder-left',(6,42),(24,36),18,6);arc('shoulder-right',(24,36),(42,42),18,6)
        contour('shoulders','shoulder-left','shoulder-right');connect('shoulders','face')
