"""Direction-pad VR controller with a diagonal handle. Square extremes 6/6/42/42. Lucide gamepad-2 informs connected D-pad strokes; tracking window omitted to give the distinguishing pad clear space in the rounded head."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2400f1b4-29ab-57cc-8024-04a0d1460272'
SOURCE_PATH = 'pictographic-primitives/technology/vr controller_2400f1b4-29ab-57cc-8024-04a0d1460272.svg'
AUTHOR = 'gpt-6'

class VrControllerDirectionPad(Solo48):
    icon_id = 'vr-controller-direction-pad'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('vr', 'controller', 'handheld', 'dpad', 'gaming', 'motion-controller', 'virtual-reality')

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
        arc('head',(14,18),(42,18),14,12)
        arc('head-right',(42,18),(30,30),12)
        line('handle-right',(30,30),(16,42));arc('handle-bottom',(16,42),(6,32),10)
        chain('handle-left',(6,32),(14,22),(14,18));contour('controller','head','head-right','handle-right','handle-bottom','handle-left-1','handle-left-2',closed=True)
        poly('pad-h',(25,18),(28,18),(31,18));poly('pad-v',(28,15),(28,18),(28,21));connect('pad-h','pad-v')
