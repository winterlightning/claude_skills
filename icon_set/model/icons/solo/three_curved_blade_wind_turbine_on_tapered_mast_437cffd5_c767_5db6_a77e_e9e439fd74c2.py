"""Wind Power Turbine.
Symbol plan: Three broad curved blades meet at a hub supported by a straight mast.
Reference construction: wind.
VRECT_L visible extremes: (6, 2, 42, 46); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '437cffd5-c767-5db6-a77e-e9e439fd74c2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/renewable energy wind turbine_437cffd5-c767-5db6-a77e-e9e439fd74c2.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'three-curved-blade-wind-turbine-on-tapered-mast'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'ecology'
    categories = ('primitives', 'ecology')
    aliases = ()
    keywords = ('wind', 'turbine', 'blades', 'energy', 'mast', 'rotor', 'power', 'ecology')
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
        hub=(24,22)
        poly('top-blade',hub,(24,4),(32,12))
        arc('top-return',(32,12),hub,8,10)
        contour('top','top-blade-1','top-blade-2','top-return',closed=True)
        poly('left-blade',hub,(8,32),(8,22))
        arc('left-return',(8,22),hub,8,7)
        contour('left','left-blade-1','left-blade-2','left-return',closed=True)
        line('right-blade',hub,(40,22))
        arc('right-return',(40,22),(24,32),16,10)
        line('right-close',(24,32),hub)
        contour('right','right-blade','right-return','right-close',closed=True)
        line('mast',(24,32),(24,44))
        poly('ground',(8,44),(24,44),(40,44))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
