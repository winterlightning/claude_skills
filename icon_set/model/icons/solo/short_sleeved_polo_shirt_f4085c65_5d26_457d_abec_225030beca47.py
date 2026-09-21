"""Short Sleeve Polo Shirt.

Plan: Retained the polo silhouette, two collar sides and central placket. Reduced folded collar points to a connected V.
Construction reference: Lucide shirt: shoulder and sleeve silhouette; original polo collar retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4085c65-5d26-457d-abec-225030beca47'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/polo_f4085c65-5d26-457d-abec-225030beca47.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'short-sleeved-polo-shirt'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
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
        poly('collar',(16,6),(24,18),(32,6));join('collar','shirt')
        line('placket',(24,18),(24,28));join('placket','collar')
