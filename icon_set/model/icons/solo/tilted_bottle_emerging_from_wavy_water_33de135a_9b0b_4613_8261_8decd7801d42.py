"""Bottle Floating in Water.

Symbol plan: Diagonal bottle with open submerged base above a two-period tangent water wave.
Keyshape HRECT_L: visible ink extremes (2, 6, 46, 42); stroke centerlines inset 2.
Lucide construction reference: bottle-wine.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33de135a-9b0b-4613-8261-8decd7801d42'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/garbage pollution soil_33de135a-9b0b-4613-8261-8decd7801d42.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'tilted-bottle-emerging-from-wavy-water'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('bottle', 'water', 'pollution', 'floating', 'waves', 'waste', 'litter', 'ecology')

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
        poly('bottle',(16,26),(23,18),(29,18),(35,8),(43,14),(37,24),(36,26))
        for i in range(4):
         arc('wave'+str(i),(4+i*10,37),(14+i*10,37),5,3,sweep=i%2==0)
        contour('water',*( 'wave'+str(i) for i in range(4)))
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)
