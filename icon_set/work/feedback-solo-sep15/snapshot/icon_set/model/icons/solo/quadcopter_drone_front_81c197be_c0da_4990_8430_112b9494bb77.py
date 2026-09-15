"""Front-view drone with rotors, pods, central hub and arched skid; HRECT_L fits its width. Lucide drone paired assemblies; pods reduced to solid stems."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81c197be-c0da-4990-8430-112b9494bb77'
SOURCE_PATH = 'pictographic-primitives/technology/drone_81c197be-c0da-4990-8430-112b9494bb77.svg'
AUTHOR = 'gpt-6'

class QuadcopterDroneFront(Solo48):
    icon_id = 'quadcopter-drone-front'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('drone', 'quadcopter', 'propeller', 'aerial', 'uav', 'flying', 'robot')

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
        # Paired rotor assemblies share one axis and dimensions.
        for x in (10,38):
            poly(f'rotor-{x}',(4 if x==10 else 34,8),(x,8),(14 if x==10 else 44,8))
            line(f'mast-{x}',(x,8),(x,18));connect(f'rotor-{x}',f'mast-{x}')
            line(f'pod-{x}',(x,18),(x,26));connect(f'mast-{x}',f'pod-{x}')
        circle('hub',24,20,5)
        line('arm-left',(10,18),(19,20));connect('arm-left','hub');connect('arm-left','mast-10');connect('arm-left','pod-10')
        line('arm-right',(29,20),(38,18));connect('arm-right','hub');connect('arm-right','mast-38');connect('arm-right','pod-38')
        arc('skid',(12,40),(36,40),12,6,sweep=True)
