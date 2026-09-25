from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '71cc0503-f8f3-434e-9c8e-e1524bb2498d'
SOURCE_PATH = 'pictographic-primitives/transportation/bicycle_71cc0503-f8f3-434e-9c8e-e1524bb2498d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'bicycle-angled-handlebar'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('bicycle',)
    def build(self):
        # Source uses two forks to wheel hubs and a single sloped connecting top tube.
        # Lucide bike matched circular wheels; asymmetry follows source steering direction.
        for name,x in (("rear",12),("front",36)):self.circle(name,x,32,8)
        self.add_polyline("rear-fork",(12,32),(19,20),(16,12))
        self.add_line("seat",(12,12),(20,12));self.relate("connect","seat","rear-fork")
        self.add_polyline("front-fork",(36,32),(31,10),(36,8))
        self.add_line("top-tube",(19,20),(33,17))
        for a,b in (("rear-fork","rear"),("front-fork","front"),("top-tube","rear-fork"),("top-tube","front-fork")):self.relate("connect",a,b)

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
