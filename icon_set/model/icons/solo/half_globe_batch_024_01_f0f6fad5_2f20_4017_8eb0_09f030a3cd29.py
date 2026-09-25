from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f0f6fad5-2f20-4017-8eb0-09f030a3cd29'
SOURCE_PATH = 'pictographic-primitives/other/a half of earth_f0f6fad5-2f20-4017-8eb0-09f030a3cd29.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'half-globe-batch-024-01'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('a half of earth',)

    def build(self):
        # Reference crescent hemisphere; two latitude lines retained.
        # Rounded outer hemisphere and smooth concave meridian mirror about y24.
        self.path("hemisphere",(40,4),[((22,4),(8,11),(8,24)),((8,37),(22,44),(40,44)),((33,36),(31,30),(31,24)),((31,18),(33,12),(40,4))],True)
        self.add_line("latitude-n",(11,18),(31,18));self.relate("connect","latitude-n","hemisphere")
        self.add_line("latitude-s",(11,30),(31,30));self.relate("connect","latitude-s","hemisphere")

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

    icon_id = 'half-globe-batch-024-01'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('half', 'globe')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
