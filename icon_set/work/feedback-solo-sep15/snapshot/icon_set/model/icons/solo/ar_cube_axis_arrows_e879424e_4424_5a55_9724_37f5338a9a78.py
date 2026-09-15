"""AR cube axis diagram with broken corners and outward vertical arrows. Square extremes 6/6/42/42. Lucide box informs the Y junction; coherent side brackets replace four short corner segments. No exact arrow diagram match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e879424e-4424-5a55-9724-37f5338a9a78'
SOURCE_PATH = 'pictographic-primitives/technology/tools ar kit_e879424e-4424-5a55-9724-37f5338a9a78.svg'
AUTHOR = 'gpt-6'

class ArCubeAxisArrows(Solo48):
    icon_id = 'ar-cube-axis-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('ar', 'augmented-reality', 'cube', '3d', 'axis', 'arkit', 'object')

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
        poly('axis',(18,20),(24,24),(30,20));line('vertical',(24,24),(24,28));connect('vertical','axis')
        poly('top-arrow',(20,10),(24,6),(28,10));line('top-stem',(24,6),(24,14));connect('top-stem','top-arrow')
        poly('bottom-arrow',(20,38),(24,42),(28,38));line('bottom-stem',(24,36),(24,42));connect('bottom-stem','bottom-arrow')
        poly('left-corner',(12,14),(6,18),(6,30),(12,34))
        poly('right-corner',(36,14),(42,18),(42,30),(36,34))
