"""Index finger touching an open-corner board. Square extremes 6/6/42/42. Lucide hand informs raised finger and thumb silhouette; other fingers merge into a broad palm and the wrist stays open."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8485b3a4-fcce-4366-a674-06665c2bb463'
SOURCE_PATH = 'pictographic-primitives/technology/virtual touch board_8485b3a4-fcce-4366-a674-06665c2bb463.svg'
AUTHOR = 'gpt-6'

class FingerTouchingBoard(Solo48):
    icon_id = 'finger-touching-board'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('touch', 'finger', 'hand', 'board', 'touchscreen', 'virtual', 'interaction')

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
            line(n+'r',(r,t+rad),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            line(n+'l',(l,b-rad),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)
        poly('board',(6,22),(6,6),(42,6),(42,18))
        arc('finger-tip',(24,19),(32,19),4)
        chain('hand-right',(32,19),(32,28),(40,30),(40,42))
        chain('hand-left',(24,42),(14,30),(16,26),(24,32),(24,19))
        contour('hand','hand-left-1','hand-left-2','hand-left-3','hand-left-4','finger-tip','hand-right-1','hand-right-2','hand-right-3')
