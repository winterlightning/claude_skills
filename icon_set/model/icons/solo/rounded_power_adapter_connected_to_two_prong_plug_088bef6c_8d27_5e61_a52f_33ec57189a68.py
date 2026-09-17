"""Electric Power Adapter and Cable.
Symbol plan: Adapter and smaller two-prong plug joined by a continuous cable return.
Reference construction: plug.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '088bef6c-8d27-5e61-a52f-33ec57189a68'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/power adapter_088bef6c-8d27-5e61-a52f-33ec57189a68.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'rounded-power-adapter-connected-to-two-prong-plug'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/electronics'
    aliases = ()
    keywords = ('adapter', 'plug', 'cable', 'power', 'charger', 'connection', 'electric', 'electronics')
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
        rect('adapter',6,14,16,18,4)
        for i,x in enumerate((10,18)):line('adapter-pin'+str(i),(x,6),(x,14))
        poly('plug-top',(30,18),(32,18),(40,18),(42,18),(42,24))
        arc('plug-right',(42,24),(36,30),6)
        arc('plug-left',(36,30),(30,24),6)
        line('plug-side',(30,24),(30,18))
        contour('plug','plug-top-1','plug-top-2','plug-top-3','plug-top-4','plug-right','plug-left','plug-side',closed=True)
        for i,x in enumerate((32,40)):line('plug-pin'+str(i),(x,10),(x,18))
        line('cord-start',(14,32),(14,34))
        arc('cord-bottom',(14,34),(24,42),10,8,sweep=False)
        arc('cord-right',(24,42),(36,30),12,sweep=False)
        contour('cord','cord-start','cord-bottom','cord-right')
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
