"""Short-sleeved polo shirt with separate collar tips and a central placket. The source collar and the local Lucide shirt silhouette inform the construction."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f4085c65-5d26-457d-abec-225030beca47'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__short-sleeved-polo-shirt/20260927T172707Z-thuan-mac-1/reference/polo_f4085c65-5d26-457d-abec-225030beca47.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'short-sleeved-polo-shirt'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('short', 'sleeved', 'polo', 'shirt')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        poly('shirt',(16,6),(32,6),(38,10),(42,22),(34,26),(34,42),(14,42),(14,26),(6,22),(10,10),(16,6),closed=True)
        # Separated pointed collar leaves the central button placket legible.
        poly('collar-left',(16,6),(22,16),(24,12));join('collar-left','shirt')
        poly('collar-right',(32,6),(26,16),(24,12));join('collar-right','shirt')
        line('placket',(24,12),(24,26));join('placket','collar-left');join('placket','collar-right')
