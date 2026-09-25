from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '76482251-1a3c-4ca3-b8db-13d73354b42d'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping cart_76482251-1a3c-4ca3-b8db-13d73354b42d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'shopping-cart-large-open-wheels'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('shopping cart',)
    def build(self):
        # Source sloped basket walls, rounded floor corners, matching large wheel rings.
        # Lucide cart informs equal wheels and coherent handle attachment.
        self.path("basket",(4,12),[(44,12),(40,23),((39.5,24.5),(38,25),(36,25)),(12,25),((10,25),(8.5,24.5),(8,23)),(4,12)],True)
        self.add_line("grip",(34,12),(38,8));self.relate("connect","grip","basket")
        for x in (13,35): self.circle(f"wheel-{x}",x,36,4)

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
