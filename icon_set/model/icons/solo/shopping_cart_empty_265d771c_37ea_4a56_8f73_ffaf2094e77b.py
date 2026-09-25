from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '265d771c-37ea-4a56-8f73-ffaf2094e77b'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping cart empty_265d771c-37ea-4a56-8f73-ffaf2094e77b.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'shopping-cart-empty'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    categories = ("shopping", "other", "primitives-generate")
    aliases = ()
    keywords = ('shopping cart empty',)

    def build(self):
        # Lucide cart: coherent handle/platform contour and equal circular wheels.
        # Reference is intentionally basket-free. HRECT_L: (4,8)-(44,40).
        self.path("platform",(4,24),[(32,24),((34,24),(35,23),(35,21)),(37,11),((37.4,9),(38,8),(40,8)),(44,8)])
        for x in (11,31): self.circle(f"wheel-{x}",x,36,4)

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

    icon_id = 'shopping-cart-empty'
    category = 'shopping'
    categories = ('shopping', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('shopping', 'cart', 'empty')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
