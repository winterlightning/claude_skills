"""Virtual cube viewed through a headset. Square extremes 6/6/42/42. Lucide box and headset construction inspected earlier; two repeated cubes reduced to one so its three faces remain clear. Nose dip omitted from the small visor."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e4cb12b0-70f3-46b1-ba40-564dedced675'
SOURCE_PATH = 'pictographic-primitives/technology/virtual boxes_e4cb12b0-70f3-46b1-ba40-564dedced675.svg'
AUTHOR = 'gpt-6'

class VirtualCubesThroughHeadset(Solo48):
    icon_id = 'virtual-cubes-through-headset'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('virtual', 'cubes', 'headset', 'vr', '3d', 'objects', 'immersive')

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
        poly('cube',(14,10),(24,6),(34,10),(34,20),(24,24),(14,20),closed=True)
        poly('top-face',(14,10),(24,15),(34,10));connect('top-face','cube')
        line('edge',(24,15),(24,24));connect('edge','cube');connect('edge','top-face')
        box('headset',14,33,34,42,4)
        poly('left-frame',(6,24),(6,38),(14,38));connect('left-frame','headset')
        poly('right-frame',(42,24),(42,38),(34,38));connect('right-frame','headset')
