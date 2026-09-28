"""Electric Power Plug with Leaf.
Symbol plan: Plug and leaf physically joined by a looping cord; plug pins share a spacing parameter.
Reference construction: plug and leaf.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0927344c-e0ec-4a0c-b0c8-f920a83c5e88'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/renewable energy charging_0927344c-e0ec-4a0c-b0c8-f920a83c5e88.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'horizontal-power-plug-with-leaf-vein-cord'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('plug', 'leaf', 'cord', 'vein', 'power', 'energy', 'electric', 'ecology')
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
        poly('plug-edge',(14,18),(14,16),(14,8),(14,6),(20,6))
        arc('plug-upper',(20,6),(26,12),6)
        arc('plug-lower',(26,12),(20,18),6)
        line('plug-bottom',(20,18),(14,18))
        contour('plug','plug-edge-1','plug-edge-2','plug-edge-3','plug-edge-4','plug-upper','plug-lower','plug-bottom',closed=True)
        for i,y in enumerate((8,16)): line('pin'+str(i),(6,y),(14,y))
        line('cord-start',(26,12),(34,12))
        arc('cord-turn',(34,12),(42,20),8)
        line('cord-end',(42,20),(42,34))
        contour('cord','cord-start','cord-turn','cord-end')
        arc('leaf-upper',(6,34),(24,26),18,8)
        line('leaf-tip',(24,26),(42,34))
        arc('leaf-lower',(42,34),(6,34),18,8)
        contour('leaf','leaf-upper','leaf-tip','leaf-lower',closed=True)
        line('vein',(42,34),(24,34))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
