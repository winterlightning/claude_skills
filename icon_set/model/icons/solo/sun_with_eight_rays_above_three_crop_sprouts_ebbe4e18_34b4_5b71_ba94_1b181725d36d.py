"""Sun shining over growing plants.
Symbol plan: Sun above three repeated V sprouts and a shared ground line.
Reference construction: sun and sprout.
VRECT_L visible extremes: (6, 2, 42, 46); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ebbe4e18-34b4-5b71-ba94-1b181725d36d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/organic sun growth_ebbe4e18-34b4-5b71-ba94-1b181725d36d.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'sun-with-eight-rays-above-three-crop-sprouts'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    aliases = ()
    keywords = ('sun', 'plants', 'sprouts', 'growth', 'field', 'rays', 'light', 'ecology')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def contour(n,*parts,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members) & set(parts)]
            self.add_contour(n,*parts,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
        def rect(n,x,y,w,h,r=0):
            if not r:
                poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2: arc(n+str(i),a,b,r)
                else: line(n+str(i),a,b)
            contour(n,*(n+str(i) for i in range(8)),closed=True)
        circle('sun',24,16,3)
        for i,(a,b) in enumerate([((24,4),(24,5)),((12,16),(11,16)),((36,16),(37,16)),((24,27),(24,28)),((15,7),(14,6)),((33,7),(34,6)),((15,25),(14,26)),((33,25),(34,26))]):line('ray'+str(i),a,b)
        poly('ground',(8,44),(12,44),(24,44),(36,44),(40,44))
        for i,x in enumerate((12,24,36)):poly('sprout'+str(i),(x-4,36),(x,44),(x+4,36))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
