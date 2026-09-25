"""Round webcam with a highlighted lens on a central stand. VRECT_L extremes 8/4/40/44. Lucide webcam informs concentric body/lens and stand. Glint becomes an open quarter of the lens ring; flared foot reduced to a flat bar."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '825e77c3-c219-5795-87b9-8c88097d2887'
SOURCE_PATH = 'pictographic-primitives/technology/webcam_825e77c3-c219-5795-87b9-8c88097d2887.svg'
AUTHOR = 'gpt-6'

class WebcamLensGlint(Solo48):
    icon_id = 'webcam-lens-glint'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('webcam', 'camera', 'video-call', 'lens', 'stream', 'device', 'computer')

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

        arc('lens-top',(24,13),(30,19),6);arc('lens-right',(30,19),(24,25),6);arc('lens-bottom',(24,25),(18,19),6)
        contour('lens','lens-top','lens-right','lens-bottom')
        line('neck',(24,34),(24,44));connect('neck','camera')
        poly('base',(8,44),(24,44),(40,44));connect('base','neck')
