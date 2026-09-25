"""Six iris blades surround a wide central hexagonal opening. Circular envelope follows the iris. Lucide aperture informs circular rim and blade connections. The central opening is larger than in the companion shutter; integer-grid opposite pairs preserve balance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f844d14-8326-56d0-966a-decf22261a63'
SOURCE_PATH = 'pictographic-primitives/photography/lens shutter_8f844d14-8326-56d0-966a-decf22261a63.svg'
AUTHOR = 'gpt-6'

class WideOpenAperture(Solo48):
    icon_id = 'wide-open-aperture'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    aliases = ()
    keywords = ('aperture', 'shutter', 'iris', 'lens', 'open', 'f-stop', 'camera', 'photography')

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

        # Integer points on the radius-20 circle; opposite pairs share parameters.
        rim=[(40,12),(40,36),(24,44),(8,36),(8,12),(24,4)]
        for j,p in enumerate(rim):arc('rim-'+str(j),p,rim[(j+1)%6],20)
        contour('rim',*[f'rim-{j}' for j in range(6)],closed=True)
        inner=[(29,14),(35,24),(30,34),(19,34),(13,24),(18,14)]
        # Each edge continues outward into a blade; join nodes remain explicit.
        for j in range(6):
            poly('blade-'+str(j),rim[j],inner[j],inner[(j-1)%6])
            connect('blade-'+str(j),'rim')
        for j in range(6):connect('blade-'+str(j),'blade-'+str((j+1)%6))
