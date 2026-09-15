"""Plump inflatable robot with oval head, short visor and rounded body. Square envelope. Shared mirror axis; continuous rounded silhouette, arm seams omitted to keep soft body clear. No exact Lucide counterpart."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca2df963-70fb-5a0e-843f-128a834a5416'
SOURCE_PATH = 'pictographic-primitives/technology/robot baymax_ca2df963-70fb-5a0e-843f-128a834a5416.svg'
AUTHOR = 'gpt-6'

class RoundInflatableRobot(Solo48):
    icon_id = 'round-inflatable-robot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('robot', 'baymax', 'companion', 'healthcare', 'character', 'friendly', 'android')

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
        arc('head-top',(12,15),(36,15),12,9)
        arc('head-bottom',(36,15),(12,15),12,9)
        contour('head','head-top','head-bottom',closed=True)
        line('visor',(22,15),(26,15))
        arc('body-left',(12,15),(6,30),12,18,sweep=False)
        arc('bottom-left',(6,30),(16,42),10,12,sweep=False)
        chain('feet',(16,42),(24,42),(32,42))
        arc('bottom-right',(32,42),(42,30),10,12,sweep=False)
        arc('body-right',(42,30),(36,15),12,18,sweep=False)
        contour('body','body-left','bottom-left','feet-1','feet-2','bottom-right','body-right');connect('body','head')
        line('legs',(24,42),(24,33));connect('legs','body')
