"""Tidal Energy Turbine with Waves.
Symbol plan: Three turbine blades share a central hub below one current stroke.
Reference construction: wind.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1844bd29-3f6c-4752-ac13-83d7452913a2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/tidal energy 1_1844bd29-3f6c-4752-ac13-83d7452913a2.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'three-blade-tidal-turbine-beneath-wavy-current'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    aliases = ()
    keywords = ('tidal', 'turbine', 'water', 'waves', 'energy', 'blades', 'current', 'ecology')
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
        line('blade-top',(20,28),(20,10))
        arc('blade-left',(20,10),(6,24),14,sweep=False)
        line('blade-return',(6,24),(20,28))
        contour('top-blade','blade-top','blade-left','blade-return',closed=True)
        line('blade-right-base',(20,28),(42,28))
        arc('blade-right-curve',(42,28),(20,28),11,10,sweep=False)
        contour('right-blade','blade-right-base','blade-right-curve',closed=True)
        poly('blade-low-base',(20,28),(6,42),(20,42))
        arc('blade-low-curve',(20,42),(20,28),7,sweep=False)
        contour('lower-blade','blade-low-base-1','blade-low-base-2','blade-low-curve',closed=True)
        arc('current',(30,8),(42,8),6,2)
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
