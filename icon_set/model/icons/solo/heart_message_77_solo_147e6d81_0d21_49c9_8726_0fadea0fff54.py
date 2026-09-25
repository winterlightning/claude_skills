from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '147e6d81-0d21-49c9-8726-0fadea0fff54'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble with heart_147e6d81-0d21-49c9-8726-0fadea0fff54.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'heart-message-77-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('messages bubble with heart',)
    def build(self):
        # Lucide message-square-heart: rounded speech outline with a deep, symmetric heart.
        # SQUARE centerline bounds6..42. Reference has an inset lower-left tail.
        self.path("bubble",(10,6),[(38,6),((40.209,6),(42,7.791),(42,10)),(42,32),((42,34.209),(40.209,36),(38,36)),(24,36),(14,42),(14,36),(10,36),((7.791,36),(6,34.209),(6,32)),(6,10),((6,7.791),(7.791,6),(10,6))],True)
        self.path("heart",(24,27),[(17,21),((12,16),(18,11),(24,17)),((30,11),(36,16),(31,21)),(24,27)],True)

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

    icon_id = 'heart-message-77-solo'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('sub icon', 'message bubble with heart')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
