"""Moving window with trailing edge. HRECT_L preserves a wide window; one broad echo replaces two crowded trails. Lucide smartphone-style rounded corners, inspected earlier in this task."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a027a723-6775-453a-b9a9-bbf4820ea975'
SOURCE_PATH = 'pictographic-primitives/technology/lazy moving animation_a027a723-6775-453a-b9a9-bbf4820ea975.svg'
AUTHOR = 'gpt-6'

class WindowWithMotionTrails(Solo48):
    icon_id = 'window-with-motion-trails'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('animation', 'motion', 'window', 'movement', 'trail', 'interface', 'transition')

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
        box('window',4,14,32,34,4)
        arc('trail-top',(38,8),(42,14),6)
        line('trail-side',(42,14),(42,34))
        arc('trail-bottom',(42,34),(38,40),6)
        contour('motion-trail','trail-top','trail-side','trail-bottom')
