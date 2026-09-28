"""Air Purifier Device.

Symbol plan: Purifier owns housing, mirrored feet, an indicator, and a two-stroke airflow series.
Keyshape VRECT_L: visible ink extremes (6, 2, 42, 46); stroke centerlines inset 2.
Lucide construction reference: air-vent.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e686f130-6226-4d7d-b4c5-09b77a01b089'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/air purifier_e686f130-6226-4d7d-b4c5-09b77a01b089.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'air-purifier-with-two-feet-and-airflow-strokes'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('purifier', 'air', 'device', 'airflow', 'indicator', 'feet', 'home', 'ecology')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def arc(n,a,b,rx,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def contour(n,*parts,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members) & set(parts)]
            self.add_contour(n,*parts,closed=closed)
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
        rect('body',8,16,32,24,4)
        line('indicator',(20,25),(28,25))
        for i,x in enumerate((16,32)):
         line('foot'+str(i),(x,40),(x,44))
         arc('air'+str(i),(x,4),(x,7),3,3,sweep=i==1)
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)
