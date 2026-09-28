from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '240918de-1160-4292-9b40-49d0208b6170'
SOURCE_PATH = 'pictographic-primitives/other/technology device smart band_240918de-1160-4292-9b40-49d0208b6170.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'fitness-band-on-wrist'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('technology device smart band',)
    def build(self):
        # Human hand reference vocabulary: relaxed closed hand, smooth lower thumb arc.
        # Restore source wristband seam without changing4-unit stroke.
        self.box("band",12,10,10,28,3)
        self.add_line("arm-top",(4,14),(12,14));self.add_line("arm-bottom",(4,34),(12,34))
        self.path("hand",(22,14),[(38,14),((41,14),(42,15),(42,18)),(44,29),((44,32),(43,32),(40,32)),(33,32)])
        self.path("thumb",(22,34),[((25,34),(26,38),(32,38)),((37,38),(39,36),(39,32))]);self.relate("connect","thumb","hand")
        self.add_line("band-seam",(12,25),(22,21))
        for name in ("arm-top","arm-bottom","hand","thumb","band-seam"):self.relate("connect",name,"band")

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
