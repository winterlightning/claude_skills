from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd56550d9-6b05-4800-a322-0335dc878173'
SOURCE_PATH = 'pictographic-primitives/other/women_d56550d9-6b05-4800-a322-0335dc878173.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'woman-with-bob-hair-batch-022-15'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('women',)

    def build(self):
        # Human user.svg: circular jaw radius7; exact head30/shoulder38 gap.
        # Soft swept fringe replaces the rejected pointed pentagonal face.
        self.add_line("hair-left",(8,30),(8,20))
        self.add_arc("hair-top",(8,20),(40,20),radius_x=16)
        self.add_line("hair-right",(40,20),(40,30))
        self.add_contour("hair","hair-left","hair-top","hair-right")
        self.path("fringe",(17,19),[((20,18),(23,16),(24,14)),((25,16),(28,18),(31,19))])
        self.add_line("face-left",(17,19),(17,23));self.add_arc("jaw",(17,23),(31,23),radius_x=7,sweep=False);self.add_line("face-right",(31,23),(31,19))
        self.relate("connect","face-left","jaw");self.relate("connect","face-right","jaw");self.relate("connect","fringe","face-left");self.relate("connect","fringe","face-right")
        self.path("shoulders",(8,44),[((8,40),(17,38),(24,38)),((31,38),(40,40),(40,44))])

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
