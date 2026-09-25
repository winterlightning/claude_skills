"""Electric Power Plug with Cable.
Symbol plan: Two-prong plug with a broad rounded body and a smooth S-shaped cable.
Reference construction: plug.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '92e8c674-3772-4d83-93db-8e77c6711bbd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/phone charger_92e8c674-3772-4d83-93db-8e77c6711bbd.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'two-prong-power-plug-with-s-curved-cord'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'electronics'
    aliases = ()
    keywords = ('plug', 'cable', 'cord', 'power', 'prongs', 'electric', 'connection', 'electronics')
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
        poly('top',(6,20),(6,14),(10,14),(22,14),(26,14),(26,20))
        arc('body-right',(26,20),(16,30),10)
        arc('body-left',(16,30),(6,20),10)
        contour('plug','top-1','top-2','top-3','top-4','top-5','body-right','body-left',closed=True)
        for i,x in enumerate((10,22)):line('pin'+str(i),(x,6),(x,14))
        line('cord-start',(16,30),(16,34))
        arc('cord-a',(16,34),(24,42),8,sweep=False)
        arc('cord-b',(24,42),(32,34),8,sweep=False)
        arc('cord-c',(32,34),(40,26),8)
        line('cord-end',(40,26),(42,26))
        contour('cord','cord-start','cord-a','cord-b','cord-c','cord-end')
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
