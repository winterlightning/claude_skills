"""Geothermal Power Plant.
Symbol plan: Two cooling towers at different heights share a baseline above three repeated heat curves.
Reference construction: factory.
HRECT_L visible extremes: (2, 6, 46, 42); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81483a71-208c-589e-90e8-b4046ada23fb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/factory geothermal power plant_81483a71-208c-589e-90e8-b4046ada23fb.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'paired-geothermal-towers-above-heat-strokes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('geothermal', 'plant', 'towers', 'heat', 'energy', 'power', 'industry', 'ecology')
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
        poly('tower-front',(4,28),(10,8),(20,8),(26,28))
        poly('tower-back',(28,18),(30,12),(38,12),(44,28))
        poly('ground',(4,28),(26,28),(44,28))
        for i,x in enumerate((12,24,36)):
         arc('heat'+str(i),(x,37),(x,40),3,3,sweep=bool(i%2))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
