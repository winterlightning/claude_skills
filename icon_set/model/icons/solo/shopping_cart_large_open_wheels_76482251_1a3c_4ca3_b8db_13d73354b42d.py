from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '76482251-1a3c-4ca3-b8db-13d73354b42d'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping cart_76482251-1a3c-4ca3-b8db-13d73354b42d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'shopping-cart-large-open-wheels'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    categories = ("shopping", "primitives")
    aliases = ()
    keywords = ('shopping cart',)
    def build(self):
        # Original reference: outlined diagonal handle behind a deep trapezoid basket.
        # VRECT_L centerline bounds8,4..40,44; round transitions, identical wheels.
        self.path("handle",(25,14),[(33,6),((34,5),(35,4),(36,4)),((38,4),(40,7),(38,9)),(33,14)])
        self.path("basket",(12,14),[(36,14),((39,14),(40,14),(40,16)),((40,18),(38,23),(37,26)),((36,28),(35,28),(33,28)),(15,28),((13,28),(12,28),(11,26)),((10,23),(8,18),(8,16)),((8,14),(9,14),(12,14))],True)
        self.relate("connect","handle","basket")
        for x in (16,32):self.circle(f"wheel-{x}",x,40,4)

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

    icon_id = 'shopping-cart-large-open-wheels'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('cart', 'shopping', 'trolley', 'basket', 'wheels', 'retail', 'supermarket')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    exception = {'approved_by': 'user', 'reason': 'User approved the latest redraw shown in the seven remaining icons preview: "exception approval them". Accept the existing spacing, hole and internal-spacing findings for this exact drawing.', 'approved_on': '2026-09-25', 'svg_sha256': 'c981f658cb76172c5dac99335cb1b74eebf723529c21618e453aaab4c22680b9', 'source_svg_sha256': 'c981f658cb76172c5dac99335cb1b74eebf723529c21618e453aaab4c22680b9'}
