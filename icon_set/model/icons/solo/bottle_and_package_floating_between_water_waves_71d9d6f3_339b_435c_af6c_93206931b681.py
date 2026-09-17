"""Plastic Waste Floating in Water.
Symbol plan: A tilted bottle and package emerge through separate wave rows.
Reference construction: bottle-wine and wind.
HRECT_L visible extremes: (2, 6, 46, 42); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '71d9d6f3-339b-435c-af6c-93206931b681'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/garbage pollution water_71d9d6f3-339b-435c-af6c-93206931b681.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'bottle-and-package-floating-between-water-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('plastic', 'waste', 'bottle', 'water', 'waves', 'pollution', 'litter', 'ecology')
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
        poly('bottle',(24,20),(28,12),(32,12),(36,8),(44,16),(40,20))
        line('upper',(24,20),(40,20))
        line('upper-end',(40,20),(44,20))
        poly('package',(4,29),(4,22),(12,18),(16,29))
        arc('middle-a',(4,29),(16,29),6,1,sweep=False)
        arc('middle-b',(16,29),(30,29),7,1)
        arc('middle-c',(30,29),(44,29),7,1,sweep=False)
        contour('middle','middle-a','middle-b','middle-c')
        arc('lower',(4,40),(44,40),20,1)
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
