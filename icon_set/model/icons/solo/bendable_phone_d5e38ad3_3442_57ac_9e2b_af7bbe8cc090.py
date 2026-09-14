"""Flexible phone: bowed body, lower slot. Lucide smartphone reduction; asymmetry conveys flex instead of a rigid rectangle."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd5e38ad3-3442-57ac-9e2b-af7bbe8cc090'
SOURCE_PATH = 'pictographic-primitives/technology/bendable phone_d5e38ad3-3442-57ac-9e2b-af7bbe8cc090.svg'
AUTHOR = 'gpt-6'

class BendablePhone(Solo48):
    icon_id = 'bendable-phone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('phone', 'bendable', 'flexible', 'smartphone', 'mobile', 'device', 'foldable')

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
        line('top',(22,6),(36,6))
        arc('tr',(36,6),(40,8),4)
        arc('bend-right',(40,8),(32,40),68,sweep=False)
        arc('br',(32,40),(28,42),4)
        line('bottom',(28,42),(12,42))
        arc('bl',(12,42),(8,40),4)
        arc('bend-left',(8,40),(18,8),60)
        arc('tl',(18,8),(22,6),4)
        contour('body','top','tr','bend-right','br','bottom','bl','bend-left','tl',closed=True)
        line('slot',(18,34),(23,34))
