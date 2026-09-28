"""Circular propeller with three curved blades. CIRCLE centerline radius 20 about 24/24. Lucide fan informs curved radial construction; three blades retained, narrow almond outlines reduced to single curved strokes and motion ticks omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '20697f6b-e6a3-48c1-8c44-46bea9f5204c'
SOURCE_PATH = 'pictographic-primitives/technology/tools testflight_20697f6b-e6a3-48c1-8c44-46bea9f5204c.svg'
AUTHOR = 'gpt-6'

class CircleWithThreeBlades(Solo48):
    icon_id = 'circle-with-three-blades'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('propeller', 'blades', 'testflight', 'beta', 'app', 'circle', 'fan')

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
        circle('ring',24,24,20)
        arc('blade-top',(24,24),(24,13),6)
        arc('blade-left',(24,24),(15,29),8)
        arc('blade-right',(24,24),(33,29),8,sweep=False)
        connect('blade-top','blade-left');connect('blade-top','blade-right');connect('blade-left','blade-right')
