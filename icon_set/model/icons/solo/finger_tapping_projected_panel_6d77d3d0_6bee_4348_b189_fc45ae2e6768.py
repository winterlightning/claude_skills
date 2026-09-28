"""Finger tapping a projected panel above a projector base. Square extremes 6/6/42/42. Lucide hand informs raised index and thumb; gesture reduced to connected strokes, projector body to a base bar with lens dot to preserve all three scene parts."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6d77d3d0-6bee-4348-b189-fc45ae2e6768'
SOURCE_PATH = 'pictographic-primitives/technology/virtual tap finger_6d77d3d0-6bee-4348-b189-fc45ae2e6768.svg'
AUTHOR = 'gpt-6'

class FingerTappingProjectedPanel(Solo48):
    icon_id = 'finger-tapping-projected-panel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('tap', 'finger', 'hand', 'projection', 'virtual', 'touch', 'panel')

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
        poly('panel',(6,22),(6,6),(42,6),(42,22))
        poly('index',(24,15),(24,24),(24,28))
        line('thumb',(16,20),(24,24));connect('thumb','index')
        poly('palm',(24,28),(32,28),(32,20));connect('palm','index')
        circle('lens',24,40,2)
        poly('base',(14,42),(24,42),(34,42));connect('base','lens')
