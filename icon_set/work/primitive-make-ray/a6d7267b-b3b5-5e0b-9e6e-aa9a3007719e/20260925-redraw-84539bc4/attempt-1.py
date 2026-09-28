from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a6d7267b-b3b5-5e0b-9e6e-aa9a3007719e'
SOURCE_PATH = 'pictographic-primitives/furnitures/chair_a6d7267b-b3b5-5e0b-9e6e-aa9a3007719e.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'lounge-chair-side-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('chair',)
    def build(self):
        # Lucide rocking-chair: smooth back-to-seat transition and two splayed legs.
        # Source arm starts at the back and runs forward. Preserve upholstered thickness.
        self.path("shell",(6,10),[((6,6),(11,4),(13,9)),(20,27),(38,27),((43.333,27),(43.333,35),(38,35)),(19,35),((16,35),(14,34),(13,31)),(6,10)],True)
        self.path("arm",(17,19),[(32,19),((35,19),(36,22),(36,27))]);self.relate("connect","arm","shell")
        self.add_line("rear-leg",(17,35),(14,42));self.relate("connect","rear-leg","shell")
        self.add_line("front-leg",(36,35),(39,42));self.relate("connect","front-leg","shell")

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
