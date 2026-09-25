"""An upright lens barrel with a broad rim, grip ribs and tapered mount. Vertical envelope fits the stacked optical barrel. Lucide telescope informs stepped tube construction. Three grip ribs reduce to two; secondary bottom rings are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ddaa16b-34a0-44a7-8793-a732c5ca52ff'
SOURCE_PATH = 'pictographic-primitives/photography/lens vertical_1ddaa16b-34a0-44a7-8793-a732c5ca52ff.svg'
AUTHOR = 'gpt-6'

class UprightLensBarrel(Solo48):
    icon_id = 'upright-lens-barrel'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    aliases = ()
    keywords = ('lens', 'camera lens', 'barrel', 'zoom', 'optics', 'photography', 'grip', 'mount')

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

        poly('barrel',(12,4),(36,4),(40,8),(40,28),(34,36),(34,40),(30,44),(18,44),(14,40),(14,36),(8,28),(8,8),closed=True)
        line('rim',(8,12),(40,12));connect('rim','barrel')
        line('waist',(14,36),(34,36));connect('waist','barrel')
        for x in (20,28):line('rib-'+str(x),(x,21),(x,27))
