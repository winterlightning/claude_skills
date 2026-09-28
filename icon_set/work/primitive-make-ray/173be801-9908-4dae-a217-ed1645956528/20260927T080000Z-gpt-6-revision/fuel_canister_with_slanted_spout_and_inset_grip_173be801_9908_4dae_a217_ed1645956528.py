"""Gasoline Fuel Storage Canister.
Symbol plan: Fuel canister with a slanted spout and a separate inset grip in its upper body.
Reference construction: fuel.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '173be801-9908-4dae-a217-ed1645956528'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fuel-canister-with-slanted-spout-and-inset-grip/20260927T075452Z-thuan-mac-1/reference/fossil energy gas can_173be801-9908-4dae-a217-ed1645956528.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'fuel-canister-with-slanted-spout-and-inset-grip'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    categories = ("primitives", "ecology")
    aliases = ()
    keywords = ('fuel', 'canister', 'gasoline', 'spout', 'handle', 'storage', 'petrol', 'container')
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
        upper=[(24,20),(29,14),(38,14)]
        for i,(a,b) in enumerate(zip(upper,upper[1:])):line(f'upper-{i}',a,b)
        arc('top-corner',(38,14),(42,18),4)
        line('right-wall',(42,18),(42,38))
        arc('bottom-right',(42,38),(38,42),4)
        line('base',(38,42),(16,42))
        arc('bottom-left',(16,42),(12,38),4)
        lower=[(12,38),(12,26),(18,20),(24,20)]
        for i,(a,b) in enumerate(zip(lower,lower[1:])):line(f'lower-{i}',a,b)
        contour('outline',*(f'upper-{i}' for i in range(2)),'top-corner','right-wall','bottom-right','base','bottom-left',*(f'lower-{i}' for i in range(3)),closed=True)
        poly('spout',(6,6),(12,8),(24,20))
        self.relate('connect','spout','outline')
        line('grip',(25,30),(33,30))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
