from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'df91a888-ce29-4b72-a6a9-d9fd7c079490'
SOURCE_PATH = 'pictographic-primitives/users/man podium_df91a888-ce29-4b72-a6a9-d9fd7c079490.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'man-at-podium'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('man podium',)
    def build(self):
        # Shared user reference: circular head, exact4-unit detached gap, rounded shoulders.
        # Source lectern narrows downward.
        self.circle("head",24,11,5)
        self.add_line("shoulder-left",(12,34),(12,30))
        self.add_arc("shoulder-nw",(12,30),(18,24),radius_x=6)
        self.add_line("shoulder-top",(18,24),(30,24))
        self.add_arc("shoulder-ne",(30,24),(36,30),radius_x=6)
        self.add_line("shoulder-right",(36,30),(36,34))
        self.add_contour("shoulders","shoulder-left","shoulder-nw","shoulder-top","shoulder-ne","shoulder-right")
        self.add_line("top",(6,34),(42,34));self.relate("connect","top","shoulders")
        self.add_line("left",(10,34),(12,42));self.add_line("right",(38,34),(36,42))
        self.relate("connect","left","top");self.relate("connect","right","top")

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
