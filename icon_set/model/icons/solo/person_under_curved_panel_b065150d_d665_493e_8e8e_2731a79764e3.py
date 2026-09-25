"""Person reaching beneath a curved immersive panel. Square scene; broad tangent arcs for panel and arms; head reduced to the existing small-circle form."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b065150d-d665-493e-8e8e-2731a79764e3'
SOURCE_PATH = 'pictographic-primitives/technology/immersive reality monitor_b065150d-d665-493e-8e8e-2731a79764e3.svg'
AUTHOR = 'gpt-6'

class PersonUnderCurvedPanel(Solo48):
    icon_id = 'person-under-curved-panel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('immersive', 'person', 'panel', 'screen', 'spatial', 'virtual-reality', 'monitor')

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
        arc('top-left',(6,10),(24,6),18,4);arc('top-right',(24,6),(42,10),18,4)
        line('right',(42,10),(42,20))
        arc('bottom-right',(42,20),(24,16),18,4,sweep=False);arc('bottom-left',(24,16),(6,20),18,4,sweep=False)
        line('left',(6,20),(6,10));contour('panel','top-left','top-right','right','bottom-right','bottom-left','left',closed=True)
        circle('head',24,29,2)
        arc('arm-left',(8,30),(24,42),16,12,sweep=False);arc('arm-right',(24,42),(40,30),16,12,sweep=False);contour('arms','arm-left','arm-right')
