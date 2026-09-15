"""Round webcam on a two-leg stand. VRECT_L extremes 8/4/40/44. Lucide webcam informs concentric circles; paired legs retained and thick rounded foot reduced to one flat bar. Identical source pair preserved under distinct UUID-bearing names."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ce6e189f-b50f-4edb-b780-c1a0e3ef5711'
SOURCE_PATH = 'pictographic-primitives/technology/webcam_ce6e189f-b50f-4edb-b780-c1a0e3ef5711.svg'
AUTHOR = 'gpt-6'

class WebcamOnStandAlternate(Solo48):
    icon_id = 'webcam-on-stand-alternate'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('webcam', 'camera', 'video-call', 'lens', 'stand', 'stream', 'device')

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
            chain(n+'r',(r,t+rad),(r,(t+b)//2),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            chain(n+'l',(l,b-rad),(l,(t+b)//2),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r-1','r-2','br','b','bl','l-1','l-2','tl')],closed=True)
        arc('body-tr',(24,4),(39,19),15)
        arc('body-br1',(39,19),(33,31),15);arc('body-br2',(33,31),(24,34),15)
        arc('body-bl1',(24,34),(15,31),15);arc('body-bl2',(15,31),(9,19),15)
        arc('body-tl',(9,19),(24,4),15)
        contour('camera','body-tr','body-br1','body-br2','body-bl1','body-bl2','body-tl',closed=True)

        circle('lens',24,19,6)
        line('left-leg',(15,31),(14,44));line('right-leg',(33,31),(34,44));connect('left-leg','camera');connect('right-leg','camera')
        poly('base',(8,44),(14,44),(34,44),(40,44));connect('base','left-leg');connect('base','right-leg')
