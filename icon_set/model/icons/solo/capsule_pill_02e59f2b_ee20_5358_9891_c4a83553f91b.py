from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '02e59f2b-ee20-5358-9891-c4a83553f91b'
SOURCE_PATH = 'pictographic-primitives/health/pill_02e59f2b-ee20-5358-9891-c4a83553f91b.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'capsule-pill-02e59f2b'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('pill',)

    def build(self):
        # Lucide pill: mirrored rounded caps, parallel walls, perpendicular seam.
        # Cardinal extrema (6,6)-(42,42); both ends have identical geometry.
        self.path("shell",(10,22),[(22,10),((24.56,7.44),(27.38,6),(31,6)),((37.075,6),(42,10.925),(42,17)),((42,20.62),(40.56,23.44),(38,26)),(26,38),((23.44,40.56),(20.62,42),(17,42)),((10.925,42),(6,37.075),(6,31)),((6,27.38),(7.44,24.56),(10,22))],True)
        self.add_line("seam",(16,16),(32,32));self.relate("connect","seam","shell")

    def path(self,name,start,commands,closed=False):
        members=[]
        for i,c in enumerate(commands):
            tag=f"{name}-{i}"
            if len(c)==2: self.add_line(tag,start,c); start=c
            else: self.add_bezier(tag,start,c); start=c[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for i in range(4): self.add_arc(f"{name}-{i}",pts[i],pts[i+1],radius_x=r)
        self.add_contour(name,*[f"{name}-{i}" for i in range(4)],closed=True)

    def box(self,name,x,y,w,h,r=0):
        if not r:
            self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r),(x+r,y)]
        for i in range(8):
            if i%2: self.add_arc(f"{name}-{i}",pts[i],pts[i+1],radius_x=r)
            else: self.add_line(f"{name}-{i}",pts[i],pts[i+1])
        self.add_contour(name,*[f"{name}-{i}" for i in range(8)],closed=True)

    icon_id = 'capsule-pill-02e59f2b'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('capsule', 'pill')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
