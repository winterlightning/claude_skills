"""Two opposed hands frame a shot with index fingers and thumbs. Square envelope preserves the diagonal pair. Lucide hand informs radius-four fingertips and coherent contours; palm creases and secondary knuckle details are omitted. The second hand is a half-turn of the first."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91549f76-161b-4fab-967c-e9a88594ed9e'
SOURCE_PATH = 'pictographic-primitives/photography/hand frame_91549f76-161b-4fab-967c-e9a88594ed9e.svg'
AUTHOR = 'gpt-6'

class HandsFramingShot(Solo48):
    icon_id = 'hands-framing-shot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    aliases = ()
    keywords = ('hands', 'frame', 'framing', 'gesture', 'composition', 'director', 'photography', 'shot')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def segments(n,*p):
            for j,(a,b) in enumerate(zip(p,p[1:]),1):line(n+'-'+str(j),a,b)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'-top',(x-r,y),(x+r,y),r)
            arc(n+'-bottom',(x+r,y),(x-r,y),r)
            contour(n,n+'-top',n+'-bottom',closed=True)

        for k in range(2):
            def p(x,y):return (x,y) if k==0 else (48-x,48-y)
            prefix='hand-'+str(k)+'-'
            line(prefix+'wrist',p(6,6),p(18,6))
            arc(prefix+'knuckle',p(18,6),p(22,10),4)
            line(prefix+'finger-top',p(22,10),p(24,10))
            arc(prefix+'fingertip',p(24,10),p(24,18),4)
            line(prefix+'finger-bottom',p(24,18),p(18,18))
            line(prefix+'thumb-right',p(18,18),p(18,20))
            arc(prefix+'thumbtip',p(18,20),p(10,20),4)
            segments(prefix+'palm',p(10,20),p(10,18),p(6,18),p(6,6))
            contour('hand-'+str(k),*[prefix+s for s in ('wrist','knuckle','finger-top','fingertip','finger-bottom','thumb-right','thumbtip','palm-1','palm-2','palm-3')],closed=True)
