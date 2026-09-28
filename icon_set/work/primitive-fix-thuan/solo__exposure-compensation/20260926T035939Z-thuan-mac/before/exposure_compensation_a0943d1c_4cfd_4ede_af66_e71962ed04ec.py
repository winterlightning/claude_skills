"""The photographic exposure-compensation symbol with minus and plus divided diagonally. Square envelope fits the integrated sign. Lucide film informs the frame, and coherent joined strokes keep the divider exact. Plus reduced to compact strokes for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0943d1c-4cfd-4ede-af66-e71962ed04ec'
SOURCE_PATH = 'pictographic-primitives/photography/light mode exposure 1_a0943d1c-4cfd-4ede-af66-e71962ed04ec.svg'
AUTHOR = 'gpt-6'

class ExposureCompensation(Solo48):
    icon_id = 'exposure-compensation'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    categories = ("photography", "primitives")
    aliases = ()
    keywords = ('exposure', 'compensation', 'plus minus', 'camera', 'setting', 'brightness', 'photography', 'ev')

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

        poly('body',(10,6),(38,6),(40,8),(42,10),(42,38),(38,42),(10,42),(8,40),(6,38),(6,10),closed=True)
        line('division',(8,40),(40,8));connect('division','body')
        line('minus',(15,15),(20,15))
        poly('plus-h',(29,32),(32,32),(34,32))
        line('plus-v',(32,29),(32,34));connect('plus-h','plus-v')
