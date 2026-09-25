"""VR controller with a rounded head and diagonal handle. Square extremes 6/6/42/42. Lucide gamepad-2 informs sparse controls and rounded housing; oval tracking window becomes a solid slot. Small round button retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '18cfcdec-0823-5e86-8a9f-29b6a04e8e58'
SOURCE_PATH = 'pictographic-primitives/technology/vr controller_18cfcdec-0823-5e86-8a9f-29b6a04e8e58.svg'
AUTHOR = 'gpt-6'

class VrControllerTrackingWindow(Solo48):
    icon_id = 'vr-controller-tracking-window'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('vr', 'controller', 'handheld', 'motion-controller', 'gaming', 'tracking', 'virtual-reality')

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
        arc('head',(14,16),(42,16),14,10)
        arc('head-right',(42,16),(30,26),12,10)
        line('handle-right',(30,26),(22,42));arc('handle-bottom',(22,42),(6,32),16,10)
        chain('handle-left',(6,32),(14,20),(14,16));contour('controller','head','head-right','handle-right','handle-bottom','handle-left-1','handle-left-2',closed=True)
        line('tracking-window',(24,15),(32,15))
        self.add_dot('button',(17,31))
