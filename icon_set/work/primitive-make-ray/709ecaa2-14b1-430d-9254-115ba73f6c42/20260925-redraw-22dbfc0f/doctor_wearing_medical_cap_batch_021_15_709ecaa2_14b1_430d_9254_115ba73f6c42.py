from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '709ecaa2-14b1-430d-9254-115ba73f6c42'
SOURCE_PATH = 'pictographic-primitives/other/doctor_709ecaa2-14b1-430d-9254-115ba73f6c42.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'doctor-wearing-medical-cap-batch-021-15'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('doctor',)

    def build(self):
        # Human user.svg: circular jaw and exact detached ink gap4 (30 to38).
        # Shorter cap restores face proportion; medical cross remains a real plus.
        self.box("cap",12,4,24,18,4)
        self.add_line("cross-h",(21,13),(27,13));self.add_line("cross-v",(24,10),(24,16));self.relate("connect","cross-h","cross-v")
        self.add_arc("jaw",(16,22),(32,22),radius_x=8,sweep=False);self.relate("connect","jaw","cap")
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
