"""A studio LED panel with six lights and a tapered mount. Square envelope fits the light and its attachment. Lucide camera informs the rectangular equipment housing. Nested LED rings simplify to six dots; the narrow two-stage mount becomes one tapered foot."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90f3e60b-581e-4a28-9204-7bb62d91c267'
SOURCE_PATH = 'pictographic-primitives/photography/light_90f3e60b-581e-4a28-9204-7bb62d91c267.svg'
AUTHOR = 'gpt-6'

class LedPanelLight(Solo48):
    icon_id = 'led-panel-light'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    categories = ("photography", "primitives")
    aliases = ()
    keywords = ('led', 'panel', 'light', 'studio', 'lighting', 'video light', 'photography', 'equipment')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'-top',(x-r,y),(x+r,y),r)
            arc(n+'-bottom',(x+r,y),(x-r,y),r)
            contour(n,n+'-top',n+'-bottom',closed=True)
        def box(n,l,t,r,b,rad=4):
            pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
            for j,a in enumerate(pts):
                z=pts[(j+1)%8]
                if j%2:arc(n+str(j),a,z,rad)
                else:line(n+str(j),a,z)
            contour(n,*[n+str(j) for j in range(8)],closed=True)

        poly('panel',(6,6),(42,6),(42,32),(34,32),(14,32),(6,32),closed=True)
        for y in (15,23):
            for x in (15,24,33):self.add_dot(f'led-{x}-{y}',(x,y))
        poly('mount',(14,32),(18,42),(30,42),(34,32));connect('mount','panel')
