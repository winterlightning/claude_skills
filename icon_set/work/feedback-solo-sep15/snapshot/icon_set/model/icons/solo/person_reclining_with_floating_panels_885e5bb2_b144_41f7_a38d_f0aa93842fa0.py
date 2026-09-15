"""Reclining user with floating panels. Square envelope; Lucide armchair seat/back relationship; two panels retain the spatial scene, omitting the tiniest third panel."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '885e5bb2-b144-41f7-a38d-f0aa93842fa0'
SOURCE_PATH = 'pictographic-primitives/technology/immersive reality chair_885e5bb2-b144-41f7-a38d-f0aa93842fa0.svg'
AUTHOR = 'gpt-6'

class PersonRecliningWithFloatingPanels(Solo48):
    icon_id = 'person-reclining-with-floating-panels'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('immersive', 'person', 'chair', 'panels', 'spatial', 'virtual-reality', 'relax')

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
        poly('panel',(6,10),(18,6),(18,19),(6,15),closed=True)
        poly('small-panel',(6,28),(16,30),(16,42),(6,40),closed=True)
        circle('head',34,14,3)
        poly('person',(34,26),(30,34),(24,34),(24,42))
        poly('chair',(42,24),(38,42),(24,42));connect('person','chair')
