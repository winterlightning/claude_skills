from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '76482251-1a3c-4ca3-b8db-13d73354b42d'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping cart_76482251-1a3c-4ca3-b8db-13d73354b42d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'shopping-cart-large-open-wheels'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('shopping cart',)
    def build(self):
        # Smooth sloping basket, shared tangent transitions, deeper square proportions.
        self.path("basket",(10,10),[(38,10),((41,10),(42,10),(42,12)),((42,14),(41,18),(40,22)),((39,26),(38,26),(35,26)),(13,26),((10,26),(9,26),(8,22)),((7,18),(6,14),(6,12)),((6,10),(7,10),(10,10))],True)
        self.add_line("handle",(34,10),(38,6));self.relate("connect","handle","basket")
        for x in (14,34):self.circle(f"wheel-{x}",x,38,4)

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
